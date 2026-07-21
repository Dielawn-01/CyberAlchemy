import os
import subprocess
import shutil
import re

def extract_titles(base_dir):
    titles = {}
    # Extract from all Master files to be safe
    for master in ['01_Principia_Psychedelia_Master.tex', '02_Vol1_Master.tex', '03_Vol2_Master.tex']:
        path = os.path.join(base_dir, master)
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        parts = content.split(r'\chapter')
        for part in parts[1:]:
            part = re.sub(r'^\[[^\]]*\]', '', part).lstrip()
            if not part.startswith('{'):
                continue
                
            depth = 0
            title = ""
            for char in part:
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
                        
            m_input = re.search(r'\\input{([^}]+)}', part)
            if m_input:
                filename = m_input.group(1)
                if not filename.endswith('.tex'):
                    filename += '.tex'
                if filename not in titles:
                    titles[filename] = title.strip()
    return titles

def build_pdf(tex_file, out_dir, use_wrapper=False, titles=None):
    if titles is None:
        titles = {}
    print(f"Building {os.path.basename(tex_file)} into {out_dir}...")
    base_dir = os.path.dirname(tex_file)
    filename = os.path.basename(tex_file)
    
    if use_wrapper:
        title = titles.get(filename, filename.replace('.tex', '').replace('_', ' '))
        wrapper_path = os.path.join(base_dir, f"wrapper_{filename}")
        with open(wrapper_path, "w") as f:
            f.write(r"""\documentclass[12pt,oneside]{article}
\input{common_preamble}
\title{%s}
\author{Dylon La Rue}
\date{}
\begin{document}
\maketitle
\input{%s}
\input{unified_bibliography}
\end{document}
""" % (title, filename))
        target_file = wrapper_path
    else:
        target_file = tex_file
        
    try:
        subprocess.run(['tectonic', '-o', out_dir, target_file], check=True)
        
        if use_wrapper:
            # Rename the output PDF from wrapper_...pdf to original name
            wrapper_pdf = os.path.join(out_dir, f"wrapper_{filename.replace('.tex', '.pdf')}")
            final_pdf = os.path.join(out_dir, filename.replace('.tex', '.pdf'))
            if os.path.exists(wrapper_pdf):
                os.rename(wrapper_pdf, final_pdf)
                
        print(f"Successfully built {filename}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to build {filename}")
    finally:
        if use_wrapper and os.path.exists(wrapper_path):
            os.remove(wrapper_path)

def main():
    base_dir = '/home/phrxmaz/Documents/CyberAlchemy/papers'
    build_dir = os.path.join(base_dir, 'build')
    
    volumes_dir = os.path.join(build_dir, 'Volumes')
    papers_dir = os.path.join(build_dir, 'papers')
    
    os.makedirs(build_dir, exist_ok=True)
    os.makedirs(volumes_dir, exist_ok=True)
    os.makedirs(papers_dir, exist_ok=True)
    
    titles = extract_titles(base_dir)
    
    # Book
    print("\n--- Compiling Volumes ---")
    build_pdf(os.path.join(base_dir, "02_Vol1_Master.tex"), os.path.join(base_dir, "build/Volumes"))
    build_pdf(os.path.join(base_dir, "03_Vol2_Master.tex"), os.path.join(base_dir, "build/Volumes"))
    build_pdf(os.path.join(base_dir, "04_Vol3_Master.tex"), os.path.join(base_dir, "build/Volumes"))
    build_pdf(os.path.join(base_dir, "05_Vol4_Master.tex"), os.path.join(base_dir, "build/Volumes"))

    print("\n--- Compiling Master Book ---")
    build_pdf(os.path.join(base_dir, "01_Principia_Psychedelia_Master.tex"), os.path.join(base_dir, "build"))
    build_pdf(os.path.join(base_dir, "01_Principia_Psychedelia_Full.tex"), os.path.join(base_dir, "build"))
        
    # Papers
    for file in os.listdir(base_dir):
        if file.endswith('.tex') and file[0].isdigit() and 'Master' not in file and 'Whitepaper' not in file:
            build_pdf(os.path.join(base_dir, file), papers_dir, use_wrapper=True, titles=titles)
        elif file.endswith('.tex') and 'Whitepaper' in file:
            # Whitepapers usually have \documentclass
            build_pdf(os.path.join(base_dir, file), papers_dir, use_wrapper=False, titles=titles)
            
    # Clean up aux files
    for d in [build_dir, volumes_dir, papers_dir]:
        for root, _, files in os.walk(d):
            for f in files:
                if not f.endswith('.pdf') and os.path.isfile(os.path.join(root, f)):
                    try:
                        os.remove(os.path.join(root, f))
                    except OSError:
                        pass
                    
if __name__ == "__main__":
    main()
