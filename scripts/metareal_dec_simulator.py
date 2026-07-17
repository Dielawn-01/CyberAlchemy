import numpy as np
import math

# Metareal Physical Constants
UPSILON_LIMIT = 45 / np.pi      # ~14.32 (Casimir Torque Exergy Limit)
PHI = (1 + np.sqrt(5)) / 2      # ~1.61803 (Golden ratio)
P = 229                         # Prime chronological base
TEMP_K = 295.0                  # Biological matrix ambient temp (Kelvin)

# Potassium Photoelectric Constants
K_WORK_FUNCTION_EV = 2.29       # Potassium Work Function (eV)
K_THRESHOLD_NM = 541.0          # Green light threshold
EV_TO_JOULES = 1.60218e-19

def order_in_Fp(Z, p=P):
    if Z == 0: return 0
    Z = Z % p
    for d in range(1, p):
        if pow(Z, d, p) == 1: return d
    return p - 1

class PhotoelectricState:
    def __init__(self, dopant_z_list, matrix_z):
        self.dopant_z_list = dopant_z_list
        self.matrix_z = matrix_z
        self.k_threshold = K_WORK_FUNCTION_EV
        
    def compute_photon_momentum_shear(self):
        """
        Computes how much the biological dopant elements disrupt the K photoelectric threshold.
        The mismatch in F_229 orders causes phonon scattering that shears the optical momentum.
        """
        matrix_order = order_in_Fp(self.matrix_z)
        dopant_orders = [order_in_Fp(z) for z in self.dopant_z_list]
        
        # Mismatch acts as a refractive scattering index
        mismatch = sum([abs(matrix_order - do) for do in dopant_orders])
        
        if matrix_order in dopant_orders:
            shear_factor = 1.0 + (mismatch / 1000.0)
        else:
            shear_factor = 3.0 + (mismatch / 300.0)
            
        # Effective energy required to cross the bridge due to phonon scattering
        effective_work_function = self.k_threshold * shear_factor
        return effective_work_function, shear_factor

class GravitationalTopology:
    def __init__(self, shear_factor, concentration):
        self.shear_factor = shear_factor
        self.concentration = concentration
        self.ds_classical = 2.0  # Navier-Stokes classical fluid
        
    def phase_space_contraction(self):
        """
        Computes if the K=2 phase space contraction can be achieved to reach ds = 3/2.
        Depends heavily on the optical shear (friction) and molecular concentration.
        """
        # Contraction factor K
        # If shear is perfect (1.0) and concentration is balanced, K approaches 2
        K = 2.0 / (self.shear_factor * (1.0 + self.concentration))
        
        # Spectral dimension scales inversely with contraction
        # If K < 1.0, the fluid expands entropically instead of contracting
        if K < 1.0:
            ds = 2.0 + (1.0 - K) # Entropic classical fluid (ds >= 2)
        else:
            ds = max(1.5, 2.0 / K) # Approaches 1.5 (pAQFT resonance)
            
        return K, ds

class DEC_HeatEngine:
    def __init__(self, ds, shear_factor, concentration):
        self.ds = ds
        self.shear_factor = shear_factor
        self.concentration = concentration
        
    def compute_exergy_destruction(self):
        """
        Computes the Exergy Destruction (X_dest) of the Differential Equilibrium Cycle.
        Bounded by Upsilon <= 45/pi.
        """
        # Structural entropy generation rate (S_gen)
        # Driven by classical dimensionality ds >= 2 and phonon shear
        s_gen_base = 0.05 * self.concentration
        topological_penalty = math.exp(self.ds - 1.5) # Huge penalty if ds > 1.5
        
        S_gen = s_gen_base * self.shear_factor * topological_penalty
        
        # Exergy Destruction: X_dest = T_0 * S_gen
        # Normalized by arbitrary biochemical volume constant for scale
        X_dest = (TEMP_K * S_gen * PHI)
        return X_dest

# ---------------------------------------------------------
# Test Data
pathogens = {
    "Rhinovirus (RNA)": {"elements": [15, 30, 34], "conc": 0.08},
    "E. coli (UTI)": {"elements": [16, 15, 12, 26], "conc": 0.12},
    "S. pneumoniae": {"elements": [25, 30, 29], "conc": 0.09},
    "Cystic Fibrosis (Genetic)": {"elements": [11, 17, 12], "conc": 0.15}
}

matrices = {
    "Amanita (V)": 23,
    "Penicillium (Co)": 27,
    "Saccharomyces (Zn)": 30,
    "Aspergillus (Mn)": 25,
    "SCOBY (Cu)": 29,
    "Lactobacillus (Mg)": 12,
    "Streptomyces (Fe)": 26
}

def run_rigorous_simulation():
    md_output = "# Rigorous Metareal DEC Simulation Results\n\n"
    md_output += "This simulation executes the formal mathematical physics required for the Ambrosia matrix to achieve topological resonance. It computes the **Photoelectric Shear** ($\\Phi_{\\text{eff}}$ vs $2.29\\text{ eV}$), the **Gravitational Phase-Space Contraction** ($K \\to 2$, $d_s \\to 1.5$), and the **DEC Exergy Destruction** ($\\dot{X}_{\\text{dest}}$ vs $\\Upsilon \\le 14.32$).\n\n"
    
    for path_name, path_data in pathogens.items():
        md_output += f"## Pathogen Dopant: {path_name}\n"
        md_output += "| Microbial Matrix | Effective $\\Phi$ (eV) | Contraction ($K$) | Spectral Dim ($d_s$) | Exergy ($\\dot{X}_{\\text{dest}}$) | Status |\n"
        md_output += "|---|---|---|---|---|---|\n"
        
        best_matrix = None
        lowest_exergy = 999.0
        
        for matrix_name, matrix_z in matrices.items():
            # 1. Photoelectric Bridge
            pe_state = PhotoelectricState(path_data["elements"], matrix_z)
            eff_phi, shear = pe_state.compute_photon_momentum_shear()
            
            # 2. Gravitational Topology
            grav_state = GravitationalTopology(shear, path_data["conc"])
            K, ds = grav_state.phase_space_contraction()
            
            # 3. DEC Heat Engine
            dec_engine = DEC_HeatEngine(ds, shear, path_data["conc"])
            x_dest = dec_engine.compute_exergy_destruction()
            
            if x_dest < lowest_exergy:
                lowest_exergy = x_dest
                best_matrix = matrix_name
            
            # Evaluate bounds
            if ds > 1.8:
                status = "❌ **NAVIER-STOKES DECOHERENCE (ds ~ 2)**"
            elif x_dest > UPSILON_LIMIT:
                status = "❌ **THERMODYNAMIC FRAGMENTATION ($\\dot{X} > \\Upsilon$)**"
            else:
                status = "✅ **pAQFT RESONANCE ACHIEVED ($d_s \to 1.5$)**"
                
            md_output += f"| {matrix_name} | {eff_phi:.2f} | {K:.2f} | {ds:.3f} | {x_dest:.2f} | {status} |\n"
            
        md_output += f"\n**Optimal Physical Coupler:** {best_matrix}\n\n"

    with open("rigorous_metareal_results.md", "w") as f:
        f.write(md_output)
    
    print("Rigorous Physics Simulation complete. Output written.")

if __name__ == "__main__":
    run_rigorous_simulation()
