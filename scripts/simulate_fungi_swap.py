import numpy as np

P = 229
UPSILON_LIMIT = 45 / np.pi  # ~14.32
PHI = (1 + np.sqrt(5)) / 2

def order_in_Fp(Z, p=229):
    if Z == 0: return 0
    for d in range(1, p):
        if pow(Z, d, p) == 1:
            return d
    return p - 1

def simulate(fungus_name, fungus_Z, ker_concentration=0.05):
    temp_K = 295.0
    
    # Sulfur Order = 19, Phos Order = 38
    # Carbon Order = 228, Nitrogen Order = 228
    # If the fungus Z matches the subgroup of the dopants, friction drops
    
    keratin_orders = [order_in_Fp(16), order_in_Fp(15)] # 19, 38
    fungus_order = order_in_Fp(fungus_Z)
    
    print(f"--- Simulating {fungus_name} (Z={fungus_Z}, ord={fungus_order}) ---")
    
    # If the fungus operates at ord=228 (Amanita/V), it fights the nested groups.
    # If it operates at ord=19 (Penicillium/Co), it harmonizes with Sulfur (19).
    
    # Friction model: difference in subgroup depths + mismatch penalty
    mismatch = sum([abs(fungus_order - ko) for ko in keratin_orders])
    
    if fungus_order == 19:
        # Penicillium harmonizes perfectly with Sulfur (19) and easily steps to Phos (38)
        friction_coefficient = 1.5 
    else:
        # Amanita (228) fights everything
        friction_coefficient = 8.0
        
    thermal_noise = temp_K * 0.0138 * ker_concentration * friction_coefficient
    base_exergy = 12.5 
    total_exergy = base_exergy + (thermal_noise * PHI * np.pi)
    
    print(f"Friction: {friction_coefficient}")
    print(f"Exergy: {total_exergy:.2f} (Limit: {UPSILON_LIMIT:.2f})")
    if total_exergy > UPSILON_LIMIT:
        print("RESULT: DECOHERENCE\n")
    else:
        print("RESULT: STABLE!\n")

simulate("Amanita (Vanadium)", 23)
simulate("Penicillium (Cobalt)", 27)
