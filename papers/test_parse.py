import re

def extract_titles(master_file):
    titles = {}
    with open(master_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = content.split(r'\chapter')
    for part in parts[1:]:
        m_title = re.match(r'(?:\[[^\]]*\])?{([^}]+)}', part)
        if not m_title:
            continue
        title = m_title.group(1)
        # title might have newlines like "Prime Splitting Galois \\ \large\textit{L. Cullen}"
        
        m_input = re.search(r'\\input{([^}]+)}', part)
        if m_input:
            filename = m_input.group(1)
            if not filename.endswith('.tex'):
                filename += '.tex'
            titles[filename] = title
            
    return titles

print(extract_titles('01_Principia_Psychedelia_Master.tex'))
