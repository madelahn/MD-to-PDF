import os
import re
import subprocess
import sys
import yaml


# Order files in the directory
def extract_num(filename):
    return int(''.join(filter(str.isdigit, filename)) or 0)


def format_callout(match):
    color = match.group(1).lower()
    title = match.group(2)
    content = match.group(3).replace("> ", "").strip()

    return (
        f'\\begin{{tcolorbox}}[colback={color}!5!white, '
        f'colframe={color}!75!black, title={title}]\n'
        f'{content}\n'
        '\\end{tcolorbox}\n\n'
    )


# Preprocess markdown files from Obsidian
def preprocess(filepath):
    image_dir = os.path.join(dir, "Images")
    image_dir = image_dir.replace("\\", "/")

    with open(filepath, "r") as file:
        content = file.readlines()
        
    # Skip the first line
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
    processed_content = re.sub(r'\$\$(.*?)\$\$', lambda match: fr"$${match.group(1)}$$", processed_content, flags=re.DOTALL)
    processed_content = re.sub(r'align\*', r'aligned', processed_content)

    # Add filename as a header
    filename = os.path.basename(filepath)
    header = f"# {os.path.splitext(filename)[0]}\n\n"
    processed_content = header + processed_content
        
    return processed_content


def mdToPdf():
    # Check if dir exists
    if not os.path.exists(dir):
        print(f"Directory {dir} does not exist.")
        sys.exit(1)
    print(f"---\nMerging files for {dir}\n---")

    # Merge into one MD file
    with open(merged_file, "w") as merged:
        merged.write(r"\newpage")
        for filename in sorted(os.listdir(dir), key=extract_num):
            if (filename.endswith(".md")):
                preprocess(os.path.join(dir, filename))
                processed_content = preprocess(os.path.join(dir, filename))
                merged.write(processed_content)
                merged.write("\n\n")
                print(f"File merged: {filename}")
    print("---\nFiles merged successfully.\nGenerating PDF...\n---")

    # Generate PDF using Pandoc
    try:
        course = os.path.basename(dir.strip('/'))
        subprocess.run(
            [
            "pandoc", 
            merged_file, 
            "-o", f"{course}.pdf",
            "--pdf-engine=xelatex",
            "-f", "markdown+tex_math_dollars+raw_tex",
            f"--metadata=title:{course}",
            "-V", "geometry:margin=1in",
            "--toc", "--toc-depth=3",
            "--include-in-header", "TeX/header.tex",
            ], check=True
        )
        print(f"PDF successfully generated!")
        if not config["debug"]["save-md"]:
            os.remove(merged_file)

    except FileNotFoundError:
        print(f"Error: Pandoc not found.")

    except subprocess.CalledProcessError as e:
        print(f"Error generating PDF: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py md-pdf.py <directory>")
        sys.exit(1)

    yaml_file = 'config.yaml'
    with open(yaml_file, 'r') as f:
        config = yaml.load(f, loader=yaml.FullLoader)

    dir = rf"{sys.argv[1]}"
    merged_file = "merged.md"
    pdf = "compiled.pdf"

    mdToPdf()