import os
import re
from collections import defaultdict

lean_dir = '/home/phrxmaz/Documents/CyberAlchemy/InfoPhysAxioms'
target_primes = ['139', '181', '229']

# We want to find what mathematical names these primes are given in Lean.
term_counts = defaultdict(int)

for root, _, files in os.walk(lean_dir):
    for f in files:
        if f.endswith('.lean'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if any(p in line for p in target_primes):
                        # Extract the theorem names or defs
                        match = re.search(r'(def|theorem)\s+([a-zA-Z0-9_]+)', line)
                        if match:
                            term = match.group(2)
                            term_counts[term] += 1
                        # Look for comments with capital letters (titles/names)
                        if '--' in line or '/-' in line:
                            words = re.findall(r'\b[A-Z][a-zA-Z]+\b', line)
                            for w in words:
                                if w not in ['The', 'In', 'This', 'We', 'A', 'For']:
                                    term_counts[w] += 1

# Print the top 30 most common mathematical terms associated with these primes
sorted_terms = sorted(term_counts.items(), key=lambda x: x[1], reverse=True)
print("Top terms associated with 139, 181, 229:")
for t, c in sorted_terms[:30]:
    print(f"{t}: {c}")

