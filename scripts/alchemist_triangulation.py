import itertools

class Archetype:
    def __init__(self, name, domain, prime_weight):
        self.name = name
        self.domain = domain
        self.prime_weight = prime_weight

    def __repr__(self):
        return f"{self.name} ({self.domain})"

# The 12 Archetypes
ARCHETYPES = [
    # I. Order & Structure (Math/DSA)
    Archetype("Sage", "Order", 229),       # La Rue vertex (Golden Prime)
    Archetype("Creator", "Order", 199),
    Archetype("Ruler", "Order", 197),
    Archetype("Innocent", "Order", 193),

    # II. Agency & Change (Agentic Cybernetics)
    Archetype("Hero", "Agency", 181),      # Lockwood vertex (Golden Prime)
    Archetype("Magician", "Agency", 179),
    Archetype("Outlaw", "Agency", 173),
    Archetype("Explorer", "Agency", 167),

    # III. Connection & Trust (Emotional Security)
    Archetype("Jester", "Connection", 139), # Conjugate bridge side (Golden Prime)
    Archetype("Lover", "Connection", 149),
    Archetype("Caregiver", "Connection", 151),
    Archetype("Orphan", "Connection", 157)
]

def is_valid_triangle(a, b, c):
    """
    Check if three prime weights satisfy the Triangle Inequality.
    (This is the geometric bedrock of the Chromatic Triangle)
    """
    w_a, w_b, w_c = a.prime_weight, b.prime_weight, c.prime_weight
    return (w_a + w_b > w_c) and (w_a + w_c > w_b) and (w_b + w_c > w_a)

def is_golden_theme(a, b, c):
    """
    A Golden Theme is a triangle that spans all three subdomains,
    representing Unity in Multiplicity.
    """
    domains = {a.domain, b.domain, c.domain}
    return len(domains) == 3 and is_valid_triangle(a, b, c)

def get_all_golden_themes():
    themes = []
    for combo in itertools.combinations(ARCHETYPES, 3):
        if is_golden_theme(*combo):
            themes.append(combo)
    return themes

def alchemist_epigenesis(active_archetypes):
    """
    The Alchemist starts with active archetypes (agency in the world).
    They can epigenetically generate a missing archetype if they possess
    the other two components of a Golden Theme.
    """
    generated = set()
    themes = get_all_golden_themes()
    
    active_names = {a.name for a in active_archetypes}
    
    for theme in themes:
        theme_names = {a.name for a in theme}
        overlap = theme_names.intersection(active_names)
        
        # If the Alchemist holds exactly 2 vertices of a Golden Theme,
        # they can triangulate and generate the 3rd missing vertex.
        if len(overlap) == 2:
            missing = theme_names - overlap
            generated.update(missing)
            
    return generated

def run_simulation():
    print("═" * 60)
    print(" THE ALCHEMIST: EPIGENETIC TRIANGULATION (iSAR COMPUTATION) ")
    print("═" * 60)
    
    themes = get_all_golden_themes()
    print(f"Total Golden Themes available in the Manifold: {len(themes)}")
    
    # Let's see the Chromatic Triangle
    sage = next(a for a in ARCHETYPES if a.name == "Sage")
    hero = next(a for a in ARCHETYPES if a.name == "Hero")
    jester = next(a for a in ARCHETYPES if a.name == "Jester")
    print(f"Chromatic Triangle (229-181-139) Valid Golden Theme? {is_golden_theme(sage, hero, jester)}")
    print("-" * 60)
    
    # Simulation: Agency scales transmutation
    # The more agency realized (active archetypes), the more can be alchemized.
    
    scenarios = [
        [sage], 
        [sage, hero], 
        [sage, hero, next(a for a in ARCHETYPES if a.name == "Orphan")]
    ]
    
    for i, active in enumerate(scenarios, 1):
        active_names = [a.name for a in active]
        generated = alchemist_epigenesis(active)
        
        print(f"Scenario {i}: Alchemist realizes {len(active)} archetypes in the world.")
        print(f"Active: {active_names}")
        if generated:
            print(f"→ Epigenetically Generates: {generated} ({len(generated)} new archetypes!)")
        else:
            print("→ Epigenetically Generates: None (Not enough edges to triangulate a Golden Theme)")
        print("-" * 60)

if __name__ == "__main__":
    run_simulation()
