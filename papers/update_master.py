import os

filepath = "/home/phrxmaz/Documents/InfoPhys/LaRueResearch/papers/01_Principia_Psychedelia_Master.tex"
with open(filepath, "r") as f:
    content = f.read()

old_part = r"""\chapter[Ambrosia Protocol]{Bionetic Ambrosia Protocol}
\input{13_Bionetic_Ambrosia_Protocol}"""

new_part = r"""\chapter[Ambrosia Protocol]{Bionetic Ambrosia Protocol}
\input{13_Bionetic_Ambrosia_Protocol}

\chapter[Fusion Cybernetics]{Fusion Plasma Cybernetics and Halting Topology}
\input{18_Fusion_Plasma_Cybernetics}"""

content = content.replace(old_part, new_part)

with open(filepath, "w") as f:
    f.write(content)

print("Master tex updated.")
