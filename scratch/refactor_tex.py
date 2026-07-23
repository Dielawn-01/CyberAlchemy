import os

path = '/home/phrxmaz/Documents/CyberAlchemy/papers/ARC_Prize_2026_Plazmik_Omnibus.tex'
with open(path, 'r') as f:
    content = f.read()

content = content.replace('\\infty$-Modal Topos', '\\infty$-Modal Category')
content = content.replace('\\infty-Modal Topos', '\\infty-Modal Category')
content = content.replace('Topos', 'Category')
content = content.replace('topos', 'category')
content = content.replace('Adelic', '$S$-Arithmetic')
content = content.replace('adelic', '$S$-arithmetic')

with open(path, 'w') as f:
    f.write(content)

print("Refactored ARC Prize paper.")
