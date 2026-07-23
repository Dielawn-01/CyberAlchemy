import os
import re

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    def replacer(match):
        # match.group(1) is the content inside \texttt{...}
        inner = match.group(1)
        # replace any unescaped _ with \_
        # wait, just replacing all _ with \_ inside is safer:
        # but what if it's already \_ ?
        inner = inner.replace('\\_', '_') # first unescape all just in case
        inner = inner.replace('_', '\\_') # then escape all
        return '\\texttt{' + inner + '}'

    # regex to find \texttt{...}
    # handles simple cases without nested braces
    new_content = re.sub(r'\\texttt{([^{}]+)}', replacer, content)

    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {path}")

base_dir = '/home/phrxmaz/Documents/CyberAlchemy/papers'
for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.tex'):
            fix_file(os.path.join(root, file))
