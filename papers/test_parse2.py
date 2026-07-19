import re

def extract_titles(master_file):
    titles = {}
    with open(master_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = content.split(r'\chapter')
    for part in parts[1:]:
        # Remove optional [...]
        part = re.sub(r'^\[[^\]]*\]', '', part).lstrip()
        
        if not part.startswith('{'):
            continue
            
        # extract matching braces
        depth = 0
        title = ""
        for i, char in enumerate(part):
            if char == '{':
                depth += 1
                if depth > 1: title += char
            elif char == '}':
                depth -= 1
                if depth == 0:
                    break
                title += char
            else:
                if depth > 0:
                    title += char
                    
        # find input
        m_input = re.search(r'\\input{([^}]+)}', part)
        if m_input:
            filename = m_input.group(1)
            if not filename.endswith('.tex'):
                filename += '.tex'
            titles[filename] = title.strip()
            
    return titles

print(extract_titles('01_Principia_Psychedelia_Master.tex'))
