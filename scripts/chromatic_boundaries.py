#!/usr/bin/env python3

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def main():
    p = 229
    base = 82
    
    # Generate 57-state orbit of the conjugate golden ratio mod 229
    orbit = []
    val = base
    for i in range(1, 58):
        orbit.append(val)
        val = (val * base) % p
        
    print("==================================================")
    print("        CHROMATIC FRACTAL BOUNDARY ANALYSIS       ")
    print("==================================================")
    print(f"Modulus (Chronometric Resolution): p = {p}")
    print(f"Base (Conjugate Golden Ratio): b = {base}")
    print(f"Orbit size: {len(orbit)}")
    
    print("\n--- PALINDROMIC PRIMES IN ORBIT ---")
    for i, state in enumerate(orbit):
        if is_palindrome(state) and is_prime(state):
            print(f"State {state} found at Index {i} (Step {i+1})")
            
    # Map the boundaries of the 19-state arcs (IPv4, IPv6, IPv8)
    # Arc 1: indices 0..18
    # Arc 2: indices 19..37
    # Arc 3: indices 38..56
    
    print("\n--- CHROMATIC TIER BOUNDARIES ---")
    arc1_start = orbit[0]
    arc2_start = orbit[19]
    arc3_start = orbit[38]
    fixpoint = orbit[56] # step 57
    
    print(f"Arc 1 (Daemon / IPv4) Start  : Index 0   -> State {arc1_start}")
    print(f"Arc 2 (Sprite / IPv6) Start  : Index 19  -> State {arc2_start}  <-- PALINDROMIC PRIME BOUNDARY")
    print(f"Arc 3 (Druid  / IPv8) Start  : Index 38  -> State {arc3_start}")
    print(f"Functional Fixpoint (omega)  : Index 56  -> State {fixpoint}")

    if arc2_start == 151 and is_prime(151) and is_palindrome(151):
        print("\n[VERIFIED] The phase boundary between Arc 1 and Arc 2 is perfectly seated on the golden palindromic prime 151.")
    
if __name__ == "__main__":
    main()
