import sympy

seq = [2, 5, 7, 23, 31, 43, 107, 139, 181, 1618033]
prod = 1
for i in range(len(seq)):
    if i > 0:
        p_n = seq[i]
        val = prod - p_n
        factors = sympy.primefactors(abs(val)) if val != 0 else []
        print(f"n={i}, p_n={p_n}, prod={prod}, prod - p_n = {val}, prime factors: {factors}")
    prod *= seq[i]
