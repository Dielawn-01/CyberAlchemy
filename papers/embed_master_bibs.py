import os
import re

bib_file = 'unified_bibliography.tex'

# Parse unified bibliography
bib_dict = {}
with open(bib_file, 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.finditer(r'\\bibitem\{([^}]+)\}(.*?)(?=\\bibitem\{|\\end\{thebibliography\}|% ===)', content, re.DOTALL)
for match in matches:
    key = match.group(1).strip()
    entry = match.group(2).strip()
    bib_dict[key] = f"\\bibitem{{{key}}}\n{entry}\n"

masters = ['01_Principia_Psychedelia_Master.tex', '02_Vol1_Master.tex', '03_Vol2_Master.tex', '04_Vol3_Master.tex', '05_Vol4_Master.tex']

for master in masters:
    if not os.path.exists(master):
        continue
        
    with open(master, 'r', encoding='utf-8') as f:
        master_content = f.read()

    # Find all inputs
    inputs = re.findall(r'\\input\{([^}]+)\}', master_content)
    
    all_cites = set()
    
    # Also find cites in the master itself just in case
    for m in re.finditer(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', master_content):
        keys = m.group(1).split(',')
        for k in keys:
            if k.strip(): all_cites.add(k.strip())
            
    for inp in inputs:
        inp_file = inp if inp.endswith('.tex') else inp + '.tex'
        if os.path.exists(inp_file):
            with open(inp_file, 'r', encoding='utf-8') as f:
                inp_content = f.read()
            for m in re.finditer(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', inp_content):
                keys = m.group(1).split(',')
                for k in keys:
                    if k.strip(): all_cites.add(k.strip())
                    
    if all_cites:
        bib_block = "\n\\vspace{2em}\n\\begin{thebibliography}{99}\n"
        for k in sorted(all_cites):
            if k in bib_dict:
                bib_block += bib_dict[k] + "\n"
            else:
                print(f"WARNING: Citation {k} not found in unified_bibliography for {master}")
        bib_block += "\\end{thebibliography}\n"
        
        # Replace the unified bib comment block or insert before \end{document}
        # First remove any existing bibliography block if we added it before
        master_content = re.sub(r'\\vspace\{2em\}\n\\begin\{thebibliography\}.*?\\end\{thebibliography\}\n', '', master_content, flags=re.DOTALL)
        
        # Find where to insert
        if r'\end{document}' in master_content:
            master_content = master_content.replace(r'\end{document}', bib_block + r'\end{document}')
            with open(master, 'w', encoding='utf-8') as f:
                f.write(master_content)
            print(f"Embedded tailored bibliography into {master} with {len(all_cites)} citations.")
