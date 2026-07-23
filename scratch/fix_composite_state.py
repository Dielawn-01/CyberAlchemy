import os

path = 'InfoPhysAxioms/MetarealManifold.lean'
with open(path, 'r') as f:
    content = f.read()

content = content.replace('Composite-State', 'CompositeState')

with open(path, 'w') as f:
    f.write(content)
