import numpy as np

# Constants from the Metareal / InfoPhys Framework
P = 229
UPSILON_LIMIT = 45 / np.pi  # Casimir torque limit (~14.32)
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
DELTA_NAVIER_STOKES = 1     # Biological fluids (ds = 2)
DELTA_PAQFT = 2             # Required topological mass gap (ds = 3/2)

def order_in_Fp(Z, p=229):
    """Calculate the multiplicative order of Z in F_p^*"""
    Z = Z % p
    if Z == 0:
        return 0
    for d in range(1, p):
        if pow(Z, d, p) == 1:
            return d
    return p - 1

# Atomic numbers of relevant elements
elements = {
    'Vanadium (Amavadin)': 23,
    'Silicon (Scaffold)': 14,
    'Gold (Au-Ag-Bi)': 79,
    'Carbon (Organic Base)': 6,
    'Nitrogen (DNA/Proteins)': 7,
    'Oxygen (Polar Matrix)': 8,
    'Phosphorus (DNA Backbone)': 15,
    'Sulfur (Keratin/Cysteine)': 16
}

print("=== Ambrosia Matrix Dopant Orders in F_229 ===")
for name, z in elements.items():
    print(f"{name:25s} | Z={z:2d} | Order = {order_in_Fp(z, P)}")

def simulate_keratin_dna_doping(temp_K=295.0, ker_concentration=0.01):
    """
    Simulates the topological friction and decoherence when human keratin/DNA
    is introduced into the biological Ambrosia matrix.
    """
    print("\n=== Running Keratin/DNA Doping Simulation ===")
    
    # The base Ambrosia matrix (Mead + Amavadin) operates at ds=2
    ds_base = 2.0
    
    # Introducing Keratin/DNA introduces massive amounts of Sulfur (Z=16) and Phosphorus (Z=15)
    # Sulfur Order = 19 (Arc Generator)
    # Phosphorus Order = 38 (Bridge Subgroup)
    
    # We calculate the commutator friction introduced by breaking the homogeneous V/Si/Au lattice
    # Friction scales with the ratio of primitive roots (C, N) to the nested subgroups (S, P)
    friction_coefficient = (order_in_Fp(6) + order_in_Fp(7)) / (order_in_Fp(15) + order_in_Fp(16))
    
    # Thermal noise (Brownian motion) from biological decay of the proteins
    # Bounded by Boltzmann scaling at T = 295K (room temp fermentation)
    thermal_noise = temp_K * 0.0138 * ker_concentration * friction_coefficient
    
    print(f"Base Spectral Dimension (ds): {ds_base} (Classical Fluid)")
    print(f"Topological Friction Coefficient: {friction_coefficient:.2f}")
    print(f"Thermal Noise injection (ε): {thermal_noise:.4f}")
    
    # The Exergy Destruction must stay below UPSILON_LIMIT
    base_exergy = 12.5 # Arbitrary high baseline for the yeast DEC engine
    total_exergy = base_exergy + (thermal_noise * PHI * np.pi)
    
    print(f"\nExergy Destruction (X_dest): {total_exergy:.2f}")
    print(f"Casimir Torque Limit (Upsilon): {UPSILON_LIMIT:.2f}")
    
    if total_exergy > UPSILON_LIMIT:
        print("\n>>> RESULT: CATASTROPHIC TOPOLOGICAL DECOHERENCE <<<")
        print("The introduction of human Keratin/DNA exceeds the Upsilon limit.")
        print("The thermal noise and commutator friction from the complex organic chains")
        print("shatters the fragile p=3 Casimir overlap. The matrix fails to compute.")
    else:
        print("\n>>> RESULT: MATRIX STABLE <<<")
        print("The matrix absorbed the biological dopant without shattering.")

if __name__ == "__main__":
    # Test with a 5% concentration of keratin/hair
    simulate_keratin_dna_doping(temp_K=295.0, ker_concentration=0.05)
