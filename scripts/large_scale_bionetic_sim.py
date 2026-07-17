import numpy as np
import csv

# Metareal Constants
P = 229
UPSILON_LIMIT = 45 / np.pi  # ~14.32
PHI = (1 + np.sqrt(5)) / 2
TEMP_K = 295.0

def order_in_Fp(Z, p=P):
    if Z == 0: return 0
    Z = Z % p
    for d in range(1, p):
        if pow(Z, d, p) == 1:
            return d
    return p - 1

# Microbial Reactors (The Fermentation Engine)
# Defined by their primary trace element utilized in enzymatic or structural processes
reactors = {
    "Amanita muscaria": {"element": "Vanadium (V)", "Z": 23},
    "Penicillium chrysogenum": {"element": "Cobalt (Co)", "Z": 27},
    "Saccharomyces cerevisiae": {"element": "Zinc (Zn)", "Z": 30},
    "Aspergillus niger": {"element": "Manganese (Mn)", "Z": 25},
    "Acetobacter (SCOBY)": {"element": "Copper (Cu)", "Z": 29},
    "Lactobacillus spp.": {"element": "Magnesium (Mg)", "Z": 12},
    "Streptomyces": {"element": "Iron (Fe)", "Z": 26},
    "Bacillus subtilis": {"element": "Calcium (Ca)", "Z": 20}
}

# Pathogen Dopants (The "Vaccines")
pathogens = {
    "Viral (Rhinovirus/SARS-CoV-2)": {
        "vector": "Saliva/Mucus",
        "elements": {"Phosphorus (P)": 15, "Zinc (Zn)": 30, "Selenium (Se)": 34},
        "concentration": 0.08
    },
    "Bacterial UTI (E. coli)": {
        "vector": "Urine",
        "elements": {"Sulfur (S)": 16, "Phosphorus (P)": 15, "Magnesium (Mg)": 12, "Iron (Fe)": 26},
        "concentration": 0.12
    },
    "Bacterial Lung (S. pneumoniae)": {
        "vector": "Sputum",
        "elements": {"Manganese (Mn)": 25, "Zinc (Zn)": 30, "Copper (Cu)": 29},
        "concentration": 0.09
    },
    "Genetic Marker (Cystic Fibrosis)": {
        "vector": "Hair/Sweat",
        "elements": {"Sodium (Na)": 11, "Chlorine (Cl)": 17, "Magnesium (Mg)": 12},
        "concentration": 0.15
    }
}

def compute_friction(fungus_order, dopant_orders):
    # Algebraic mismatch in the F_229 subgroup lattice
    mismatch = sum([abs(fungus_order - do) for do in dopant_orders])
    
    if fungus_order in dopant_orders:
        return 1.0 + (mismatch / 500.0) # Harmonized
    else:
        return 3.5 + (mismatch / 150.0) # Dissonant

def compute_metabolization_feedback(total_exergy, friction):
    # If the system is stable, the microbe metabolizes the pathogen into a medicinal alkaloid.
    # The efficiency of this feedback loop is inversely proportional to the friction.
    # A perfect match yields high efficiency (>80%)
    if total_exergy > UPSILON_LIMIT:
        return 0.0
    
    # Synthesis efficiency scales based on how effortlessly the lattice commutes
    efficiency = max(0.0, 100.0 - (friction * 15.0))
    return efficiency

def run_simulation():
    csv_data = [["Pathogen", "Vector", "Microbial Reactor", "Reactor Element", "Friction", "Thermal Noise", "Total Exergy", "Synthesis Efficiency (%)", "Status"]]
    
    md_output = "# Bionetic Vaccine Synthesis Report\n\n"
    md_output += "This matrix cross-references severe pathogens (delivered via bodily fluid) against 8 microbial fermentation reactors. It computes the topological friction, Exergy destruction, and the **Metabolization Synthesis Efficiency** (how effectively the microbe converts the pathogen into a medicinal alkaloid without boiling over).\n\n"
    
    # Bulk thermodynamic base of Honey/Water provides base exergy
    base_exergy = 10.5
    
    for path_name, path_data in pathogens.items():
        md_output += f"## Pathogen: {path_name} (Vector: {path_data['vector']})\n"
        md_output += f"**Elemental Signature:** {', '.join([f'{name} (Z={z}, ord={order_in_Fp(z)})' for name, z in path_data['elements'].items()])}\n\n"
        
        md_output += "| Microbial Reactor | Primary Element | Friction | Exergy (X_dest) | Synthesis Effic. | Status |\n"
        md_output += "|---|---|---|---|---|---|\n"
        
        dopant_orders = [order_in_Fp(z) for z in path_data['elements'].values()]
        
        best_reactor = None
        best_efficiency = 0.0
        
        for reactor_name, reactor_data in reactors.items():
            reactor_order = order_in_Fp(reactor_data["Z"])
            
            friction = compute_friction(reactor_order, dopant_orders)
            thermal_noise = TEMP_K * 0.0138 * path_data['concentration'] * friction
            
            total_exergy = base_exergy + (thermal_noise * PHI * np.pi)
            
            # Compute Metabolization Pathway Feedback
            synthesis_eff = compute_metabolization_feedback(total_exergy, friction)
            
            if total_exergy > UPSILON_LIMIT:
                status = "❌ **LETHAL (Decoherence)**"
            else:
                status = "✅ **VIABLE**"
                if synthesis_eff > best_efficiency:
                    best_efficiency = synthesis_eff
                    best_reactor = reactor_name
                    
            # Log for CSV
            csv_data.append([path_name, path_data['vector'], reactor_name, f"{reactor_data['element']} (ord={reactor_order})", round(friction, 2), round(thermal_noise, 2), round(total_exergy, 2), round(synthesis_eff, 1), status])
            
            # Log for MD
            eff_str = f"{synthesis_eff:.1f}%" if synthesis_eff > 0 else "N/A"
            md_output += f"| {reactor_name} | {reactor_data['element']} (ord={reactor_order}) | {friction:.2f} | {total_exergy:.2f} | {eff_str} | {status} |\n"
            
        md_output += f"\n**Optimum Medicinal Reactor:** {best_reactor} ({best_efficiency:.1f}% Efficiency)\n\n"

    # Write MD
    with open("vaccine_brew_results.md", "w") as f:
        f.write(md_output)
        
    # Write CSV
    with open("medicinal_brew_matrix.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)
        
    print("Simulation completed successfully. Results saved to vaccine_brew_results.md and medicinal_brew_matrix.csv")

if __name__ == "__main__":
    run_simulation()
