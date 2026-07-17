import numpy as np
import math
import csv

# Metareal Physical Constants
UPSILON_LIMIT = 14.32           # Casimir Torque Exergy Limit
PHI = 1.61803                   # Golden ratio
P = 229                         # Prime chronological base
TEMP_K = 295.0                  # Ambient temp (Kelvin)

def order_in_Fp(Z, p=P):
    if Z == 0: return 0
    Z = Z % p
    for d in range(1, p):
        if pow(Z, d, p) == 1: return d
    return p - 1

pathogens = {
    "Rhinovirus (RNA)": {"elements": [15, 30, 34]},
    "E. coli (UTI)": {"elements": [16, 15, 12, 26]},
    "S. pneumoniae": {"elements": [25, 30, 29]},
    "Cystic Fibrosis (Genetic)": {"elements": [11, 17, 12]}
}

matrices = {
    "Amanita (V)": 23,
    "Penicillium (Co)": 27,
    "Saccharomyces (Zn)": 30,
    "Aspergillus (Mn)": 25,
    "SCOBY (Cu)": 29,
    "Lactobacillus (Mg)": 12,
    "Streptomyces (Fe)": 26,
    "Bacillus (Ca)": 20
}

substrates = {
    "Pure Mead": [],
    "Melomel (Fruit)": [19],
    "Braggot (Grain)": [14],
    "Pyment (Fruit+Grain)": [19, 14]
}

harvest_freqs = [3, 5, 7, 10, 14, 21, 30]
harvest_quants = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
SIM_DAYS = 180

class OptimizationEngine:
    def __init__(self, dopants, matrix_z, sub_elements):
        self.dopants = dopants
        self.matrix_z = matrix_z
        self.sub_elements = sub_elements
        
        matrix_order = order_in_Fp(self.matrix_z)
        dopant_orders = [order_in_Fp(z) for z in self.dopants]
        sub_orders = [order_in_Fp(z) for z in self.sub_elements]
        
        raw_mismatch = sum([abs(matrix_order - do) for do in dopant_orders])
        buffer_absorption = 0.0
        for so in sub_orders:
            for do in dopant_orders:
                if so == do or abs(so - do) <= 19:
                    buffer_absorption += 150.0 
                    
        effective_mismatch = max(0.0, raw_mismatch - buffer_absorption)
        
        if matrix_order in dopant_orders:
            self.shear_factor = 1.0 + (effective_mismatch / 1000.0)
        else:
            self.shear_factor = 3.0 + (effective_mismatch / 300.0)
            
        K = 2.0 / (self.shear_factor * 1.1)
        if K < 1.0:
            self.ds = 2.0 + (1.0 - K)
        else:
            self.ds = max(1.5, 2.0 / K)
            
        s_gen_base = 0.08
        topological_penalty = math.exp(self.ds - 1.5)
        self.daily_s_gen = s_gen_base * self.shear_factor * topological_penalty
        self.daily_x_gen = (TEMP_K * self.daily_s_gen * PHI) / 100.0

    def simulate(self, freq, quant):
        x_dest = 2.0
        total_potency_harvested = 0.0
        days_survived = 0
        current_potency = 0.0
        
        for day in range(1, SIM_DAYS + 1):
            x_dest += self.daily_x_gen
            
            # Potency accumulates as a function of ds resonance and time
            if self.ds < 1.8:
                # If near pAQFT resonance, potency grows exponentially with time (up to a cap)
                current_potency += math.log(day % freq + 2) * (1.8 - self.ds)
            else:
                current_potency += 0.0
                
            if x_dest > UPSILON_LIMIT:
                break # Catastrophic Thermodynamic Fragmentation
                
            days_survived = day
            
            if day % freq == 0:
                # Harvest
                x_dest = x_dest * (1.0 - quant)
                # We harvest 'quant' fraction of the accumulated potency
                total_potency_harvested += current_potency * quant
                # The remaining fluid retains the rest of the potency
                current_potency = current_potency * (1.0 - quant)
                
        # Sustainable Potency = Total Potency / Days
        if days_survived == SIM_DAYS:
            sustainable_potency = total_potency_harvested / SIM_DAYS
        else:
            sustainable_potency = 0.0 # Failed
            
        return days_survived, sustainable_potency

def run_exhaustive_optimization():
    csv_data = [["Pathogen", "Matrix", "Substrate", "Freq (Days)", "Harvest Quant", "Days Survived", "Sustainable Potency (Score)"]]
    
    # Track the best schedule for each pathogen
    best_results = {}
    for p in pathogens.keys():
        best_results[p] = {"score": -1, "matrix": "", "sub": "", "freq": 0, "quant": 0.0}

    total_perms = 0
    for p_name, p_data in pathogens.items():
        for m_name, m_z in matrices.items():
            for s_name, s_elems in substrates.items():
                engine = OptimizationEngine(p_data["elements"], m_z, s_elems)
                
                for freq in harvest_freqs:
                    for quant in harvest_quants:
                        total_perms += 1
                        days, score = engine.simulate(freq, quant)
                        
                        csv_data.append([p_name, m_name, s_name, freq, quant, days, round(score, 3)])
                        
                        if score > best_results[p_name]["score"] and days == SIM_DAYS:
                            best_results[p_name] = {
                                "score": score,
                                "matrix": m_name,
                                "sub": s_name,
                                "freq": freq,
                                "quant": quant
                            }
                            
    # Write CSV
    with open("exhaustive_bionetic_matrix.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)
        
    # Write MD Report
    md_output = "# Optimal Harvest Bounds: Ambrosia Solera System\n\n"
    md_output += f"Exhaustive simulation completed across **{total_perms} permutations** (180-day chronological loop). "
    md_output += "The optimization target was **Sustainable Potency**: balancing the accumulation of secondary medicinal metabolites against the thermodynamic requirement to bleed Exergy (preventing $\\Upsilon > 14.32$).\n\n"
    
    for p_name, res in best_results.items():
        md_output += f"## {p_name}\n"
        if res['score'] > 0:
            md_output += f"*   **Optimal Matrix:** {res['matrix']}\n"
            md_output += f"*   **Optimal Substrate:** {res['sub']}\n"
            md_output += f"*   **Harvest Frequency:** Every **{res['freq']} days**\n"
            md_output += f"*   **Harvest Quantity:** **{int(res['quant']*100)}%** volume bleed\n"
            md_output += f"*   **Potency Score:** {res['score']:.3f} (Maximized sustainable alkaloid yield)\n\n"
        else:
            md_output += "*   ❌ **NO STABLE CONFIGURATION FOUND** (All 180-day loops fragmented).\n\n"
            
    with open("optimal_harvest_bounds.md", "w") as f:
        f.write(md_output)
        
    print(f"Exhaustive optimization complete. Tested {total_perms} permutations.")

if __name__ == "__main__":
    run_exhaustive_optimization()
