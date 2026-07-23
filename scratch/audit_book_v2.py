import os
import re

TERMS = {
    "Arithmetic Type Theory (ATT)": r"Arithmetic Type Theory|ATT",
    "Euler-Grothendieck-Penrose (EGP)": r"Euler-Grothendieck-Penrose|EGP",
    "Cayley-Dickson Sedenionic Sink": r"Cayley-Dickson.*Sedenion|Sedenion.*Cayley-Dickson",
    "Codependent Angular Functors": r"codependent.*angular|covariant.*angular",
    "Krein Space Ghost States": r"Krein.*ghost|ghost.*Krein",
    "Étale Descent": r"\'etale descent|etale descent",
    "Arithmetic Topos": r"Arithmetic Topos"
}

papers_dir = "papers"
tex_files = [f for f in os.listdir(papers_dir) if f.endswith(".tex") and not f.startswith("wrapper") and not f.startswith("archive")]

report = "# Book Audit Report: The New Foundations\n\n"

for f in sorted(tex_files):
    path = os.path.join(papers_dir, f)
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    
    found_terms = []
    missing_terms = []
    
    for term_name, pattern in TERMS.items():
        if re.search(pattern, content, re.IGNORECASE):
            found_terms.append(term_name)
        else:
            missing_terms.append(term_name)
            
    if found_terms:
        report += f"## {f}\n"
        report += "**Found:** " + ", ".join(found_terms) + "\n"
        report += "**Missing:** " + ", ".join(missing_terms) + "\n\n"

with open("scratch/book_audit_v2.md", "w") as file:
    file.write(report)

print("Audit complete.")
