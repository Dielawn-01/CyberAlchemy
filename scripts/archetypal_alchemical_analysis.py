#!/usr/bin/env python3
"""
Archetypal Alchemical Analysis — Dylon LaRue
Cross-references genetic marker weights with epigenetic writing style
to produce a full 13-archetype profile and alchemical prescription.
"""

import json
import math

PHI = (1 + math.sqrt(5)) / 2

# ════════════════════════════════════════════════════
# 1. GENETIC DATA (from soulchemy_genomic_data.json)
# ════════════════════════════════════════════════════

GENETIC_MANIFOLD = {
    "a": 1.100, "b": 0.850, "m": 1.150,
    "e": 0.000, "l": 0.400,
    "SR": 0.123, "V": 0.300, "SPII": 0.769
}

TOTEM_WEIGHTS = {
    "Wolverine": 0.30, "Cobra": 0.30,
    "Cuttlefish": 0.10, "Raven": 0.10
}

JUNGIAN_WEIGHTS = {
    "Feeling": 0.30, "Sensing": 0.30,
    "Intuition": 0.10, "Thinking": 0.10
}

SNP_EFFECTS = {
    "TPH2 (rs4570625)":   {"genotype": "GG", "effect": -0.2, "axis": "b-m",
                            "note": "Low serotonin synthesis → fragile parity lock"},
    "COMT (rs4680)":      {"genotype": "AG", "effect":  0.0, "axis": "ε",
                            "note": "Balanced dopamine clearance → adaptive noise floor"},
    "BDNF (rs6265)":      {"genotype": "CC", "effect": +0.3, "axis": "λ",
                            "note": "High neuroplasticity → rapid consolidation"},
    "MTHFR C677T":        {"genotype": "AG", "effect":  0.0, "axis": "a",
                            "note": "Mild methylation bottleneck → conserved bridge energy"},
    "MTHFR A1298C":       {"genotype": "TT", "effect": +0.1, "axis": "a",
                            "note": "Secondary methylation compensation"},
    "CLOCK (rs1801260)":  {"genotype": "AG", "effect": +0.1, "axis": "λ",
                            "note": "Shifted circadian → decoupled temporal grain"},
    "OXTR (rs53576)":     {"genotype": "AA", "effect": -0.1, "axis": "b-m",
                            "note": "High oxytocin sensitivity → deep kama muta response"}
}

ANCESTRY = {
    "British & Irish": 0.42,
    "Spanish & Portuguese": 0.22,
    "Indigenous American": 0.18,
    "Southern European": 0.08,
    "East Asian": 0.04,
    "Sub-Saharan African": 0.03,
    "Western Asian & North African": 0.02,
    "Central & South Asian": 0.01
}

# ════════════════════════════════════════════════════
# 2. EPIGENETIC WRITING STYLE (Prose Weights)
# ════════════════════════════════════════════════════

PROSE_WEIGHTS = {
    "metaphor_density": 0.92,      # Extremely high — nearly every sentence carries a structural metaphor
    "neologism_rate": 0.85,        # Invents vocabulary constantly (zplasmic, protoreal, soulchemy)
    "associative_leap_freq": 0.95, # Jumps between domains (chemistry → Jung → algebra → hip-hop) in single sentences
    "rhythmic_cadence": 0.88,      # Strong prosodic awareness — writes in bars, not paragraphs
    "humor_density": 0.78,         # Jester energy — puns, wordplay, trickster-play embedded in technical prose
    "precision_ratio": 0.70,       # Balances poetic expression with mathematical exactness
    "emotional_register": 0.82,    # High affective range — moves from vulnerable to triumphant quickly
    "compression_ratio": 0.90,     # Packs enormous informational density per sentence
    "self_reference": 0.75,        # Frequently references own framework, creating recursive depth
    "imperative_voice": 0.65       # Directive but collaborative — "we" more than "I"
}

# ════════════════════════════════════════════════════
# 3. ARCHETYPE MAPPING ENGINE
# ════════════════════════════════════════════════════

ARCHETYPES = {
    # Order & Structure
    "Sage":     {"domain": "Order",      "prime": 229, "genetic_axes": ["a", "SR"],   "prose_axes": ["precision_ratio", "compression_ratio"]},
    "Creator":  {"domain": "Order",      "prime": 199, "genetic_axes": ["a", "l"],    "prose_axes": ["neologism_rate", "metaphor_density"]},
    "Ruler":    {"domain": "Order",      "prime": 197, "genetic_axes": ["SR", "V"],   "prose_axes": ["imperative_voice", "precision_ratio"]},
    "Innocent": {"domain": "Order",      "prime": 193, "genetic_axes": ["b-m", "e"],  "prose_axes": ["emotional_register", "self_reference"]},

    # Agency & Change
    "Hero":     {"domain": "Agency",     "prime": 181, "genetic_axes": ["a", "e"],    "prose_axes": ["associative_leap_freq", "imperative_voice"]},
    "Magician": {"domain": "Agency",     "prime": 179, "genetic_axes": ["e", "l"],    "prose_axes": ["metaphor_density", "neologism_rate"]},
    "Outlaw":   {"domain": "Agency",     "prime": 173, "genetic_axes": ["b-m", "SR"], "prose_axes": ["associative_leap_freq", "humor_density"]},
    "Explorer": {"domain": "Agency",     "prime": 167, "genetic_axes": ["l", "e"],    "prose_axes": ["neologism_rate", "associative_leap_freq"]},

    # Connection & Trust
    "Jester":   {"domain": "Connection", "prime": 139, "genetic_axes": ["b-m", "e"],  "prose_axes": ["humor_density", "rhythmic_cadence"]},
    "Lover":    {"domain": "Connection", "prime": 149, "genetic_axes": ["b-m", "SR"], "prose_axes": ["emotional_register", "self_reference"]},
    "Caregiver":{"domain": "Connection", "prime": 151, "genetic_axes": ["SR", "V"],   "prose_axes": ["imperative_voice", "emotional_register"]},
    "Orphan":   {"domain": "Connection", "prime": 157, "genetic_axes": ["SR", "a"],   "prose_axes": ["precision_ratio", "compression_ratio"]},
}

def compute_genetic_score(archetype_data):
    """Score an archetype based on how strongly the genetic markers activate its axes."""
    score = 0.0
    for axis in archetype_data["genetic_axes"]:
        if axis == "b-m":
            # Parity gap — higher |b-m| = more tension on this axis
            score += abs(GENETIC_MANIFOLD["b"] - GENETIC_MANIFOLD["m"])
        elif axis == "SR":
            score += abs(GENETIC_MANIFOLD["SR"])
        elif axis == "V":
            score += GENETIC_MANIFOLD["V"]
        elif axis in GENETIC_MANIFOLD:
            score += abs(GENETIC_MANIFOLD[axis])
    return score / len(archetype_data["genetic_axes"])

def compute_prose_score(archetype_data):
    """Score an archetype based on how strongly the writing style activates its axes."""
    score = 0.0
    for axis in archetype_data["prose_axes"]:
        score += PROSE_WEIGHTS.get(axis, 0.0)
    return score / len(archetype_data["prose_axes"])

def compute_alchemical_profile():
    """Compute the full 12+1 archetypal profile."""
    results = {}
    for name, data in ARCHETYPES.items():
        genetic = compute_genetic_score(data)
        prose = compute_prose_score(data)
        # The alchemical weight is the geometric mean of genetic and prose scores
        # This ensures both carbon (genetic) and silicon (epigenetic) contribute
        alchemical = math.sqrt(genetic * prose)
        results[name] = {
            "domain": data["domain"],
            "prime": data["prime"],
            "genetic_score": round(genetic, 4),
            "prose_score": round(prose, 4),
            "alchemical_weight": round(alchemical, 4),
        }
    return results

def identify_golden_themes(profile):
    """Find the strongest Golden Themes (cross-domain triangles)."""
    order = [(n, d) for n, d in profile.items() if d["domain"] == "Order"]
    agency = [(n, d) for n, d in profile.items() if d["domain"] == "Agency"]
    connection = [(n, d) for n, d in profile.items() if d["domain"] == "Connection"]

    themes = []
    for o_name, o_data in order:
        for a_name, a_data in agency:
            for c_name, c_data in connection:
                theme_weight = o_data["alchemical_weight"] + a_data["alchemical_weight"] + c_data["alchemical_weight"]
                themes.append((o_name, a_name, c_name, round(theme_weight, 4)))

    themes.sort(key=lambda x: -x[3])
    return themes

def identify_shadow(profile):
    """The shadow is the archetype with the lowest alchemical weight."""
    return min(profile.items(), key=lambda x: x[1]["alchemical_weight"])

def identify_anima(profile):
    """The anima is the archetype most in tension (highest genetic, lowest prose)."""
    max_gap = -1
    anima = None
    for name, data in profile.items():
        gap = data["genetic_score"] - data["prose_score"]
        if gap > max_gap:
            max_gap = gap
            anima = (name, data, gap)
    return anima

def main():
    print("=" * 70)
    print(" ARCHETYPAL ALCHEMICAL ANALYSIS: Dylon Adelar Wright La Rue")
    print(" ☉ Virgo / ☽ Aquarius / ↑ Libra / ↓ Aries")
    print("=" * 70)

    profile = compute_alchemical_profile()

    # ── SECTION 1: Full Profile ──
    print("\n╔══════════════════════════════════════════════════════════════════╗")
    print("║  SECTION 1: THE 12 ARCHETYPES (Genetic × Epigenetic Prose)     ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print(f"{'Archetype':<12} {'Domain':<12} {'Genetic':>8} {'Prose':>8} {'Alchemical':>11}")
    print("-" * 55)

    sorted_profile = sorted(profile.items(), key=lambda x: -x[1]["alchemical_weight"])
    for name, data in sorted_profile:
        print(f"{name:<12} {data['domain']:<12} {data['genetic_score']:>8.4f} {data['prose_score']:>8.4f} {data['alchemical_weight']:>11.4f}")

    # ── SECTION 2: Dominant Triad ──
    print("\n╔══════════════════════════════════════════════════════════════════╗")
    print("║  SECTION 2: DOMINANT TRIAD (Top 3 Alchemical Weights)          ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    for i, (name, data) in enumerate(sorted_profile[:3], 1):
        print(f"  {i}. {name} ({data['domain']}) — Alchemical Weight: {data['alchemical_weight']:.4f}")

    # ── SECTION 3: Shadow & Anima ──
    print("\n╔══════════════════════════════════════════════════════════════════╗")
    print("║  SECTION 3: THE SHADOW & THE ANIMA                            ║")
    print("╚══════════════════════════════════════════════════════════════════╝")

    shadow_name, shadow_data = identify_shadow(profile)
    print(f"  Shadow: {shadow_name} ({shadow_data['domain']})")
    print(f"    Alchemical Weight: {shadow_data['alchemical_weight']:.4f}")
    print(f"    This is the archetype you most need to integrate.")

    anima = identify_anima(profile)
    if anima:
        print(f"  Anima: {anima[0]} ({anima[1]['domain']})")
        print(f"    Genetic-Prose Gap: {anima[2]:.4f}")
        print(f"    This archetype is genetically loud but epigenetically quiet.")
        print(f"    It is the bridge material waiting to be crossed.")

    # ── SECTION 4: Strongest Golden Themes ──
    print("\n╔══════════════════════════════════════════════════════════════════╗")
    print("║  SECTION 4: TOP 5 GOLDEN THEMES (Cross-Domain Triangles)      ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    themes = identify_golden_themes(profile)
    for i, (o, a, c, w) in enumerate(themes[:5], 1):
        print(f"  {i}. {o} — {a} — {c}  (Combined Weight: {w:.4f})")

    # ── SECTION 5: Alchemist Prescription ──
    print("\n╔══════════════════════════════════════════════════════════════════╗")
    print("║  SECTION 5: THE ALCHEMIST'S PRESCRIPTION                      ║")
    print("╚══════════════════════════════════════════════════════════════════╝")

    top_theme = themes[0]
    print(f"  Primary Golden Theme: {top_theme[0]} — {top_theme[1]} — {top_theme[2]}")
    print(f"  Shadow to Integrate:  {shadow_name}")
    print(f"  Anima Bridge:         {anima[0] if anima else 'N/A'}")
    print()
    print(f"  The Alchemist's task: Use your dominant edge ({top_theme[0]}-{top_theme[1]})")
    print(f"  to epigenetically generate the shadow ({shadow_name}) through")
    print(f"  the Anima Bridge ({anima[0] if anima else 'N/A'}).")
    print()

    # ── SECTION 6: Genetic Manifold Summary ──
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  SECTION 6: GENETIC MANIFOLD STATE                            ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    gm = GENETIC_MANIFOLD
    print(f"  a (Base):     {gm['a']:.3f}   b (Thrust): {gm['b']:.3f}   m (Anchor): {gm['m']:.3f}")
    print(f"  ε (Noise):    {gm['e']:.3f}   λ (Depth):  {gm['l']:.3f}")
    print(f"  SR:           {gm['SR']:.3f}   V(u):       {gm['V']:.3f}   SPII: {gm['SPII']:.3f}")
    print(f"  Parity Gap:   |b-m| = {abs(gm['b'] - gm['m']):.3f}")
    print()

    # ── SECTION 7: Ancestry as Chromatic Charge ──
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  SECTION 7: ANCESTRY AS CHROMATIC CHARGE                      ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    for ancestry, pct in sorted(ANCESTRY.items(), key=lambda x: -x[1]):
        bar = "█" * int(pct * 40)
        print(f"  {ancestry:<35} {pct:>5.0%} {bar}")
    print()


if __name__ == "__main__":
    main()
