import numpy as np

# Physical / Metareal Constants
P = 229
UPSILON_LIMIT = 45 / np.pi  # ~14.32 (Casimir torque limit)
PHI = (1 + np.sqrt(5)) / 2  # ~1.618 (Golden ratio)
TEMP_K = 295.0              # Room temperature fermentation

def order_in_Fp(Z, p=P):
    if Z == 0: return 0
    Z = Z % p
    for d in range(1, p):
        if pow(Z, d, p) == 1:
            return d
    return p - 1

fungal_matrices = {
    "Amanita muscaria": {"element": "Vanadium (V)", "Z": 23},
    "Penicillium chrysogenum": {"element": "Cobalt (Co)", "Z": 27},
    "Saccharomyces cerevisiae": {"element": "Zinc (Zn)", "Z": 30},
    "Aspergillus niger": {"element": "Manganese (Mn)", "Z": 25},
    "SCOBY (Acetobacter)": {"element": "Copper (Cu)", "Z": 29}
}

patient_dopants = {
    "Saliva": {
        "elements": {"Potassium (K)": 19, "Calcium (Ca)": 20, "Phosphorus (P)": 15},
        "concentration": 0.05
    },
    "Urine": {
        "elements": {"Nitrogen (N)": 7, "Sodium (Na)": 11, "Chlorine (Cl)": 17},
        "concentration": 0.10
    }
}

# Pathologies act as independent variables that modify the dopant boundaries
pathologies = {
    "Healthy Baseline": {
        "extra_elements": {},
        "conc_multiplier": 1.0
    },
    "Heavy Metal Toxicity": {
        "extra_elements": {"Cadmium (Cd)": 48, "Lead (Pb)": 82},
        "conc_multiplier": 1.2
    },
    "Systemic Inflammation": {
        "extra_elements": {"Copper (Cu)": 29, "Iron (Fe)": 26},
        "conc_multiplier": 1.5
    },
    "Severe Renal Distress": {
        "extra_elements": {"Nitrogen (N_urea)": 7},
        "conc_multiplier": 2.5 # Massive concentration spike poisons the brew
    }
}

def simulate():
    results_md = "# Medicinal Brew: Pathology Boundary Analysis\n\n"
    results_md += "This report analyzes the topological boundaries of the Ambrosia brew when subjected to independent pathological variables (illnesses). Some illnesses introduce heavy metals or massive elemental shedding that act as toxic friction, 'poisoning' the brew and forcing decoherence.\n\n"
    
    for dopant_name, dopant_data in patient_dopants.items():
        results_md += f"## Substrate: {dopant_name}\n"
        
        for path_name, path_data in pathologies.items():
            results_md += f"### Pathology: {path_name}\n"
            
            # Combine elements
            active_elements = dopant_data['elements'].copy()
            active_elements.update(path_data['extra_elements'])
            active_conc = dopant_data['concentration'] * path_data['conc_multiplier']
            
            elem_str = ', '.join([f'{name} (Z={z}, ord={order_in_Fp(z)})' for name, z in active_elements.items()])
            results_md += f"**Active Profile:** {elem_str}\n"
            results_md += f"**Concentration Load:** {active_conc:.2f}\n\n"
            
            results_md += "| Fungal Matrix | Friction | Thermal Noise (ε) | Exergy (X_dest) | Status |\n"
            results_md += "|---|---|---|---|---|\n"
            
            dopant_orders = [order_in_Fp(z) for z in active_elements.values()]
            
            best_fungus = None
            lowest_exergy = 999
            
            for fungus_name, fungus_data in fungal_matrices.items():
                fungus_Z = fungus_data["Z"]
                fungus_order = order_in_Fp(fungus_Z)
                
                mismatch = sum([abs(fungus_order - do) for do in dopant_orders])
                
                if fungus_order in dopant_orders:
                    friction_coefficient = 1.0 + (mismatch / 400)
                else:
                    friction_coefficient = 4.0 + (mismatch / 100)
                    
                thermal_noise = TEMP_K * 0.0138 * active_conc * friction_coefficient
                base_exergy = 10.0 # Standard DEC baseline
                total_exergy = base_exergy + (thermal_noise * PHI * np.pi)
                
                if total_exergy < lowest_exergy:
                    lowest_exergy = total_exergy
                    best_fungus = fungus_name
                
                if total_exergy > UPSILON_LIMIT:
                    status = "❌ **POISONED (Decoheres)**"
                else:
                    status = "✅ **STABLE (Cures)**"
                    
                results_md += f"| {fungus_name} | {friction_coefficient:.2f} | {thermal_noise:.2f} | {total_exergy:.2f} | {status} |\n"
            
            results_md += f"\n**Optimal Fungal Host:** {best_fungus}\n\n"

    with open("medicinal_brew_results.md", "w") as f:
        f.write(results_md)
        
    print("Simulation complete. Results written to medicinal_brew_results.md")

if __name__ == "__main__":
    simulate()
