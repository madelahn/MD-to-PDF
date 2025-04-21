import re

# Order files in the directory
def extract_num(filename):
    return int(''.join(filter(str.isdigit, filename)) or 0)


def format_math(match):
    content = match.group(1)
    lines = content.strip().splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    math_block = '\n'.join(cleaned_lines)
    return f'\\begin{{align*}}\n{math_block}\n\\end{{align*}}'


# Callouts
def format_callout(match):
    color = match.group(1).lower()
    title = match.group(2)
    raw_content = match.group(3)
    lines = [line.lstrip("> ").rstrip() for line in raw_content.splitlines()]

    box_lines = []
    post_box_lines = []
    in_box = True

    for line in lines:
        if in_box and re.match(r'^#{1,6}\s', line):
            in_box = False
        if in_box:
            box_lines.append(line)
        else:
            post_box_lines.append(line)
    box_content = "\n".join(box_lines).strip()
    post_content = "\n".join(post_box_lines).strip()

    result = (
        f'\\begin{{tcolorbox}}[colback={color}!5!white, '
        f'colframe={color}!75!black, title={title}]\n'
        f'{box_content}\n'
        '\\end{tcolorbox}\n\n'
    )

    if post_content:
        result += post_content + "\n\n"

    return result
