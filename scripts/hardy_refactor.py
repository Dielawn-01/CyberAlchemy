import os
import re
from pathlib import Path

# Terms to sanitize
REPLACEMENTS = [
    (r"(?i)physical creativity engine", "foundational prime field"),
    (r"(?<!\\texttt\{)(?<!\\texttt\{ )CyberAlchemy(?!/)(?!\}|\.\w)", "the Adelic Cohomology Framework"),
    (r"(?i)Unreal Algebra", "Arithmetic Scheme Topos"),
    (r"(?i)Protoreal Manifold", "Motivic Scheme"),
    (r"(?i)Semantic Condensation", "Topological Phase Transition"),
    (r"(?i)metareal", "arithmetic scheme"),
]

def sanitize_tex(content):
    for pattern, replacement in REPLACEMENTS:
        # We use re.sub, handling case insensitivity where specified
        content = re.sub(pattern, replacement, content)
    return content

def parse_bibliography(bib_path):
    with open(bib_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract \bibitem{key} blocks
    blocks = {}
    
    # Find all \bibitem
    matches = list(re.finditer(r'\\bibitem\{([^}]+)\}', content))
    
    for i, match in enumerate(matches):
        key = match.group(1).strip()
        start = match.start()
        end = matches[i+1].start() if i + 1 < len(matches) else content.find(r'\end{thebibliography}')
        if end == -1: end = len(content)
        
        block_content = content[start:end].strip()
        blocks[key] = block_content
        
    return blocks

def process_file(filepath, unified_bib_blocks, bib_dir):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Sanitize content
    new_content = sanitize_tex(content)
    
    # Extract cited keys
    cited_keys = set()
    for match in re.finditer(r'\\cite(?:p|t)?\{([^}]+)\}', new_content):
        keys = [k.strip() for k in match.group(1).split(',')]
        for k in keys:
            cited_keys.add(k)
            
    # If this file inputs the unified bibliography, replace it and generate local bib
    bib_input_pattern = r'\\input\{.*?unified_bibliography\}'
    if re.search(bib_input_pattern, new_content):
        # Generate local bibliography
        basename = os.path.basename(filepath)
        name_without_ext = os.path.splitext(basename)[0]
        local_bib_filename = f"local_bib_{name_without_ext}.tex"
        local_bib_path = os.path.join(bib_dir, local_bib_filename)
        
        # Create the local bib content
        local_bib_content = ["\\begin{thebibliography}{99}"]
        for key in sorted(cited_keys):
            if key in unified_bib_blocks:
                local_bib_content.append(unified_bib_blocks[key])
            else:
                print(f"Warning: Citation '{key}' in {basename} not found in unified_bibliography.tex")
        local_bib_content.append("\\end{thebibliography}")
        
        with open(local_bib_path, 'w', encoding='utf-8') as f:
            f.write("\n\n".join(local_bib_content))
            
        # Replace the input command in the tex file
        # We need to figure out the relative path to bib_dir
        rel_path_to_bib = os.path.relpath(local_bib_path, start=os.path.dirname(filepath))
        # Remove .tex extension for \input
        rel_path_to_bib = os.path.splitext(rel_path_to_bib)[0]
        
        # Replace Windows backslashes with forward slashes for LaTeX
        rel_path_to_bib = rel_path_to_bib.replace('\\', '/')
        
        new_content = re.sub(bib_input_pattern, f"\\\\input{{{rel_path_to_bib}}}", new_content)
        
    # Write back if changed
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

if __name__ == "__main__":
    base_dir = "/home/phrxmaz/Documents/CyberAlchemy/papers"
    unified_bib_path = os.path.join(base_dir, "unified_bibliography.tex")
    
    # We will save local bibs in a new directory or alongside unified
    local_bibs_dir = os.path.join(base_dir, "local_bibs")
    os.makedirs(local_bibs_dir, exist_ok=True)
    
    print("Parsing unified bibliography...")
    bib_blocks = parse_bibliography(unified_bib_path)
    print(f"Found {len(bib_blocks)} bibliography entries.")
    
    changed_files = 0
    
    # Process all tex files
    for root, dirs, files in os.walk(base_dir):
        # Exclude build directory and local_bibs
        if "build" in root or "local_bibs" in root:
            continue
            
        for file in files:
            if file.endswith(".tex") and file != "unified_bibliography.tex":
                filepath = os.path.join(root, file)
                if process_file(filepath, bib_blocks, local_bibs_dir):
                    print(f"Updated {os.path.relpath(filepath, base_dir)}")
                    changed_files += 1
                    
    print(f"Refactor complete. Modified {changed_files} files.")
