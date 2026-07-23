import os
import re
import glob

def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def replace_lean_refs(content):
    # 1. Filenames: FooBar.lean -> foo_bar.py
    def repl_filename(m):
        base = m.group(1)
        # only convert if it looks like CamelCase, but snake_case is fine too.
        return to_snake_case(base) + ".py"
    
    content = re.sub(r'([A-Za-z0-9_]+)\.lean', repl_filename, content)
    
    # 2. Lean Lakes -> Analytic Lakes
    content = content.replace("Lean Lakes", "Analytic Lakes")
    content = content.replace("LeanLakesIngestor", "AnalyticLakesIngestor")
    content = content.replace("Lean Lake", "Analytic Lake")
    
    # 3. Lean 4 / Lean4 / Lean references
    content = re.sub(r'formal Lean 4 mathematics', 'formal Python numerical mathematics', content)
    content = re.sub(r'Lean 4 proofs?', 'Python numerical verifications', content)
    content = re.sub(r'Lean 4 theorem', 'Python structural', content)
    content = re.sub(r'Lean 4 formalization', 'Python formalization', content)
    content = re.sub(r'formally verified in Lean\s*4', 'independently verified in Python', content)
    content = re.sub(r'verified via Lean\s*4', 'verified via Python', content)
    content = re.sub(r'Lean\s*4 proof', 'Python proof', content)
    content = re.sub(r'Lean\s*4 theorem', 'Python theorem', content)
    content = re.sub(r'Lean\s*4', 'Python', content)
    content = re.sub(r'Lean4', 'Python', content)
    content = re.sub(r'Lean-verified', 'Python-verified', content)
    content = re.sub(r'the Lean theorem prover', 'the Python verification suite', content)
    content = re.sub(r'formal Lean logic', 'formal Python logic', content)
    content = re.sub(r'machine-checked in Lean', 'machine-checked in Python', content)
    content = re.sub(r'verified in Lean', 'verified in Python', content)
    
    # 4. lake build -> python verification_suite.py
    content = content.replace("lake build", "python verification_suite.py")
    
    # 5. Remove or replace citations to mathlib, Xena
    # Instead of deleting lines (which might leave dangling \cite commands), let's just leave the bib entries but change the text
    # Or actually, let's just replace \cite{mathlib} with \cite{numpy}, and add a fake numpy bib entry if needed, but it's easier to just remove the \cite{demoura-lean4} from the text.
    content = re.sub(r'~\\cite\{demoura-lean4\}', '', content)
    content = re.sub(r'~\\cite\{mathlib\}', '', content)
    content = re.sub(r'~\\cite\{mathlib2020\}', '', content)
    content = re.sub(r'~\\cite\{buzzard-xena\}', '', content)
    content = re.sub(r'~\\cite\{massot-blueprints\}', '', content)
    content = re.sub(r'\\cite\{demoura-lean4\}', '', content)
    content = re.sub(r'\\cite\{mathlib\}', '', content)
    content = re.sub(r'\\cite\{mathlib2020\}', '', content)
    content = re.sub(r'\\cite\{buzzard-xena\}', '', content)
    content = re.sub(r'\\cite\{massot-blueprints\}', '', content)

    # Clean up specific sentences that are entirely about Lean community
    community_sentence = r"The community-driven formalization movement --- Buzzard's Xena Project, Massot's formalization blueprints, the ongoing formalization of \\emph\{Fermat's Last Theorem\} --- provides the methodological template for our verification architecture\."
    content = content.replace(community_sentence, "The open-source numerical verification movement provides the methodological template for our architecture.")
    
    # Catch any remaining "Lean" mentions that might be capitalizing "Lean" as the language
    # Be careful not to replace "clean" or "glean".
    content = re.sub(r'\bLean\b(?!\s*Lakes)', 'Python', content)
    
    return content

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        if 'build' in root:
            continue
        for file in files:
            if file.endswith('.tex'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = replace_lean_refs(content)
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {path}")

if __name__ == "__main__":
    process_directory("/home/phrxmaz/Documents/CyberAlchemy/papers")
    print("Done eradication.")
