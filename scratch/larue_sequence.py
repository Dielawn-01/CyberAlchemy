import sympy

def generate_larue_sequence(n_terms):
    seq = [2]
    for _ in range(1, n_terms):
        product = 1
        for p in seq:
            product *= p
        
        target = product - 1
        factors = sympy.primefactors(target)
        # Assuming we take the smallest prime factor not already in the sequence, 
        # or maybe just the smallest prime factor?
        # Let's print all factors to see.
        print(f"Product: {product}, target: {target}, factors: {factors}")
        
        # usually Euclid-Mullin sequence takes the smallest prime factor
        for f in factors:
            if f not in seq:
                seq.append(f)
                break
    return seq

print("Sequence:")
print(generate_larue_sequence(15))
