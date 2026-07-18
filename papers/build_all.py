import os
import subprocess
import shutil

def build_pdf(tex_file, out_dir, use_wrapper=False):
    print(f"Building {os.path.basename(tex_file)} into {out_dir}...")
    base_dir = os.path.dirname(tex_file)
    filename = os.path.basename(tex_file)
    
    if use_wrapper:
        wrapper_path = os.path.join(base_dir, f"wrapper_{filename}")
        with open(wrapper_path, "w") as f:
            f.write(r"""\documentclass[12pt,oneside]{book}
\input{common_preamble}
\begin{document}
\input{%s}
\end{document}
""" % filename)
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
    
    # Book
    build_pdf(os.path.join(base_dir, '01_Principia_Psychedelia_Master.tex'), build_dir)
    
    # Volumes
    for vol in ['02_Vol1_Master.tex', '03_Vol2_Master.tex']:
        if os.path.exists(os.path.join(base_dir, vol)):
            build_pdf(os.path.join(base_dir, vol), volumes_dir)
        
    # Papers
    for file in os.listdir(base_dir):
        if file.endswith('.tex') and file[0].isdigit() and 'Master' not in file and 'Whitepaper' not in file:
            build_pdf(os.path.join(base_dir, file), papers_dir, use_wrapper=True)
        elif file.endswith('.tex') and 'Whitepaper' in file:
            # Whitepapers usually have \documentclass
            build_pdf(os.path.join(base_dir, file), papers_dir, use_wrapper=False)
            
    # Clean up aux files (tectonic usually cleans up its own aux files, but just in case)
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
