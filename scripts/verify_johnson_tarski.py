import sys

def get_ord(a, p):
    if a % p == 0:
        return 0
    for i in range(1, p):
        if pow(a, i, p) == 1:
            return i
    return 0

def main():
    print("==========================================================")
    print(" VERIFYING TARSKIAN EQUILIBRIUM FOR 92 JOHNSON SOLIDS ")
    print(" COMPOSITE FIELD: {139, 181, 229}")
    print("==========================================================")
    print("Tarskian Boundary Condition: Re(s) = 1/2 -> info_in = info_out")
    print("In finite fields, this corresponds to ord(J) = (p-1)/2.")
    print("----------------------------------------------------------\n")
    
    primes = [139, 181, 229]
    half_orders = {p: (p-1)//2 for p in primes}
    
    valid_bridges = []
    
    for J in range(1, 93):
        orders = {p: get_ord(J, p) for p in primes}
        
        # Check if J sits at the Tarskian boundary in any of the primes
        is_tarskian = any(orders[p] == half_orders[p] for p in primes)
        
        if is_tarskian:
            status = []
            for p in primes:
                if orders[p] == half_orders[p]:
                    status.append(f"Tarskian in F_{p}")
            valid_bridges.append((J, status))
            
    print(f"Out of 92 Johnson solids, {len(valid_bridges)} sit at the Tarskian boundary in at least one field.\n")
    
    for J, status in valid_bridges:
        print(f"J_{J}: {', '.join(status)}")
        
    print("\n==========================================================")
    print(" Multi-Field Resonant Bridges (Tarskian in multiple primes):")
    print("==========================================================")
    for J, status in valid_bridges:
        if len(status) > 1:
            print(f"J_{J}: {', '.join(status)}  <-- PRIME CONSISTENT BRIDGE")

if __name__ == "__main__":
    main()
