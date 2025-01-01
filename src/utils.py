import os

# Order files in the directory
def extract_num(filename):
    return int(''.join(filter(str.isdigit, filename)) or 0)


# Callouts
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



