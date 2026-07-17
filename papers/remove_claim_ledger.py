import os
import re

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Regex to find Claim Ledger block:
    # Matches from %==========... down to \section*{Claim Ledger} and then everything until \end{itemize}
    # Wait, some might have \end{itemize} but some might not? Let's check 10_chiral_casimir_experiment.tex.
    # It has \begin{itemize} ... \end{itemize}
    
    # Let's use a simpler pattern:
    # Match "\section*{Claim Ledger}" and anything after it up to but not including the next "\section{" or "\subsection{" or "\newpage" or EOF.
    
    pattern = re.compile(r'(?:%[=]+\n)?\\section\*\{Claim Ledger\}(?:.|\n)*?(?=\n(?:%[=]+\n)?\\(?:sub)?section|\n\\newpage|\Z)', re.MULTILINE)
    
    new_content = pattern.sub('', content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Removed Claim Ledger from {filepath}")

for root, _, files in os.walk('/home/phrxmaz/Documents/CyberAlchemy/papers'):
    for file in files:
        if file.endswith('.tex'):
            process_file(os.path.join(root, file))

