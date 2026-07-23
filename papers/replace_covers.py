import os
import re

files_to_update = [
    '01_Principia_Psychedelia_Master.tex',
    '02_Vol1_Master.tex',
    '03_Vol2_Master.tex',
    '04_Vol3_Master.tex',
    '05_Vol4_Master.tex',
    '01_Principia_Psychedelia_Full.tex'
]

title_map = {
    '01_Principia_Psychedelia_Master.tex': r'PRINCIPIA PSYCHEDELIA',
    '01_Principia_Psychedelia_Full.tex': r'PRINCIPIA PSYCHEDELIA (FULL)',
    '02_Vol1_Master.tex': r'VOLUME I',
    '03_Vol2_Master.tex': r'VOLUME II',
    '04_Vol3_Master.tex': r'VOLUME III',
    '05_Vol4_Master.tex': r'VOLUME IV',
}

base_dir = '/home/phrxmaz/Documents/CyberAlchemy/papers'

for fname in files_to_update:
    path = os.path.join(base_dir, fname)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    title_text = title_map[fname]
    
    new_titlepage = r"""\begin{titlepage}
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  \fill[black] (current page.north west) rectangle (current page.south east);
  \node[anchor=center, opacity=0.85] at (current page.center) {\includegraphics[width=\paperwidth, height=\paperheight, keepaspectratio]{images/genome_cover.png}};
  \node[anchor=center] at ([yshift=3cm]current page.center) {\fontsize{16}{20}\selectfont\sffamily\color{white}\addfontfeatures{LetterSpace=12}""" + title_text + r"""};
  \node[anchor=center, text width=12cm, align=center] at ([yshift=-3.5cm]current page.center) {\fontsize{22}{28}\selectfont\bfseries\color{white}The Mathematics of Metareality};
  \node[anchor=center] at ([yshift=-7cm]current page.center) {\fontsize{18}{22}\selectfont\color{white}\textbf{Dylon La Rue}};
\end{tikzpicture}
\end{titlepage}"""
    
    start_idx = content.find(r'\begin{titlepage}')
    end_idx = content.find(r'\end{titlepage}')
    if start_idx != -1 and end_idx != -1:
        end_idx += len(r'\end{titlepage}')
        content = content[:start_idx] + new_titlepage + content[end_idx:]
    
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {fname}")
    else:
        print(f"Could not find titlepage in {fname}")

