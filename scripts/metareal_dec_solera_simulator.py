import numpy as np
import math

# Metareal Physical Constants
UPSILON_LIMIT = 14.32           # Casimir Torque Exergy Limit
PHI = 1.61803                   # Golden ratio
P = 229                         # Prime chronological base
TEMP_K = 295.0                  # Ambient temp (Kelvin)
K_WORK_FUNCTION_EV = 2.29       # Potassium Work Function

def order_in_Fp(Z, p=P):
    if Z == 0: return 0
    Z = Z % p
    for d in range(1, p):
        if pow(Z, d, p) == 1: return d
    return p - 1

class SoleraEngine:
    def __init__(self, dopants, matrix_z, substrate):
        self.dopants = dopants
        self.matrix_z = matrix_z
        self.substrate = substrate
        self.x_dest = 2.0  # Initial thermodynamic heat of the matrix
        
        # Substrate Buffers
        self.substrate_elements = []
        if substrate == "Melomel (Fruit)":
            self.substrate_elements.append(19) # Potassium buffer
        elif substrate == "Braggot (Grain)":
            self.substrate_elements.append(14) # Silicon buffer
        elif substrate == "Pyment (Fruit+Grain)":
            self.substrate_elements.extend([19, 14]) # Max buffering
            
    def compute_daily_s_gen(self):
        matrix_order = order_in_Fp(self.matrix_z)
        dopant_orders = [order_in_Fp(z) for z in self.dopants]
        sub_orders = [order_in_Fp(z) for z in self.substrate_elements]
        
        # Calculate raw mismatch
        raw_mismatch = sum([abs(matrix_order - do) for do in dopant_orders])
        
        # Apply Substrate Buffers
        # If the substrate provides an order that matches a dopant's order, it absorbs the shear
        buffer_absorption = 0.0
        for so in sub_orders:
            for do in dopant_orders:
                if so == do or abs(so - do) <= 19: # 19-adic color tolerance
                    buffer_absorption += 150.0 
                    
        effective_mismatch = max(0.0, raw_mismatch - buffer_absorption)
        
        if matrix_order in dopant_orders:
            shear_factor = 1.0 + (effective_mismatch / 1000.0)
        else:
            shear_factor = 3.0 + (effective_mismatch / 300.0)
            
        K = 2.0 / (shear_factor * 1.1)
        if K < 1.0:
            ds = 2.0 + (1.0 - K)
        else:
            ds = max(1.5, 2.0 / K)
            
        s_gen_base = 0.08
        topological_penalty = math.exp(ds - 1.5)
        
        return s_gen_base * shear_factor * topological_penalty, ds
        
    def step_day(self):
        s_gen, ds = self.compute_daily_s_gen()
        # Daily accumulation of Exergy
        daily_x = (TEMP_K * s_gen * PHI) / 100.0  # Normalized for daily rate
        self.x_dest += daily_x
        return self.x_dest, ds
        
    def solera_bleed(self, fractional_harvest):
        # Harvesting a percentage of the Ambrosia removes that percentage of accumulated Exergy
        # and replaces it with fresh, cool honey/water/substrate.
        self.x_dest = self.x_dest * (1.0 - fractional_harvest)

def run_solera_sim():
    # Test cases that previously suffered Catastrophic Thermodynamic Fragmentation
    test_cases = [
        {"name": "E. coli vs Saccharomyces", "dopants": [16, 15, 12, 26], "matrix_z": 30},
        {"name": "Rhinovirus vs Amanita", "dopants": [15, 30, 34], "matrix_z": 23}
    ]
    
    substrates = ["Pure Mead", "Melomel (Fruit)", "Braggot (Grain)", "Pyment (Fruit+Grain)"]
    
    md_output = "# Solera Bioreactor \& Complex Substrate Results\n\n"
    md_output += "This simulation tests if a **Continuous Solera Bleed** (harvesting 20% volume at Day 15) and **Complex Substrates** (Fruit K-buffers, Grain Si-buffers) can resurrect pairings that normally suffer Catastrophic Thermodynamic Fragmentation in a closed-batch pure mead.\n\n"
    
    for case in test_cases:
        md_output += f"## {case['name']}\n"
        md_output += "| Substrate Matrix | Day 14 ($\\dot{X}_{dest}$) | Day 15 Harvest | Day 30 ($\\dot{X}_{dest}$) | Final Status |\n"
        md_output += "|---|---|---|---|---|\n"
        
        for sub in substrates:
            engine = SoleraEngine(case["dopants"], case["matrix_z"], sub)
            
            # Days 1-14
            for day in range(1, 15):
                x_dest, ds = engine.step_day()
                
            day_14_x = engine.x_dest
            
            # Day 15 Solera Harvest
            engine.solera_bleed(0.20) # 20% harvest
            
            # Days 16-30
            for day in range(16, 31):
                x_dest, ds = engine.step_day()
                
            day_30_x = engine.x_dest
            
            if day_30_x > UPSILON_LIMIT or day_14_x > UPSILON_LIMIT:
                status = "❌ **FRAGMENTATION**"
            else:
                status = f"✅ **STABLE ($d_s={ds:.2f}$)**"
                
            md_output += f"| {sub} | {day_14_x:.2f} | 20% Bleed | {day_30_x:.2f} | {status} |\n"
            
        md_output += "\n"
        
    with open("solera_metareal_results.md", "w") as f:
        f.write(md_output)
    print("Solera simulation completed.")

if __name__ == "__main__":
    run_solera_sim()
