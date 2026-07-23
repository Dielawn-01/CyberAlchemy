import os
import re
import glob

bib_file = 'unified_bibliography.tex'

# Parse unified bibliography
bib_dict = {}
with open(bib_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all bibitems
# Regex matches \bibitem{key} followed by everything until the next \bibitem or \end{thebibliography}
matches = re.finditer(r'\\bibitem\{([^}]+)\}(.*?)(?=\\bibitem\{|\\end\{thebibliography\}|% ===)', content, re.DOTALL)
for match in matches:
    key = match.group(1).strip()
    entry = match.group(2).strip()
    bib_dict[key] = f"\\bibitem{{{key}}}\n{entry}\n"

# Process all tex files
tex_files = glob.glob('*.tex')
for tex in tex_files:
    if 'Master' in tex or tex == bib_file or tex.startswith('wrapper_'):
        continue
    
    with open(tex, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # Remove any existing \input{unified_bibliography} or similar
    file_content = re.sub(r'\\input\{.*?bib.*?\}', '', file_content)
    
    # If thebibliography is already embedded, skip or remove?
    if r'\begin{thebibliography}' in file_content:
        # We assume it's already done or we shouldn't touch it.
        # But maybe we want to clean it up? Let's just say if it's there, skip for now.
        pass
    
    # Extract citations
    # \cite{key1, key2} or \cite[page]{key}
    cites = []
    for m in re.finditer(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', file_content):
        keys = m.group(1).split(',')
        for k in keys:
            k = k.strip()
            if k:
                cites.append(k)
    
    unique_cites = list(set(cites))
    
    if unique_cites and r'\begin{thebibliography}' not in file_content:
        bib_block = "\n\\vspace{2em}\n\\begin{thebibliography}{99}\n"
        for k in sorted(unique_cites):
            if k in bib_dict:
                bib_block += bib_dict[k] + "\n"
            else:
                print(f"WARNING: Citation {k} not found in unified_bibliography for file {tex}")
        bib_block += "\\end{thebibliography}\n"
        
        file_content += bib_block
        
        with open(tex, 'w', encoding='utf-8') as f:
            f.write(file_content)
        print(f"Embedded bibliography into {tex} with {len(unique_cites)} citations.")

print("Done embedding bibliographies.")
