import re, subprocess, os
import config
from utils import extract_num, format_callout, format_math


def merge_files(dir):
    print(f"---\nMerging files for {dir}\n---")
    with open("merged.md", "w") as merged:
        merged.write(r"\newpage" + "\n\n")
        for filename in sorted(os.listdir(dir), key=extract_num):
            if (filename.endswith(".md")):
                processed_content = preprocess(os.path.join(dir, filename), dir)
                merged.write(processed_content)
                merged.write("\n\n")
                print(f"File merged: {filename}")
    print("---\nFiles merged successfully.")


# Preprocess markdown files from Obsidian
def preprocess(filepath, dir):
    if not isinstance(config.IMAGE_DIR, str):
        raise ValueError(f"Expected config.IMAGE_DIR to be a string, got {type(config.IMAGE_DIR)}.")
    image_dir = os.path.join(dir, config.IMAGE_DIR)
    image_dir = image_dir.replace("\\", "/")

    with open(filepath, "r") as file:
        content = file.readlines()
        
    # Skip YAML header and first line
    if content[0].strip() == "---":
        for i, line in enumerate(content[1:], start=1):
            if line.strip() == "---":
                content = content[i+1:]
                break
    content = content[1:]
    content = ''.join(content)
    
    # Image embeds: ![[image.png]] -> ![Alt](Images/image.png)
    processed_content = re.sub(r'!\[\[(.*?)\]\]', fr'\n![\1]({image_dir}/\1)', content)

    # Bullet and numbered lists
    processed_content = re.sub(r'^-\s', '\n- ', processed_content, flags=re.MULTILINE)
    processed_content = re.sub(r'^\d+\.\s', lambda match: f"\n{match.group(0)}", processed_content, flags=re.MULTILINE)

    # Add a new line before headers
    processed_content = re.sub(r'^(#{1,6})\s', r'\n\1 ', processed_content, flags=re.MULTILINE)

    # Add one # to all headers
    processed_content = re.sub(r'^(#{1,6})\s', lambda match: f"{match.group(1)}# ", processed_content, flags=re.MULTILINE)
    # TODO: Exclude from code blocks (```)

    # Remove highlights
    processed_content = re.sub(r'==.==', '', processed_content)

    # Callouts
    processed_content = re.sub(
        r'> \[\!(\w+)\] (.*?)\n((?:> .*\n)*)',
        format_callout,
        processed_content,
        flags=re.DOTALL
    )

    # Math Equations
    processed_content = re.sub(
        r'\$\$\s*\\begin\{align\*?\}(.*?)\\end\{align\*?\}\s*\$\$',
        lambda m: format_math(m),
        processed_content,
        flags=re.DOTALL
    )
    
    # Add filename as a header
    filename = os.path.basename(filepath)
    header = f"# {os.path.splitext(filename)[0]}\n\n"
    processed_content = header + processed_content
        
    return processed_content


def make_pdf(dir):
    try:
        course = os.path.basename(dir.strip('/'))
        subprocess.run(
            [
            "pandoc", 
            "merged.md", 
            "-o", f"{course}.pdf",
            "--pdf-engine=xelatex",
            "-f", "markdown+tex_math_dollars+raw_tex",
            f"--metadata=title:{course}",
            "-V", "geometry:margin=1in",
            "--toc", "--toc-depth=3",
            "--include-in-header", "TeX/header.tex",
            # "--verbose"
            ], check=True
        )
        print(f"PDF successfully generated!")
        if not config.SAVE_MD:
            os.remove("merged.md")

    except FileNotFoundError:
        print(f"Error: Pandoc not found.")

    except subprocess.CalledProcessError as e:
        print(f"Error generating PDF: {e}")