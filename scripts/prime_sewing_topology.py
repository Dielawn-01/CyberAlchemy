#!/usr/bin/env python3
"""
Prime Sewing Topology Analysis

Maps the full sewing graph of golden-split primes and analyzes:
1. The graph structure (degree distribution, clustering, components)
2. The sewing dimension spectrum
3. Where {229, 181, 139} sit in the topology
4. Natural communities / clusters
5. The 3-sewn vs 1-sewn subgraph structure

Authors: LaRue (Theory), Antigravity (Analysis)
"""

import math
import os
from collections import Counter, defaultdict

# ═══════════════════════════════════════════════════════════
# FIELD ARITHMETIC (from deep_prime_branch_hash.py)
# ═══════════════════════════════════════════════════════════

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0: return False
        i += 6
    return True

def sqrt_mod(n, p):
    if pow(n, (p-1)//2, p) != 1: return None
    if p % 4 == 3: return pow(n, (p+1)//4, p)
    q, s = p-1, 0
    while q % 2 == 0: q //= 2; s += 1
    z = 2
    while pow(z, (p-1)//2, p) != p-1: z += 1
    M, c, t, R = s, pow(z, q, p), pow(n, q, p), pow(n, (q+1)//2, p)
    while True:
        if t == 1: return R
        i = 0; tmp = t
        while tmp != 1: tmp = tmp*tmp % p; i += 1
        b = pow(c, 1 << (M-i-1), p)
        M, c, t, R = i, b*b%p, t*b*b%p, R*b%p

def golden_roots(p):
    s5 = sqrt_mod(5, p)
    if s5 is None: return None
    inv2 = pow(2, p-2, p)
    phi = (1 + s5) * inv2 % p
    pbar = (1 - s5 + p) * inv2 % p
    return phi, pbar

def multiplicative_order(base, mod):
    if base % mod == 0: return 0
    x, order = base % mod, 1
    while x != 1:
        x = x * base % mod
        order += 1
    return order

def build_golden_split_primes(limit):
    primes = []
    for p in range(7, limit):
        if not is_prime(p): continue
        if p % 5 not in [1, 4]: continue
        if p % 6 != 1: continue
        roots = golden_roots(p)
        if roots is None: continue
        phi, pbar = roots
        ord_pbar = multiplicative_order(pbar, p)
        ord_phi = multiplicative_order(phi, p)
        primes.append({
            'p': p, 'phi': phi, 'pbar': pbar,
            'ord_phi': ord_phi, 'ord_pbar': ord_pbar,
            'three_dec': ord_pbar % 3 == 0,
            'pisano_factors': factorize(ord_pbar),
        })
    return primes

def factorize(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def sewing_dim(a, b):
    g_phi = math.gcd(a['ord_phi'], b['ord_phi'])
    g_pbar = math.gcd(a['ord_pbar'], b['ord_pbar'])
    return min(g_phi, g_pbar)

# ═══════════════════════════════════════════════════════════
# GRAPH ANALYSIS
# ═══════════════════════════════════════════════════════════

def build_sewing_graph(primes, min_sew=1):
    """Build adjacency list with sewing dimensions as edge weights."""
    adj = defaultdict(list)
    edges = []
    for i, a in enumerate(primes):
        for j, b in enumerate(primes):
            if i >= j: continue
            sd = sewing_dim(a, b)
            if sd >= min_sew:
                adj[a['p']].append((b['p'], sd))
                adj[b['p']].append((a['p'], sd))
                edges.append((a['p'], b['p'], sd))
    return adj, edges

def connected_components(adj, all_nodes):
    visited = set()
    components = []
    for node in all_nodes:
        if node in visited: continue
        comp = []
        stack = [node]
        while stack:
            n = stack.pop()
            if n in visited: continue
            visited.add(n)
            comp.append(n)
            for neighbor, _ in adj.get(n, []):
                if neighbor not in visited:
                    stack.append(neighbor)
        components.append(comp)
    return components

def clustering_coefficient(adj, node):
    """Local clustering coefficient of a node."""
    neighbors = [n for n, _ in adj.get(node, [])]
    k = len(neighbors)
    if k < 2: return 0.0
    neighbor_set = set(neighbors)
    triangles = 0
    for i, n1 in enumerate(neighbors):
        for n2 in neighbors[i+1:]:
            # Check if n1 and n2 are connected
            if any(m == n2 for m, _ in adj.get(n1, [])):
                triangles += 1
    return 2 * triangles / (k * (k - 1))


def main():
    print("═══════════════════════════════════════════════════════════")
    print("  PRIME SEWING TOPOLOGY — Full Graph Analysis")
    print("═══════════════════════════════════════════════════════════")
    print()
    
    # Build universe
    LIMIT = 2000
    primes = build_golden_split_primes(LIMIT)
    all_p = [d['p'] for d in primes]
    prime_map = {d['p']: d for d in primes}
    print(f"Universe: {len(primes)} golden-split primes (p≡1 mod 6) below {LIMIT}")
    print()
    
    # ═══════════════════════════════════════════════════════
    # 1. ORD(φ̄) SPECTRUM
    # ═══════════════════════════════════════════════════════
    print("═══ ORD(φ̄) SPECTRUM ═══")
    print()
    
    orders = [(d['p'], d['ord_pbar'], d['three_dec']) for d in primes]
    orders.sort(key=lambda x: x[1])
    
    # Factor frequency in orders
    factor_freq = Counter()
    for d in primes:
        for f in d['pisano_factors']:
            factor_freq[f] += 1
    
    print("  Factor frequency in ord(φ̄) across all primes:")
    for f, count in sorted(factor_freq.items()):
        pct = 100 * count / len(primes)
        bar = "█" * int(pct / 2)
        print(f"    {f:>4}: {count:>3}/{len(primes)} ({pct:5.1f}%) {bar}")
    print()
    
    # 3-decomposable vs boundary
    three_dec = [d for d in primes if d['three_dec']]
    boundary = [d for d in primes if not d['three_dec']]
    print(f"  3-decomposable (3|ord(φ̄)): {len(three_dec)}/{len(primes)} ({100*len(three_dec)/len(primes):.0f}%)")
    print(f"  Boundary (3∤ord(φ̄)):       {len(boundary)}/{len(primes)} ({100*len(boundary)/len(primes):.0f}%)")
    print(f"  Boundary primes: {[d['p'] for d in boundary]}")
    print()
    
    # ═══════════════════════════════════════════════════════
    # 2. FULL SEWING GRAPH (min_sewing=1)
    # ═══════════════════════════════════════════════════════
    print("═══ FULL SEWING GRAPH (min_sewing=1) ═══")
    print()
    
    adj_1, edges_1 = build_sewing_graph(primes, min_sew=1)
    
    total_possible = len(primes) * (len(primes) - 1) // 2
    print(f"  Edges: {len(edges_1)}/{total_possible} ({100*len(edges_1)/total_possible:.1f}% density)")
    
    comps_1 = connected_components(adj_1, all_p)
    print(f"  Connected components: {len(comps_1)}")
    print(f"  Largest component: {len(comps_1[0])} nodes")
    
    # Degree distribution
    degrees_1 = {p: len(adj_1[p]) for p in all_p}
    avg_deg = sum(degrees_1.values()) / len(degrees_1)
    print(f"  Average degree: {avg_deg:.1f}")
    print(f"  Min degree: {min(degrees_1.values())} ({[p for p,d in degrees_1.items() if d==min(degrees_1.values())][:5]})")
    print(f"  Max degree: {max(degrees_1.values())} ({[p for p,d in degrees_1.items() if d==max(degrees_1.values())][:5]})")
    print()
    
    # ═══════════════════════════════════════════════════════
    # 3. 3-SEWN SUBGRAPH
    # ═══════════════════════════════════════════════════════
    print("═══ 3-SEWN SUBGRAPH (min_sewing=3) ═══")
    print()
    
    adj_3, edges_3 = build_sewing_graph(primes, min_sew=3)
    
    print(f"  Edges: {len(edges_3)}/{total_possible} ({100*len(edges_3)/total_possible:.1f}% density)")
    
    comps_3 = connected_components(adj_3, all_p)
    comps_3.sort(key=len, reverse=True)
    print(f"  Connected components: {len(comps_3)}")
    for i, comp in enumerate(comps_3[:5]):
        comp.sort()
        label = ""
        if 229 in comp: label += " [229✓]"
        if 181 in comp: label += " [181✓]"
        if 139 in comp: label += " [139✓]"
        print(f"    Component {i+1}: {len(comp)} nodes{label}")
        if len(comp) <= 15:
            print(f"      Primes: {comp}")
    if len(comps_3) > 5:
        isolated = [c for c in comps_3 if len(c) == 1]
        print(f"    ... {len(comps_3)-5} more components ({len(isolated)} isolated nodes)")
    print()
    
    # Degree distribution in 3-sewn subgraph
    degrees_3 = {p: len(adj_3.get(p, [])) for p in all_p}
    
    # Gauge triplet degrees
    print("  Gauge triplet degrees (3-sewn):")
    for gp in [229, 181, 139]:
        d = degrees_3[gp]
        cc = clustering_coefficient(adj_3, gp)
        neighbors = sorted([(n, s) for n, s in adj_3.get(gp, [])], key=lambda x: -x[1])
        top_5 = neighbors[:5]
        print(f"    p={gp}: degree={d}, clustering={cc:.3f}")
        print(f"      Top sewn neighbors: {[(n,s) for n,s in top_5]}")
    print()
    
    # ═══════════════════════════════════════════════════════
    # 4. SEWING DIMENSION SPECTRUM
    # ═══════════════════════════════════════════════════════
    print("═══ SEWING DIMENSION SPECTRUM ═══")
    print()
    
    sd_dist = Counter(sd for _, _, sd in edges_1)
    for sd_val, count in sorted(sd_dist.items()):
        bar = "█" * min(count, 60)
        print(f"    sew={sd_val:>4}: {count:>5} edges {bar}")
    print()
    
    # High-sewing edges (sd >= 9)
    high_sew = [(a, b, sd) for a, b, sd in edges_1 if sd >= 9]
    high_sew.sort(key=lambda x: -x[2])
    print(f"  High-sewing edges (sd ≥ 9): {len(high_sew)}")
    for a, b, sd in high_sew[:15]:
        oa = prime_map[a]['ord_pbar']
        ob = prime_map[b]['ord_pbar']
        print(f"    {a}↔{b}: sewing={sd} (ord(φ̄)={oa},{ob}, gcd={math.gcd(oa,ob)})")
    if len(high_sew) > 15:
        print(f"    ... and {len(high_sew)-15} more")
    print()
    
    # ═══════════════════════════════════════════════════════
    # 5. GAUGE TRIPLET TOPOLOGY
    # ═══════════════════════════════════════════════════════
    print("═══ GAUGE TRIPLET {229, 181, 139} TOPOLOGY ═══")
    print()
    
    # Internal sewing
    s_229_181 = sewing_dim(prime_map[229], prime_map[181])
    s_229_139 = sewing_dim(prime_map[229], prime_map[139])
    s_181_139 = sewing_dim(prime_map[181], prime_map[139])
    
    print(f"  Internal sewing:")
    print(f"    229↔181: {s_229_181}")
    print(f"    229↔139: {s_229_139}")
    print(f"    181↔139: {s_181_139}")
    print()
    
    # Shared neighbors
    n229 = set(n for n, _ in adj_3.get(229, []))
    n181 = set(n for n, _ in adj_3.get(181, []))
    n139 = set(n for n, _ in adj_3.get(139, []))
    
    shared_229_181 = n229 & n181
    shared_229_139 = n229 & n139
    shared_181_139 = n181 & n139
    shared_all = n229 & n181 & n139
    
    print(f"  Shared 3-sewn neighbors:")
    print(f"    229∩181: {len(shared_229_181)} primes → {sorted(shared_229_181)[:10]}{'...' if len(shared_229_181)>10 else ''}")
    print(f"    229∩139: {len(shared_229_139)} primes → {sorted(shared_229_139)}")
    print(f"    181∩139: {len(shared_181_139)} primes → {sorted(shared_181_139)}")
    print(f"    229∩181∩139: {len(shared_all)} primes → {sorted(shared_all)}")
    print()
    
    # Betweenness-like: how many shortest paths pass through gauge primes?
    # Simple proxy: is each gauge prime a cut vertex?
    print(f"  Structural role in 3-sewn subgraph:")
    for gp in [229, 181, 139]:
        # Remove gp and check if the component splits
        reduced_adj = {p: [(n,s) for n,s in adj_3.get(p,[]) if n != gp] 
                       for p in all_p if p != gp}
        reduced_nodes = [p for p in all_p if p != gp]
        reduced_comps = connected_components(reduced_adj, reduced_nodes)
        
        original_comp_size = len([c for c in comps_3 if gp in c][0]) if any(gp in c for c in comps_3) else 0
        new_largest = max(len(c) for c in reduced_comps) if reduced_comps else 0
        
        is_cut = len(reduced_comps) > len(comps_3)
        print(f"    p={gp}: {'CUT VERTEX' if is_cut else 'not a cut vertex'}, "
              f"removing splits {original_comp_size}→{[len(c) for c in reduced_comps if len(c)>1][:5]}")
    print()
    
    # ═══════════════════════════════════════════════════════
    # 6. COMMUNITY DETECTION (simple modularity)
    # ═══════════════════════════════════════════════════════
    print("═══ SEWING COMMUNITIES (by order divisibility) ═══")
    print()
    
    # Group primes by the largest prime factor of ord(φ̄)
    def largest_prime_factor(n):
        if n <= 1: return 1
        f = n
        d = 2
        while d * d <= f:
            while f % d == 0: f //= d
            d += 1
        return max(f, 1) if f > 1 else d-1
    
    communities = defaultdict(list)
    for d in primes:
        lpf = largest_prime_factor(d['ord_pbar'])
        communities[lpf].append(d['p'])
    
    print(f"  Communities by largest prime factor of ord(φ̄):")
    for lpf in sorted(communities.keys()):
        members = sorted(communities[lpf])
        label = ""
        if 229 in members: label += " ★229"
        if 181 in members: label += " ★181"
        if 139 in members: label += " ★139"
        if len(members) <= 8:
            print(f"    lpf={lpf:>4}: {members}{label}")
        else:
            print(f"    lpf={lpf:>4}: [{len(members)} primes] {members[:5]}...{label}")
    print()
    
    # ═══════════════════════════════════════════════════════
    # 7. FIBONACCI/LUCAS STRUCTURE IN ORDERS
    # ═══════════════════════════════════════════════════════
    print("═══ FIBONACCI/LUCAS STRUCTURE ═══")
    print()
    
    # Check which primes have ord(φ̄) that are Fibonacci or Lucas numbers
    def fib_set(limit):
        s = set()
        a, b = 1, 1
        while a <= limit:
            s.add(a)
            a, b = b, a+b
        return s
    
    def lucas_set(limit):
        s = set()
        a, b = 2, 1
        while a <= limit:
            s.add(a)
            a, b = b, a+b
        return s
    
    max_ord = max(d['ord_pbar'] for d in primes)
    fibs = fib_set(max_ord)
    lucases = lucas_set(max_ord)
    
    fib_primes = [(d['p'], d['ord_pbar']) for d in primes if d['ord_pbar'] in fibs]
    lucas_primes = [(d['p'], d['ord_pbar']) for d in primes if d['ord_pbar'] in lucases]
    
    print(f"  Primes with Fibonacci ord(φ̄): {fib_primes}")
    print(f"  Primes with Lucas ord(φ̄): {lucas_primes}")
    print()
    
    # Pisano period connection
    print("  Hosoya connection — ord(φ̄) mod 30 distribution:")
    mod30_dist = Counter(d['ord_pbar'] % 30 for d in primes)
    for r in sorted(mod30_dist.keys()):
        count = mod30_dist[r]
        bar = "█" * count
        print(f"    {r:>2} mod 30: {count:>3} {bar}")
    print()
    
    # ═══════════════════════════════════════════════════════
    # 8. DISTANCE MATRIX FOR GAUGE TRIPLET NEIGHBORHOOD
    # ═══════════════════════════════════════════════════════
    print("═══ GAUGE NEIGHBORHOOD (2-hop from any gauge prime, 3-sewn) ═══")
    print()
    
    # BFS from each gauge prime, 2 hops
    gauge_neighborhood = set()
    for gp in [229, 181, 139]:
        gauge_neighborhood.add(gp)
        for n1, s1 in adj_3.get(gp, []):
            gauge_neighborhood.add(n1)
            for n2, s2 in adj_3.get(n1, []):
                gauge_neighborhood.add(n2)
    
    print(f"  2-hop neighborhood size: {len(gauge_neighborhood)}/{len(primes)} primes")
    print(f"  Coverage: {100*len(gauge_neighborhood)/len(primes):.0f}%")
    
    # Check if the gauge neighborhood IS the full 3-sewn component
    main_3_comp = max(comps_3, key=len)
    print(f"  Main 3-sewn component: {len(main_3_comp)} primes")
    print(f"  2-hop covers {'ALL' if gauge_neighborhood >= set(main_3_comp) else 'PARTIAL'} "
          f"of main component")
    print()
    
    # ═══════════════════════════════════════════════════════
    # 9. SECURITY IMPLICATIONS
    # ═══════════════════════════════════════════════════════
    print("═══ SECURITY IMPLICATIONS ═══")
    print()
    
    # The key question: is the 3-sewn graph "small-world"?
    # If yes, any two primes are a few hops apart → harder to hide branch choice
    # If no, there are distant clusters → branch choice reveals cluster membership
    
    # BFS diameter estimation from 229
    def bfs_distances(adj, start):
        dist = {start: 0}
        queue = [start]
        i = 0
        while i < len(queue):
            node = queue[i]; i += 1
            for nbr, _ in adj.get(node, []):
                if nbr not in dist:
                    dist[nbr] = dist[node] + 1
                    queue.append(nbr)
        return dist
    
    d229 = bfs_distances(adj_3, 229)
    d181 = bfs_distances(adj_3, 181)
    d139 = bfs_distances(adj_3, 139)
    
    print(f"  Diameter from 229 (3-sewn): max={max(d229.values()) if d229 else 'N/A'}, "
          f"avg={sum(d229.values())/max(len(d229),1):.2f}")
    print(f"  Diameter from 181 (3-sewn): max={max(d181.values()) if d181 else 'N/A'}, "
          f"avg={sum(d181.values())/max(len(d181),1):.2f}")
    print(f"  Diameter from 139 (3-sewn): max={max(d139.values()) if d139 else 'N/A'}, "
          f"avg={sum(d139.values())/max(len(d139),1):.2f}")
    print()
    
    # Distance distribution
    print(f"  Distance distribution from 229:")
    dist_hist = Counter(d229.values())
    for d in sorted(dist_hist.keys()):
        bar = "█" * dist_hist[d]
        print(f"    hop {d}: {dist_hist[d]:>3} primes {bar}")
    print()
    
    print(f"  Distance 229→181: {d229.get(181, '∞')}")
    print(f"  Distance 229→139: {d229.get(139, '∞')}")
    print(f"  Distance 181→139: {d181.get(139, '∞')}")
    print()
    
    if max(d229.values(), default=0) <= 2:
        print("  ⚠ SMALL-WORLD: All primes within 2 hops of 229 in 3-sewn graph!")
        print("    → Branch choice at depth 1 already reaches most of the graph")
        print("    → Deep branches are needed for security, NOT shallow ones")
        print("    → Depth randomization is CRITICAL")
    elif max(d229.values(), default=0) >= 4:
        print("  ✓ WIDE: Graph has diameter ≥ 4 from 229")
        print("    → Distant clusters provide structural hiding")
        print("    → Branch choice reveals less at shallow depth")
    print()
    
    # 139 isolation analysis
    if 139 not in d229 or d229[139] > 2:
        print("  ✓ 139 IS TOPOLOGICALLY DISTANT from 229 in 3-sewn graph")
        print("    → The boundary channel provides genuinely independent entropy")
    else:
        print(f"  ⚠ 139 is only {d229.get(139,'∞')} hops from 229 in 3-sewn graph")
        print(f"    → But sewing dimension is only {s_229_139}")
    print()
    
    # What about 1-sewn?
    d229_1 = bfs_distances(adj_1, 229)
    print(f"  In 1-sewn (full) graph:")
    print(f"    Diameter from 229: max={max(d229_1.values()) if d229_1 else 'N/A'}, "
          f"avg={sum(d229_1.values())/max(len(d229_1),1):.2f}")
    dist_hist_1 = Counter(d229_1.values())
    for d in sorted(dist_hist_1.keys()):
        bar = "█" * dist_hist_1[d]
        print(f"    hop {d}: {dist_hist_1[d]:>3} primes {bar}")
    print()


if __name__ == "__main__":
    main()
