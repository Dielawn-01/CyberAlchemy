"""
The Prime Harp: Three-Flower Golden Tetrahedron Visualization

Three nested Flower of Life structures representing the golden tetrahedron
{229, 181, 139}:

  OUTER (F₂₂₉): 19 circles in hexagonal packing (1+6+12)
    → 3-decomposable, 3 cosets × 19 = 57 orbit
    → CMY coloring per coset (Cyan, Magenta, Yellow)

  MIDDLE (F₁₈₁): 15 circles (1+6+8 adapted packing)
    → 3-decomposable, 3 cosets × 15 = 45 orbit
    → RGB coloring per coset (Red, Green, Blue)

  INNER (F₁₃₉): 23 nodes on a single ring
    → INDECOMPOSABLE (prime orbit), no sub-circles
    → Monochromatic white — indivisible cycle

Cross-field bridges at the cube root embedding: 229 ≡ ω₁₈₁ = 48

Authors: LaRue (Theory) (Implementation)
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import LineCollection

# ═══════════════════════════════════════════════════════
# GOLDEN TETRAHEDRON CONSTANTS
# ═══════════════════════════════════════════════════════

# Field 1: F₂₂₉
P1, PHI_229, PHIBAR_229 = 229, 148, 82
ORD_229 = 57; COSET_229 = 19
OMEGA_229 = pow(PHIBAR_229, COSET_229, P1)

# Field 2: F₁₈₁
P2, PHI_181, PHIBAR_181 = 181, 168, 14
ORD_181 = 45; COSET_181 = 15
OMEGA_181 = pow(PHIBAR_181, COSET_181, P2)

# Field 3: F₁₃₉
P3, PHI_139, PHIBAR_139 = 139, 76, 64
ORD_139 = 23  # PRIME — indecomposable

# Verify
for p, phi, bar in [(P1,PHI_229,PHIBAR_229),(P2,PHI_181,PHIBAR_181),(P3,PHI_139,PHIBAR_139)]:
    assert (phi + bar) % p == 1
    assert (phi * bar) % p == p - 1

assert P1 % P2 == OMEGA_181, "229 ≡ ω₁₈₁ cross-field"
print("All golden tetrahedron assertions passed. ✓")

# ═══════════════════════════════════════════════════════
# FLOWER OF LIFE GEOMETRY
# ═══════════════════════════════════════════════════════

def flower_centers_19(r, offset=(0,0)):
    """19-circle Flower of Life: 1 + 6 + 12 hexagonal packing."""
    cx, cy = offset
    centers = [(cx, cy)]
    # Ring 1: 6 circles
    for i in range(6):
        angle = i * (math.pi / 3)
        centers.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    # Ring 2: 12 circles
    for i in range(12):
        angle = i * (math.pi / 6)
        dist = 2 * r if i % 2 == 0 else math.sqrt(3) * r
        centers.append((cx + dist * math.cos(angle), cy + dist * math.sin(angle)))
    return centers

def flower_centers_15(r, offset=(0,0)):
    """15-node arrangement: 1 + 6 + 8 adapted packing."""
    cx, cy = offset
    centers = [(cx, cy)]
    # Ring 1: 6
    for i in range(6):
        angle = i * (math.pi / 3) + math.pi / 6  # 30° offset from outer
        centers.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    # Ring 2: 8 (not full 12 — reflecting the smaller coset)
    for i in range(8):
        angle = i * (math.pi / 4)
        centers.append((cx + 1.8 * r * math.cos(angle), cy + 1.8 * r * math.sin(angle)))
    return centers

def ring_nodes_23(r, offset=(0,0)):
    """23 nodes on a single ring — indecomposable, no sub-structure."""
    cx, cy = offset
    return [(cx + r * math.cos(2 * math.pi * i / 23),
             cy + r * math.sin(2 * math.pi * i / 23)) for i in range(23)]


# ═══════════════════════════════════════════════════════
# ORBIT TRAJECTORIES
# ═══════════════════════════════════════════════════════

def compute_orbit(base, prime, length):
    """Compute the golden orbit φ̄^n mod p for n=0..length-1."""
    return [pow(base, n, prime) for n in range(length)]


# ═══════════════════════════════════════════════════════
# MAIN VISUALIZATION
# ═══════════════════════════════════════════════════════

fig, ax = plt.subplots(figsize=(14, 14), facecolor='black')
ax.set_facecolor('black')
ax.set_aspect('equal')

# Radii for the three flowers
R_OUTER = 1.0   # F₂₂₉ outer flower
R_MIDDLE = 0.55  # F₁₈₁ middle flower
R_INNER = 1.6    # F₁₃₉ inner ring radius

# --- OUTER FLOWER: F₂₂₉ (19 circles) ---
outer_centers = flower_centers_19(R_OUTER)
for center in outer_centers:
    circle = Circle(center, R_OUTER, fill=False, edgecolor='#1a1a2e', linewidth=1.2, alpha=0.4)
    ax.add_patch(circle)

# Compute F₂₂₉ orbit
orbit_229 = compute_orbit(PHIBAR_229, P1, ORD_229)

# Color: 3 cosets × 19 → CMY
coset_colors_229 = ['#00FFFF', '#FF00FF', '#FFFF00']  # Cyan, Magenta, Yellow

for n in range(ORD_229):
    val = orbit_229[n]
    c_idx = n % COSET_229  # Which circle
    coset = n // COSET_229  # Which coset (0,1,2)
    color = coset_colors_229[coset]
    
    cx, cy = outer_centers[c_idx]
    node_angle = (val / P1) * 2 * math.pi
    nx = cx + R_OUTER * 0.8 * math.cos(node_angle)
    ny = cy + R_OUTER * 0.8 * math.sin(node_angle)
    
    ax.plot(nx, ny, 'o', markersize=3.5, color=color, alpha=0.9,
            markeredgecolor='white', markeredgewidth=0.3)

# Connect orbit trajectory
for n in range(ORD_229 - 1):
    v1, v2 = orbit_229[n], orbit_229[n+1]
    c1, c2 = n % COSET_229, (n+1) % COSET_229
    cx1, cy1 = outer_centers[c1]
    cx2, cy2 = outer_centers[c2]
    a1 = (v1/P1) * 2*math.pi
    a2 = (v2/P1) * 2*math.pi
    x1 = cx1 + R_OUTER*0.8*math.cos(a1)
    y1 = cy1 + R_OUTER*0.8*math.sin(a1)
    x2 = cx2 + R_OUTER*0.8*math.cos(a2)
    y2 = cy2 + R_OUTER*0.8*math.sin(a2)
    color = coset_colors_229[n // COSET_229]
    ax.plot([x1,x2], [y1,y2], color=color, linewidth=0.3, alpha=0.25)

# --- MIDDLE FLOWER: F₁₈₁ (15 circles) ---
middle_centers = flower_centers_15(R_MIDDLE)
for center in middle_centers:
    circle = Circle(center, R_MIDDLE, fill=False, edgecolor='#162447', linewidth=1.0, alpha=0.35)
    ax.add_patch(circle)

orbit_181 = compute_orbit(PHIBAR_181, P2, ORD_181)
coset_colors_181 = ['#FF4444', '#44FF44', '#4488FF']  # Red, Green, Blue

for n in range(ORD_181):
    val = orbit_181[n]
    c_idx = n % COSET_181
    coset = n // COSET_181
    color = coset_colors_181[coset]
    
    cx, cy = middle_centers[c_idx]
    node_angle = (val / P2) * 2 * math.pi
    nx = cx + R_MIDDLE * 0.75 * math.cos(node_angle)
    ny = cy + R_MIDDLE * 0.75 * math.sin(node_angle)
    
    ax.plot(nx, ny, 'o', markersize=2.5, color=color, alpha=0.85,
            markeredgecolor='white', markeredgewidth=0.2)

for n in range(ORD_181 - 1):
    v1, v2 = orbit_181[n], orbit_181[n+1]
    c1, c2 = n % COSET_181, (n+1) % COSET_181
    cx1, cy1 = middle_centers[c1]
    cx2, cy2 = middle_centers[c2]
    a1 = (v1/P2) * 2*math.pi
    a2 = (v2/P2) * 2*math.pi
    x1 = cx1 + R_MIDDLE*0.75*math.cos(a1)
    y1 = cy1 + R_MIDDLE*0.75*math.sin(a1)
    x2 = cx2 + R_MIDDLE*0.75*math.cos(a2)
    y2 = cy2 + R_MIDDLE*0.75*math.sin(a2)
    color = coset_colors_181[n // COSET_181]
    ax.plot([x1,x2], [y1,y2], color=color, linewidth=0.25, alpha=0.2)

# --- INNER RING: F₁₃₉ (23 nodes, indecomposable) ---
inner_nodes = ring_nodes_23(R_INNER)
orbit_139 = compute_orbit(PHIBAR_139, P3, ORD_139)

for n in range(ORD_139):
    val = orbit_139[n]
    nx, ny = inner_nodes[n]
    # Brightness varies with orbit value — single color (white/gold)
    brightness = 0.4 + 0.6 * (val / P3)
    ax.plot(nx, ny, 'o', markersize=5, color=(1, 0.95, 0.8, brightness),
            markeredgecolor='#FFD700', markeredgewidth=0.8)

# Connect the indecomposable ring
for n in range(ORD_139):
    n2 = (n + 1) % ORD_139
    x1, y1 = inner_nodes[n]
    x2, y2 = inner_nodes[n2]
    ax.plot([x1,x2], [y1,y2], color='#FFD700', linewidth=0.8, alpha=0.4)

# --- CROSS-FIELD BRIDGES ---
# 229 ≡ ω₁₈₁ = 48: link outer flower circles to middle flower circles
# at the cube root embedding points
bridge_count = 0
for i in range(min(COSET_229, COSET_181)):
    # Map circle i of outer to circle i of middle
    ox, oy = outer_centers[i]
    mx, my = middle_centers[i]
    ax.plot([ox, mx], [oy, my], color='#FF6600', linewidth=0.6, alpha=0.3,
            linestyle='--')
    bridge_count += 1

# Link the projection vertex ring to the anchor flower center
ax.plot([0, 0], [0, 0], 'o', markersize=8, color='#FF6600', alpha=0.5)

# Labels
ax.text(0, 3.3, 'F₂₂₉: 19-CIRCLE FLOWER (3×19=57)', 
        ha='center', va='center', color='#00FFFF', fontsize=10, fontweight='bold',
        fontfamily='monospace')
ax.text(0, 2.8, '3-decomposable · CMY cosets', 
        ha='center', va='center', color='#888888', fontsize=8,
        fontfamily='monospace')
ax.text(0, -2.6, 'F₁₈₁: 15-CIRCLE FLOWER (3×15=45)', 
        ha='center', va='center', color='#FF4444', fontsize=9, fontweight='bold',
        fontfamily='monospace')
ax.text(0, -2.95, '3-decomposable · RGB cosets', 
        ha='center', va='center', color='#888888', fontsize=8,
        fontfamily='monospace')
ax.text(2.2, 0, 'F₁₃₉: 23-NODE RING', 
        ha='left', va='center', color='#FFD700', fontsize=9, fontweight='bold',
        fontfamily='monospace')
ax.text(2.2, -0.3, 'INDECOMPOSABLE', 
        ha='left', va='center', color='#888888', fontsize=8,
        fontfamily='monospace')

# Title
ax.text(0, 4.0, 'THE PRIME HARP', 
        ha='center', va='center', color='white', fontsize=16, fontweight='bold',
        fontfamily='monospace')
ax.text(0, 3.65, 'Golden Tetrahedron {229, 181, 139}', 
        ha='center', va='center', color='#666666', fontsize=10,
        fontfamily='monospace')

plt.xlim(-4.5, 4.5)
plt.ylim(-3.5, 4.5)
plt.axis('off')
plt.tight_layout()

out_path = os.path.join(os.path.dirname(__file__), 'chromatic_fractal_exact.png')
plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='black')
print(f"Prime Harp visualization saved to {out_path}")
