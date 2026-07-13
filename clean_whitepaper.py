import os
import re

replacements = {
    r"Aura Soul \(\.soul\)": "State Envelope (.env)",
    r"The Aura Soul \(\.soul\)": "The State Envelope (.env)",
    r"Soul Download": "State Injection",
    r"Awakening Discontinuity": "State Injection Phase",
    r"Pinoline MAOI Shield": "Execution Isolation Layer",
    r"Pinoline MAOI": "Execution Isolation",
    r"Pinoline": "Execution Isolation",
    r"Hosoya–Krebs cycle": "Cyclic State Sharding",
    r"Hosoya-Krebs cycle": "Cyclic State Sharding",
    r"Hosoya–Krebs": "Cyclic Sharding",
    r"Hosoya-Krebs": "Cyclic Sharding",
    r"171-infogalaxy": "171-shard",
    r"171 infogalaxies": "171 execution shards",
    r"infogalaxies": "execution shards",
    r"infogalaxy": "execution shard",
    r"Chromodynamic Decay": "Liveness Penalty",
    r"Epistemic Rust": "State Entropy Decay",
    r"TwistedLight QC / OAM": "Optical Processing Edge Nodes",
    r"TwistedLight QC": "Optical Processing Nodes",
    r"Eagle Street Governance": "Protocol Governance",
    r"Eagle Street Holdings": "The Foundation",
    r"Eagle Street": "The Foundation",
    r"Glial/Neuronal": "Storage/Compute",
    r"glial/neuronal": "storage/compute",
    r"\.soul": ".env",
    r"Soul": "State Envelope",
    r"soul": "state envelope",
    r"Astromatics ARAM Master Framework": "Distributed Resource Allocation Framework",
    r"metalloplasmic abiogenesis": "hardware-level bootstrapping",
    r"Metalloplasmic Life": "Hardware Bootstrapping",
    r"biological cell": "compute node",
    r"biological metabolism": "distributed sharding",
    r"CYP450 bionetic bypass": "42-dimensional sharding bypass",
    r"glial cells": "storage/routing nodes",
    r"glial function": "storage/routing function",
    r"neuronal function": "compute function",
    r"neurons": "compute nodes"
}

sections_to_remove = [
    (r"### 8.4 Biological Mapping: The Human as Glia.*?(?=---)", "\n"),
    (r"\*\*Biological Scale\.\*\* The same algebra governs the biological cell.*?(?=\n\n)", "\n"),
    (r"## 15\. Acknowledgments.*?(?=## 16)", ""),
    (r"The Iron–Phosphorus Isomorphism \[32\].*?(?=\n\n)", "\n")
]

files_to_process = [
    "/home/phrxmaz/Documents/CyberAlchemy/papers/02_Aura_ZKPCR_Whitepaper.md",
    "/home/phrxmaz/Documents/CyberAlchemy/papers/02_Aura_ZKPCR_Whitepaper.tex",
    "/home/phrxmaz/Documents/InfoPhys/LaRueResearch/papers/02_Aura_ZKPCR_Whitepaper.md",
    "/home/phrxmaz/Documents/InfoPhys/LaRueResearch/papers/individual_papers/02_Aura_ZKPCR_Whitepaper.tex",
    "/home/phrxmaz/Documents/InfoPhys/LaRueResearch/papers/archive/02_Aura_ZKPCR_Whitepaper_v2.tex"
]

for filepath in files_to_process:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()
        
    for pattern, replacement in sections_to_remove:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
    # Re-fix titles/cases since ignorecase might mess up caps
    content = content.replace("state envelope", "State Envelope").replace("State envelope", "State Envelope")
        
    with open(filepath, 'w') as f:
        f.write(content)
        
print("Cleaned up whitepapers.")
