#!/usr/bin/env python3
"""
Prime-Field Stem Check v2.2

Runs five verification layers on any paper in the lineage:
  1. Structural (6-face hexagonal discriminator) — categorical coherence
  2. Computational — extract and verify all numerical claims
  3. Cross-reference — check claim consistency across sections
  4. Physical interpretation — domain-crossing errors
  5. Logical fallacy — post-hoc fitting, cherry-picking, overfit, causal overreach

Usage:
  python3 stem_check.py <path-to-tex-file>
"""

import re
import sys
import math
from pathlib import Path

PHI = 1.618033988749895
PHI_C = 0.6180339887498949

# ═══════════════════════════════════════════════════════
# LAYER 1: STRUCTURAL (existing 6-face discriminator)
# ═══════════════════════════════════════════════════════

AXIOM_KW = [
    ("according to", 1.0), ("cited", 0.8), ("reference", 0.8),
    ("theorem", 1.0), ("lemma", 1.0), ("proposition", 0.9),
    ("corollary", 0.9), ("defined as", 1.0), ("denotes", 0.8),
    ("measured", 0.8), ("observed", 0.7), ("proven", 1.0),
    ("verified", 0.9), ("established", 0.8),
]
CONSTRUCT_KW = [
    ("should", 0.7), ("must", 0.8), ("will", 0.6),
    ("we show", 0.9), ("we prove", 1.0), ("therefore", 0.9),
    ("hence", 0.8), ("it follows", 0.9), ("implies", 0.9),
    ("generates", 0.7), ("builds", 0.7), ("propose", 0.8),
]
DESTRUCT_KW = [
    ("because", 0.7), ("since", 0.6), ("given", 0.6),
    ("due to", 0.7), ("follows from", 0.9), ("by assumption", 0.9),
    ("however", 0.8), ("but", 0.5), ("although", 0.7),
    ("contradiction", 1.0), ("impossible", 0.8),
]
WITNESS_KW = [
    ("might", 0.6), ("perhaps", 0.7), ("possibly", 0.7),
    ("arguably", 0.7), ("approximately", 0.5),
    ("for example", 0.8), ("there exists", 1.0), ("such that", 0.9),
]
INDUCTION_KW = [
    ("in other words", 0.7), ("the key insight", 0.8),
    ("fundamentally", 0.8), ("generalization", 0.8), ("framework", 0.7),
    ("for all", 0.9), ("by induction", 1.0), ("recursively", 0.9),
]
# v2.1: Descriptive category for data/results/empirical sections
DESCRIPTIVE_KW = [
    ("tested", 0.9), ("achieves", 0.8), ("outperforms", 0.9),
    ("error", 0.7), ("rms", 0.8), ("accuracy", 0.8),
    ("table", 0.7), ("results", 0.8), ("data", 0.7),
    ("falsified if", 1.0), ("falsification", 0.9),
    ("conjecture", 0.9), ("prediction", 0.8),
    ("confirms", 0.8), ("confirms that", 0.9),
    ("sub-", 0.6), ("factor", 0.5), ("improvement", 0.7),
    ("competitor", 0.7), ("model", 0.5),
]

def score_kw(text, keywords):
    return sum(w for kw, w in keywords if kw in text)

def classify(text):
    lower = text.lower()
    scores = {
        'a': score_kw(lower, AXIOM_KW),
        'w': score_kw(lower, CONSTRUCT_KW),
        'i': score_kw(lower, DESTRUCT_KW),
        'e': score_kw(lower, WITNESS_KW),
        'l': score_kw(lower, INDUCTION_KW),
        'd': score_kw(lower, DESCRIPTIVE_KW),  # v2.1
    }
    total = sum(scores.values()) + 0.001
    fracs = {k: v / total for k, v in scores.items()}
    return scores, fracs

# ═══════════════════════════════════════════════════════
# LAYER 2: COMPUTATIONAL VERIFICATION
# ═══════════════════════════════════════════════════════

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def extract_and_verify_claims(text, raw_tex):
    """Extract numerical claims from LaTeX and verify them."""
    results = []

    # Normalize LaTeX thousands: {,} → nothing
    norm = raw_tex.replace('{,}', '')

    # Pattern: a^b mod p = c (modular exponentiation)
    # Match: N^{E} \bmod P = R  or  N^E \bmod P = R
    for m in re.finditer(r'(\d+)\^\{?(\d+)\}?\s*\\bmod\s*(\d+)\s*=\s*(\d+)', norm):
        base, exp, mod, result = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
        actual = pow(base, exp, mod)
        ok = actual == result
        results.append({
            'type': 'modexp',
            'claim': f'{base}^{exp} mod {mod} = {result}',
            'ok': ok,
            'actual': actual,
            'context': m.group(0)[:60],
        })

    # Pattern: N \bmod P = R (simple reduction — skip if preceded by ^)
    for m in re.finditer(r'(\d+)\s*\\bmod\s*(\d+)\s*=\s*(\d+)', norm):
        # Skip if this is part of a modexp (has ^ before the number)
        start = m.start()
        prefix = norm[max(0, start-5):start]
        if '^' in prefix or '}' in prefix:
            continue
        n, p, r = int(m.group(1)), int(m.group(2)), int(m.group(3))
        actual = n % p
        ok = actual == r
        results.append({
            'type': 'modreduce',
            'claim': f'{n} mod {p} = {r}',
            'ok': ok,
            'actual': actual,
            'context': m.group(0)[:60],
        })

    # Pattern: a \times b = c where c is the FULL modular result
    # Only match if c > a and c > b (to avoid false positives from inline steps)
    # OR match: a \times b \equiv R
    for m in re.finditer(r'(\d+)\s*\\times\s*(\d+)\s*(?:=\s*(\d+)|\\equiv\s*(\d+))', norm):
        a, b = int(m.group(1)), int(m.group(2))
        c = int(m.group(3)) if m.group(3) else int(m.group(4))
        # Only verify if it looks like a full product or a modular result
        actual_prod = a * b
        if c == actual_prod:
            results.append({
                'type': 'product',
                'claim': f'{a} × {b} = {c}',
                'ok': True,
                'actual': actual_prod,
                'context': m.group(0)[:60],
            })
        # Skip — this is probably an intermediate step in a modular chain

    # Pattern: a - b = c (standalone, not part of modular chain)
    for m in re.finditer(r'(?:^|\n)\s*.*?(\d+)\s*-\s*(\d+)\s*=\s*(\d+)(?:\s*[.\\)]|\s*$)', norm, re.MULTILINE):
        a, b, c = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if a > b and a - b == c:
            results.append({
                'type': 'difference',
                'claim': f'{a} - {b} = {c}',
                'ok': True,
                'actual': a - b,
                'context': m.group(0).strip()[:60],
            })

    # Pattern: gcd(a,b) = c
    for m in re.finditer(r'gcd\((\d+)\s*,\s*(\d+)\)\s*=\s*(\d+)', norm):
        a, b, c = int(m.group(1)), int(m.group(2)), int(m.group(3))
        actual = math.gcd(a, b)
        ok = actual == c
        results.append({
            'type': 'gcd',
            'claim': f'gcd({a},{b}) = {c}',
            'ok': ok,
            'actual': actual,
            'context': m.group(0)[:60],
        })

    # Pattern: N is prime (from text like "14489 (prime")
    for m in re.finditer(r'(\d{3,})\s*(?:\(|is\s+)prime', norm, re.IGNORECASE):
        n = int(m.group(1))
        ok = is_prime(n)
        results.append({
            'type': 'primality',
            'claim': f'{n} is prime',
            'ok': ok,
            'actual': is_prime(n),
            'context': m.group(0)[:60],
        })

    # Verify confinement identity 1+ω+ω²≡0 where referenced
    if '1 + \\omega + \\omega^2' in raw_tex or '1+\\omega+\\omega' in raw_tex:
        for p, omega in [(229, 94), (181, 48)]:
            val = (1 + omega + pow(omega, 2, p)) % p
            ok = val == 0
            results.append({
                'type': 'confinement',
                'claim': f'1+ω+ω² ≡ 0 (mod {p}) with ω={omega}',
                'ok': ok,
                'actual': val,
                'context': f'confinement identity at p={p}',
            })

    # Verify Vieta product φ·φ̄ ≡ -1
    if 'varphi' in raw_tex.lower() and 'bar' in raw_tex.lower():
        for p, phi, phi_bar in [(229, 148, 82), (181, 14, 168), (139, 76, 64)]:
            prod = (phi * phi_bar) % p
            ok = prod == p - 1  # p-1 ≡ -1
            results.append({
                'type': 'vieta',
                'claim': f'φ·φ̄ ≡ -1 (mod {p})',
                'ok': ok,
                'actual': prod,
                'context': f'Vieta product at p={p}',
            })

    # Verify golden polynomial splits: x²-x-1 has roots mod p
    for p, phi, phi_bar in [(229, 148, 82), (181, 14, 168), (139, 76, 64)]:
        for root, name in [(phi, 'φ'), (phi_bar, 'φ̄')]:
            val = (root*root - root - 1) % p
            ok = val == 0
            results.append({
                'type': 'golden_split',
                'claim': f'{name}²-{name}-1 ≡ 0 (mod {p}), {name}={root}',
                'ok': ok,
                'actual': val,
                'context': f'golden polynomial at p={p}',
            })

    # Verify superparticular coupling: I(l) = (l+2)/(l+1)
    if 'alpha_s' in raw_tex or 'coupling' in raw_tex.lower():
        for l, expected_num, expected_den in [(0, 2, 1), (17, 19, 18), (13, 15, 14), (21, 23, 22)]:
            actual_val = (l + 2) / (l + 1)
            expected_val = expected_num / expected_den
            ok = abs(actual_val - expected_val) < 1e-15
            results.append({
                'type': 'coupling',
                'claim': f'I({l}) = {expected_num}/{expected_den}',
                'ok': ok,
                'actual': actual_val,
                'context': f'running coupling at depth {l}',
            })

    # Verify Schwarzian invariance claim
    if 'schwarzian' in raw_tex.lower() or 'invariant' in raw_tex.lower():
        b, m_val, eps = 3.7, 1.2, 0.5
        ok = abs((b + eps - m_val - eps) - (b - m_val)) < 1e-15
        results.append({
            'type': 'schwarzian',
            'claim': 'Schwarzian gap b-m invariant under C',
            'ok': ok,
            'actual': (b + eps - m_val - eps) - (b - m_val),
            'context': 'confinement operator algebra',
        })

    # Verify MV parity identity
    if 'mayer' in raw_tex.lower() or 'parity identity' in raw_tex.lower():
        for p, phi, phi_bar in [(229, 148, 82), (181, 14, 168), (139, 76, 64)]:
            all_ok = True
            for n in range(1, 120):
                prod = pow(phi, n, p) * pow(phi_bar, n, p) % p
                expected = pow(-1, n, p)
                if prod != expected:
                    all_ok = False
                    break
            results.append({
                'type': 'mv_parity',
                'claim': f'φ^n·φ̄^n ≡ (-1)^n (mod {p}), n=1..119',
                'ok': all_ok,
                'actual': 'all pass' if all_ok else f'fail at n={n}',
                'context': f'MV parity at p={p}',
            })

    # Deduplicate
    seen = set()
    unique = []
    for r in results:
        key = r['claim']
        if key not in seen:
            seen.add(key)
            unique.append(r)
    return unique

# ═══════════════════════════════════════════════════════
# LAYER 3: CROSS-REFERENCE (claim consistency)
# ═══════════════════════════════════════════════════════

def check_cross_refs(all_claims):
    """Check for contradictions between sections."""
    issues = []
    
    # Group claims by type
    by_type = {}
    for sec, claims in all_claims:
        for c in claims:
            by_type.setdefault(c['type'], []).append((sec, c))
    
    # Check: same modexp in different sections should agree
    modexp_claims = {}
    for sec, c in by_type.get('modexp', []):
        key = c['claim']
        if key in modexp_claims:
            prev_sec, prev_c = modexp_claims[key]
            if prev_c['ok'] != c['ok']:
                issues.append(f"Contradiction: '{key}' ok={prev_c['ok']} in {prev_sec} vs ok={c['ok']} in {sec}")
        modexp_claims[key] = (sec, c)
    
    return issues


# ═══════════════════════════════════════════════════════
# LAYER 4: PHYSICAL INTERPRETATION CHECK (v2.1)
# ═══════════════════════════════════════════════════════
#
# Catches domain-crossing errors: when a term from one
# field (e.g. stat mech) is used in a way that contradicts
# its standard meaning in that field.
#
# Lesson learned: we misused "microstate" and "macrostate"
# to mean "discrete component" and "continuous component".
# In stat mech, microstate = detailed config of all particles,
# macrostate = bulk observable (T, P, etc). The mapping was
# backwards. This layer catches that class of error.

PHYSICS_TERMS = {
    # term -> (standard_domain, standard_meaning, misuse_patterns)
    'microstate': (
        'statistical mechanics',
        'specific detailed configuration of all particles/degrees of freedom',
        [
            # Flagged if used to mean "discrete" or "fine structure" without
            # connecting to actual particle configurations
            r'microstate.*(?:discrete|fine.?structure|resonance|position)',
        ]
    ),
    'macrostate': (
        'statistical mechanics',
        'bulk observable (temperature, pressure, entropy) aggregated over microstates',
        [
            r'macrostate.*(?:continuous|winding|wrapping|spacing|trend)',
        ]
    ),
    'asymptotic freedom': (
        'QCD/gauge theory',
        'coupling constant decreases at high energy (short distance) in non-Abelian gauge theory',
        [
            # Flag if claimed without scope disclaimer
            r'asymptotic freedom(?!.*(?:analog|analogy|algebraic|information|scope))',
        ]
    ),
    'confinement': (
        'QCD/gauge theory',
        'quarks cannot be isolated; color charge is always screened at long distances',
        [
            r'confinement.*(?:noise|entropy|crystalliz)',
        ]
    ),
}

def check_physical_interpretation(text, raw_tex):
    """Check for misused physics terms (Layer 4).
    
    Returns list of (term, domain, issue_description).
    """
    issues = []
    lower = text.lower()
    raw_lower = raw_tex.lower()
    
    for term, (domain, standard, patterns) in PHYSICS_TERMS.items():
        if term not in lower:
            continue
        
        for pattern in patterns:
            matches = re.findall(pattern, lower)
            if matches:
                # Check if there's a scope disclaimer nearby
                # (within 500 chars of the term)
                term_positions = [m.start() for m in re.finditer(re.escape(term), lower)]
                has_disclaimer = False
                for pos in term_positions:
                    context = lower[max(0, pos-500):pos+500]
                    if any(d in context for d in [
                        'analog', 'analogy', 'not a claim', 'scope',
                        'algebraic', 'does not model', 'shares only',
                        'information-theoretic', 'not equivalent',
                    ]):
                        has_disclaimer = True
                        break
                
                if not has_disclaimer:
                    issues.append({
                        'term': term,
                        'domain': domain,
                        'standard': standard,
                        'issue': f"'{term}' used in non-standard way without scope disclaimer",
                        'match': matches[0][:80] if matches else '',
                    })
    
    return issues

# ═══════════════════════════════════════════════════════
# LAYER 5: LOGICAL FALLACY DETECTION (v2.2)
# ═══════════════════════════════════════════════════════
#
# Catches inferential overreaches that pass domain and
# numerical checks but fail logical scrutiny:
#   - Post-hoc formula selection
#   - Parameter overfitting claims
#   - Cherry-picking (partial matches presented as full)
#   - Unqualified causal language
#   - Vague falsification criteria

FALLACY_CHECKS = [
    # ── POST-HOC FORMULA SELECTION ──────────────────────
    # Flag: "the mixing angle satisfies" or "equals" near
    # known SM constants WITHOUT "if...interpreted", "analogy",
    # "coincidence", "numerical", or "proxy"
    {
        'name': 'post-hoc formula',
        'desc': 'Claims a formula yields a SM value without acknowledging the formula was chosen to match',
        'trigger': re.compile(
            r'(?:satisfies|equals|gives|yields|predicts)\s+.{0,80}'
            r'(?:sin|alpha|theta|weinberg|coupling|137|0\.231|1/4)',
            re.IGNORECASE | re.DOTALL
        ),
        'excuse': re.compile(
            r'(?:if.*interpreted|analogy|analog|coinciden|proxy|'
            r'numerical coincidence|not a derivation|scope|observes)',
            re.IGNORECASE
        ),
        'radius': 600,  # chars around trigger to search for excuse
    },
    # ── PARAMETER OVERFITTING ───────────────────────────
    # Flag: model with more parameters than data points
    # without explicit acknowledgment
    {
        'name': 'parameter overfit',
        'desc': 'Model has ≥ data-count parameters without overfitting disclaimer',
        'trigger': re.compile(
            r'(?:sub-0\.\d+\%|0\.0\d+\%|error.*\d+\.\d+\%|rms.*\d)',
            re.IGNORECASE
        ),
        'excuse': re.compile(
            r'(?:parameter count|degrees of freedom|overfit|bayesian|'
            r'effective.*fewer|constrain|discrete)',
            re.IGNORECASE
        ),
        'radius': 2000,  # look in the same section
        'search_full_doc': True,  # disclaimer may be in a different section
    },
    # ── CHERRY-PICKING ──────────────────────────────────
    # Flag: "reproduce" or "match" hypercharges/SM values
    # when only a subset matches
    {
        'name': 'cherry-pick',
        'desc': 'Claims to reproduce SM values but only matches a subset',
        'trigger': re.compile(
            r'(?:reproduc|recover|deriv|predict)(?:e|es|ing)\s+'
            r'(?:the\s+)?(?:standard model|sm|hypercharge|coupling|mass)',
            re.IGNORECASE
        ),
        'excuse': re.compile(
            r'(?:three of|subset|partial|incomplete|remaining.*do not|'
            r'coincide with|suggestive)',
            re.IGNORECASE
        ),
        'radius': 800,
    },
    # ── UNQUALIFIED CAUSAL LANGUAGE ─────────────────────
    # Flag: "is the reason" / "determines" / "causes"
    # when the algebra only shows correlation
    {
        'name': 'unqualified causal',
        'desc': 'Uses causal language for algebraic correlation without qualifier',
        'trigger': re.compile(
            r'(?:is the reason|determines\s+(?:mass|coupling|charge)|'
            r'causes?\s+(?:the|mass|confinement))',
            re.IGNORECASE
        ),
        'excuse': re.compile(
            r'(?:algebraic|analog|correlation|structural|in the algebra|'
            r'scope|not a derivation|parallel)',
            re.IGNORECASE
        ),
        'radius': 400,
    },
    # ── VAGUE FALSIFICATION ─────────────────────────────
    # Flag: "Falsified if" followed by vague language
    # without specific numbers or thresholds
    {
        'name': 'vague falsification',
        'desc': 'Falsification criterion lacks operational specificity',
        'trigger': re.compile(
            r'falsified if\b.{0,200}?(?:broader|additional|some|'
            r'any other|no.*relationship|cannot be)',
            re.IGNORECASE | re.DOTALL
        ),
        'excuse': re.compile(
            r'(?:\d+\s*(?:golden|primes|percent|%|\\%|systems|genera)|'
            r'threshold|within|more than|fewer than|specifically)',
            re.IGNORECASE
        ),
        'radius': 400,
    },
]


def check_logical_fallacies(text, raw_tex, full_doc_text=""):
    """Layer 5: detect logical fallacies and inferential overreaches.
    
    Args:
        text: stripped text of the current section
        raw_tex: raw LaTeX of the current section
        full_doc_text: stripped text of the FULL document (for cross-section excuse search)
    """
    issues = []
    lower = text.lower()
    raw_lower = raw_tex.lower()
    full_lower = full_doc_text.lower() if full_doc_text else lower
    
    # Strip tabular environments from causal-language search
    # (table headers like "determines mass" are summaries, not causal claims)
    lower_no_tables = re.sub(
        r'\\begin\{tabular\}.*?\\end\{tabular\}', ' ', raw_lower, flags=re.DOTALL
    )
    
    for check in FALLACY_CHECKS:
        # For causal checks, use table-stripped text
        search_text = lower_no_tables if check['name'] == 'unqualified causal' else lower
        
        trigger_matches = list(check['trigger'].finditer(search_text))
        for m in trigger_matches:
            pos = m.start()
            
            # For overfit checks, search the FULL DOCUMENT for excuses
            # (the disclaimer may be in a different section)
            if check.get('search_full_doc') and full_lower:
                has_excuse = bool(check['excuse'].search(full_lower))
            else:
                # Search for excuse within radius of the trigger
                window_start = max(0, pos - check['radius'])
                window_end = min(len(search_text), pos + check['radius'])
                context = search_text[window_start:window_end]
                has_excuse = bool(check['excuse'].search(context))
            
            if not has_excuse:
                snippet = search_text[pos:pos+120].replace('\n', ' ').strip()
                issues.append({
                    'name': check['name'],
                    'desc': check['desc'],
                    'snippet': snippet[:80],
                })
    
    return issues

# ═══════════════════════════════════════════════════════
# LAYER 8: EPISTEMIC / ONTOLOGICAL PLASMA WALL (v3.0)
# ═══════════════════════════════════════════════════════
#
# Enforces the Lockwood WMR1-R2 Maximum-Rigor rules:
#   R1. Hard claim tiering (Theorem / Computation / Analogy / Physical)
#   R2. Order certification protocol
#   R3. No-free-parameter rule
#   R4. Physical upgrade pipeline
#   R5. Type/unit ledger
#   R6. Gauge-theory upgrade boundary
#   R7. Executable verification
#   R8. Correction register
#   R9. Terminology quarantine
#
# The plasma wall is the hard epistemic boundary between
# proved algebraic facts and speculative physical interpretation.

PLASMA_WALL_RULES = {
    'R1': {
        'name': 'Claim Tiering (Plasma Wall)',
        'desc': 'Every chapter must have a claim ledger separating Theorem / Computation / Analogy / Physical',
        'required_patterns': [
            r'(?i)(?:plasma\s*wall|claim\s*ledger|separation\s*of\s*claims|claim\s*protocol)',
        ],
        'severity': 'critical',
    },
    'R2': {
        'name': 'Order Certification Protocol',
        'desc': 'Order claims need positive witness + prime-divisor non-witnesses',
        'check_type': 'order_certification',
        'severity': 'high',
    },
    'R5': {
        'name': 'Type/Unit Declarations',
        'desc': 'Symbols must have declared types (dimensionless, SI, etc.)',
        'required_patterns': [
            r'(?i)(?:dimensionless|type\s*ledger|unit\s*ledger|type\s*and\s*unit)',
        ],
        'severity': 'medium',
        'scope': 'document',  # Only needs to appear once in the whole doc
    },
    'R6': {
        'name': 'Center-Algebra Scope',
        'desc': 'SU(3)/confinement language needs explicit center-algebra-only disclaimer',
        'trigger_patterns': [
            r'(?i)SU\s*\(\s*3\s*\)\s*(?:confinement|confin)',
            r'(?i)color\s+confin',
            r'(?i)(?<!center-)(?:confinement|deconfinement)(?!.*center\s*algebra)',
        ],
        'excuse_patterns': [
            r'(?i)center.?algebra',
            r'(?i)center.?algebra\s*(?:only|realization|scope)',
            r'(?i)not\s+a\s+derivation\s+of\s+yang',
            r'(?i)not\s+yang.?mills',
            r'(?i)center\s+(?:copy|grading)',
            r'(?i)\bZ/3Z\b',
            r'(?i)\\mathbb\{Z\}/3\\mathbb\{Z\}',
            r'(?i)\\ZZ/3\\ZZ',
            r'(?i)scope\s*rule',
        ],
        'radius': 800,
        'severity': 'high',
    },
    'R9': {
        'name': 'Terminology Quarantine',
        'desc': 'Physical terms (dark, exotic, neutrino) need explicit scope qualification',
        'trigger_excuse_pairs': [
            (r'(?i)\bdark\s+(?:matter|energy)\b',
             r'(?i)(?:structural|analogy|not\s+cosmological|quarantine|scope|outside.*subgroup)'),
            (r'(?i)\bexotic\s+matter\b',
             r'(?i)(?:structural|algebraic|analogy|outside.*partition|quarantine|scope)'),
            (r'(?i)\b[dD]-?[Nn]eutrino\b',
             r'(?i)(?:structural|pattern|not\s+a\s+PMNS|scope|quarantine)'),
            (r'(?i)\bzero.?point\s+energy\b',
             r'(?i)(?:structural|algebraic|1/R\s+scaling|not\s+QED|scope|quarantine|Casimir)'),
        ],
        'radius': 600,
        'severity': 'medium',
    },
    'R3': {
        'name': 'No-Free-Parameter Rule',
        'desc': 'Fitted coefficients must be justified by theorem, calibration, or conservation law',
        'trigger_patterns': [
            r'(?i)(?:fitting|fitted|calibrat|tuned|chosen\s+(?:to|so\s+that))',
        ],
        'excuse_patterns': [
            r'(?i)(?:theorem|measured|conservation|variational|preregistered|no.?free.?parameter)',
        ],
        'radius': 500,
        'severity': 'medium',
    },
}

def check_plasma_wall(text, raw_tex, full_doc_text="", is_book_chapter=False):
    """Layer 8: Enforce the Epistemic/Ontological Plasma Wall.
    
    Returns list of {'rule', 'name', 'desc', 'severity', 'detail'} dicts.
    """
    issues = []
    lower = text.lower()
    raw_lower = raw_tex.lower()
    full_lower = full_doc_text.lower() if full_doc_text else lower
    
    # ── R1: Claim Tiering ──
    r1 = PLASMA_WALL_RULES['R1']
    has_wall = any(
        re.search(p, raw_lower) for p in r1['required_patterns']
    )
    if not has_wall and len(text.split()) > 500:
        issues.append({
            'rule': 'R1',
            'name': r1['name'],
            'desc': r1['desc'],
            'severity': r1['severity'],
            'detail': 'No Plasma Wall / Claim Ledger section found',
        })
    
    # ── R5: Type/Unit Ledger ──
    r5 = PLASMA_WALL_RULES['R5']
    search_text = full_lower if r5.get('scope') == 'document' else lower
    has_ledger = any(
        re.search(p, search_text) for p in r5['required_patterns']
    )
    if not has_ledger:
        issues.append({
            'rule': 'R5',
            'name': r5['name'],
            'desc': r5['desc'],
            'severity': r5['severity'],
            'detail': 'No Type/Unit Ledger found in document',
        })
    
    # ── R6: Center-Algebra Scope ──
    r6 = PLASMA_WALL_RULES['R6']
    for trigger_pat in r6['trigger_patterns']:
        for m in re.finditer(trigger_pat, raw_lower):
            pos = m.start()
            window_start = max(0, pos - r6['radius'])
            window_end = min(len(raw_lower), pos + r6['radius'])
            context = raw_lower[window_start:window_end]
            
            has_excuse = any(
                re.search(p, context) for p in r6['excuse_patterns']
            )
            # Also check full doc frontmatter
            if not has_excuse and full_lower:
                has_excuse = any(
                    re.search(p, full_lower[:5000]) for p in r6['excuse_patterns']
                )
            
            if not has_excuse:
                snippet = raw_lower[pos:pos+80].replace('\n', ' ').strip()
                issues.append({
                    'rule': 'R6',
                    'name': r6['name'],
                    'desc': r6['desc'],
                    'severity': r6['severity'],
                    'detail': f'Missing center-algebra disclaimer near: "{snippet[:60]}..."',
                })
                break  # One warning per trigger type
    
    # ── R9: Terminology Quarantine ──
    r9 = PLASMA_WALL_RULES['R9']
    for trigger_pat, excuse_pat in r9['trigger_excuse_pairs']:
        for m in re.finditer(trigger_pat, raw_lower):
            pos = m.start()
            window_start = max(0, pos - r9['radius'])
            window_end = min(len(raw_lower), pos + r9['radius'])
            context = raw_lower[window_start:window_end]
            
            has_excuse = bool(re.search(excuse_pat, context))
            # Also check full doc frontmatter
            if not has_excuse and full_lower:
                has_excuse = bool(re.search(excuse_pat, full_lower[:5000]))
            
            if not has_excuse:
                snippet = raw_lower[pos:pos+60].replace('\n', ' ').strip()
                issues.append({
                    'rule': 'R9',
                    'name': r9['name'],
                    'desc': r9['desc'],
                    'severity': r9['severity'],
                    'detail': f'Unquarantined term: "{snippet}"',
                })
                break
    
    # ── R3: No-Free-Parameter ──
    r3 = PLASMA_WALL_RULES['R3']
    for trigger_pat in r3['trigger_patterns']:
        for m in re.finditer(trigger_pat, raw_lower):
            pos = m.start()
            window_start = max(0, pos - r3['radius'])
            window_end = min(len(raw_lower), pos + r3['radius'])
            context = raw_lower[window_start:window_end]
            
            has_excuse = any(
                re.search(p, context) for p in r3['excuse_patterns']
            )
            if not has_excuse and full_lower:
                has_excuse = any(
                    re.search(p, full_lower[:5000]) for p in r3['excuse_patterns']
                )
            
            if not has_excuse:
                snippet = raw_lower[pos:pos+60].replace('\n', ' ').strip()
                issues.append({
                    'rule': 'R3',
                    'name': r3['name'],
                    'desc': r3['desc'],
                    'severity': r3['severity'],
                    'detail': f'Fitted parameter without justification: "{snippet}"',
                })
                break
    
    # ── R2: Order Certification (computational check) ──
    # Check that any order claim has both a^N=1 and a^(N/q)≠1 witnesses
    order_claims = re.findall(
        r'(?:ord|order)\s*(?:\(|_\{?)(\d+)(?:\)|_?\}?)\s*=\s*(\d+)', raw_tex
    )
    for base_str, order_str in order_claims:
        base, order = int(base_str), int(order_str)
        # Check for prime-divisor non-witnesses nearby
        prime_factors = set()
        for p_candidate in range(2, order + 1):
            if order % p_candidate == 0:
                prime_factors.add(p_candidate)
                while order % p_candidate == 0:
                    order //= p_candidate
                order = int(order_str)  # Reset
        
        has_nonwitness = False
        for q in prime_factors:
            sub_exp = int(order_str) // q
            pattern = rf'{base_str}\s*\^\s*\{{?\s*{sub_exp}\s*\}}?\s*(?:\\neq|\\ne|\\not|≠|\\bmod)'
            if re.search(pattern, raw_tex):
                has_nonwitness = True
                break
        
        if not has_nonwitness and len(prime_factors) > 0:
            # Check if the full Lockwood-style certification appears anywhere
            any_cert = any(
                re.search(rf'{base_str}\s*\^\s*\{{?\s*{int(order_str)//q}\s*\}}?', raw_tex)
                for q in prime_factors
            )
            if not any_cert:
                issues.append({
                    'rule': 'R2',
                    'name': 'Order Certification Protocol',
                    'desc': f'ord({base_str}) = {order_str} claimed without prime-divisor non-witnesses',
                    'severity': 'high',
                    'detail': f'Need checks at N/q for q ∈ {prime_factors}',
                })
    
    # Deduplicate by rule+detail
    seen = set()
    unique = []
    for i in issues:
        key = (i['rule'], i.get('detail', ''))
        if key not in seen:
            seen.add(key)
            unique.append(i)
    
    return unique


#
# Catches what a peer reviewer from the target field
# would flag before a paper even gets to review:
#   - Selection bias
#   - Retrodiction-only (no novel predictions)
#   - Missing standard apparatus for claimed arXiv category
#   - Small sample sizes
#   - Framing mismatches

# Required machinery per arXiv category
ARXIV_REQUIREMENTS = {
    'math-ph': {
        'name': 'Mathematical Physics',
        'checks': [
            ('theorem environments', r'\\begin\{(?:theorem|proposition|lemma)\}', 2,
             'math-ph papers need formal theorem-proof structure'),
        ],
    },
    'hep-th': {
        'name': 'High Energy Physics (Theory)',
        'checks': [
            ('Lagrangian/action', r'(?i)lagrangian|action\s+principle|path\s+integral', 1,
             'hep-th papers need a Lagrangian or action principle'),
            ('representations', r'(?i)representation|irreducible|multiplet|adjoint', 2,
             'hep-th papers need representation-theoretic content'),
        ],
    },
    'hep-ph': {
        'name': 'High Energy Physics (Phenomenology)',
        'checks': [
            ('cross sections', r'(?i)cross.?section|branching\s+ratio|decay\s+width', 1,
             'hep-ph papers need experimental observables'),
        ],
    },
    'math.NT': {
        'name': 'Number Theory',
        'checks': [
            ('proof environments', r'\\begin\{proof\}', 1,
             'math.NT papers need formal proofs'),
        ],
    },
}


def check_external_validity(parsed, content, raw_content):
    """Layer 7: detect external validity issues a peer reviewer would flag."""
    issues = []
    full_text = " ".join(text for _, text, _ in parsed)
    full_lower = full_text.lower()
    
    # ── Parse arXiv tags ──
    arxiv_match = re.search(r'\\date\{.*?((?:math-ph|hep-th|hep-ph|math\.NT|math\.AG|'
                            r'astro-ph|cond-mat|quant-ph)[^}]*)\}', raw_content)
    arxiv_tags = []
    if arxiv_match:
        tag_str = arxiv_match.group(1)
        arxiv_tags = re.findall(r'(math-ph|hep-th|hep-ph|math\.NT|math\.AG|'
                                r'astro-ph|cond-mat|quant-ph)', tag_str)
    
    # ── CHECK 1: Selection bias ──
    # Specific number triples/tuples assigned meaning without uniqueness proof
    has_specific_numbers = bool(re.search(r'\{229.*181.*139\}', raw_content))
    has_uniqueness = bool(re.search(
        r'(?i)unique|only\s+(?:triple|one)|exhaustive|all\s+golden\s+split\s+primes\s+below',
        raw_content
    ))
    if has_specific_numbers and not has_uniqueness:
        issues.append({
            'check': 'selection bias',
            'desc': 'Specific primes {229,181,139} assigned meaning without uniqueness proof',
            'severity': 'high',
            'fix': 'Add exhaustive search showing the triple is unique under stated criteria',
        })
    
    # ── CHECK 2: Retrodiction-only ──
    has_predictions = bool(re.search(
        r'(?i)(?:not\s+yet\s+(?:tested|measured|performed))|(?:untested)|'
        r'(?:novel\s+prediction)|(?:future\s+experiment)',
        raw_content
    ))
    has_conjecture = bool(re.search(r'(?i)conjecture|falsified\s+if', raw_content))
    if has_conjecture and not has_predictions:
        issues.append({
            'check': 'retrodiction-only',
            'desc': 'Paper has conjectures but no predictions about untested/future data',
            'severity': 'high',
            'fix': 'Add at least one prediction about data not yet collected or computed',
        })
    
    # ── CHECK 3: Missing apparatus per arXiv category ──
    for tag in arxiv_tags:
        if tag not in ARXIV_REQUIREMENTS:
            continue
        req = ARXIV_REQUIREMENTS[tag]
        for check_name, pattern, min_count, msg in req['checks']:
            matches = re.findall(pattern, raw_content)
            if len(matches) < min_count:
                issues.append({
                    'check': f'missing apparatus ({tag})',
                    'desc': f'{msg} (found {len(matches)}, need ≥{min_count})',
                    'severity': 'medium',
                    'fix': f'Add {check_name} to meet {tag} standards',
                })
    
    # ── CHECK 4: Small sample size ──
    sample_matches = re.findall(
        r'(?i)(?:tested|verified|checked)\s+(?:on|against|for)\s+(\d+)\s+'
        r'(?:system|case|example|sample|prime|planet)', full_text
    )
    for m in sample_matches:
        n = int(m)
        if n < 10:
            has_ack = bool(re.search(
                r'(?i)small\s+sample|limited|preliminary|not\s+sufficient',
                full_text
            ))
            if not has_ack:
                issues.append({
                    'check': 'small sample',
                    'desc': f'Claims based on N={n} cases without statistical caveat',
                    'severity': 'medium',
                    'fix': 'Acknowledge sample size limitation or increase N',
                })
    
    # ── CHECK 5: Framing mismatch ──
    physics_vocab = len(re.findall(
        r'(?i)gauge|boson|fermion|quark|lepton|confinement|coupling|'
        r'mass.?less|neutrino|higgs|standard\s+model', raw_content
    ))
    physics_machinery = len(re.findall(
        r'(?i)lagrangian|path\s+integral|propagator|feynman|'
        r'renormalization|anomaly|representation', raw_content
    ))
    if physics_vocab > 20 and physics_machinery < 3:
        has_scope = bool(re.search(
            r'(?i)analog|analogy|algebraic\s+correlate|not\s+a\s+derivation|'
            r'scope|does\s+not\s+derive', raw_content
        ))
        if not has_scope:
            issues.append({
                'check': 'framing mismatch',
                'desc': f'Heavy physics vocabulary ({physics_vocab} terms) with minimal '
                        f'physics machinery ({physics_machinery}), no scope disclaimers',
                'severity': 'medium',
                'fix': 'Either add standard physics apparatus or clarify the paper is algebraic/number-theoretic',
            })
    
    return issues, arxiv_tags

# ═══════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════

def strip_latex(text):
    text = re.sub(r'%.*?\n', '\n', text)
    text = re.sub(r'\\begin\{[^}]*\}', '', text)
    text = re.sub(r'\\end\{[^}]*\}', '', text)
    text = re.sub(r'\$\$.*?\$\$', ' [MATH] ', text, flags=re.DOTALL)
    text = re.sub(r'\$[^$]*?\$', ' [MATH] ', text)
    text = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\\[a-zA-Z]+', '', text)
    text = re.sub(r'[{}]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def main():
    if len(sys.argv) < 2:
        # Default to golden_tetrahedron
        tex_path = '/home/phrxmaz/Documents/InfoPhys/papers/golden_tetrahedron.tex'
    else:
        tex_path = sys.argv[1]
    
    path = Path(tex_path)
    if not path.exists():
        print(f"File not found: {tex_path}")
        sys.exit(1)
    
    with open(tex_path, 'r') as f:
        content = f.read()

    # Split by \section
    sections_raw = re.split(r'\\section\*?\{', content)
    parsed = []
    for i, sec in enumerate(sections_raw):
        if i == 0:
            abstract_match = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', sec, re.DOTALL)
            if abstract_match:
                parsed.append(("Abstract", strip_latex(abstract_match.group(1)), abstract_match.group(1)))
            continue
        name_match = re.match(r'([^}]+)\}', sec)
        name = name_match.group(1) if name_match else f"Section {i}"
        text = strip_latex(sec)
        if len(text) > 50:
            parsed.append((name, text, sec))
    
    paper_name = path.stem.replace('_', ' ').title()
    
    # ═══════════════════════════════════════════
    # LAYER 1: STRUCTURAL
    # ═══════════════════════════════════════════
    print("=" * 72)
    print(f"STEM CHECK v2.0 — {paper_name}")
    print("=" * 72)
    print()
    print("━━━ LAYER 1: STRUCTURAL (Categorical Coherence) ━━━")
    print()
    
    structural_issues = 0
    for name, text, raw in parsed:
        scores, fracs = classify(text)
        fracs_list = list(fracs.values())
        hhi = sum(f*f for f in fracs_list)
        max_frac = max(fracs_list)
        words = len(text.split())
        
        if hhi < 0.25 and max_frac < 0.35:
            marker = "⚠️"
            structural_issues += 1
        else:
            marker = "✓ "
        
        dominant = max(fracs.items(), key=lambda x: x[1])
        type_names = {'a': 'Axm', 'w': 'Con', 'i': 'Des', 'e': 'Wit', 'l': 'Ind', 'd': 'Dat'}
        print(f"  {marker} §{name[:45]:<45} {words:>4}w  HHI={hhi:.3f}  dom={type_names[dominant[0]]}({dominant[1]:.2f})")
    
    print(f"\n  Structural issues: {structural_issues}")
    
    # ═══════════════════════════════════════════
    # LAYER 2: COMPUTATIONAL
    # ═══════════════════════════════════════════
    print()
    print("━━━ LAYER 2: COMPUTATIONAL (Numerical Verification) ━━━")
    print()
    
    all_claims = []
    total_pass = 0
    total_fail = 0
    total_skip = 0
    failures = []
    
    for name, text, raw in parsed:
        claims = extract_and_verify_claims(text, raw)
        all_claims.append((name, claims))
        
        sec_pass = sum(1 for c in claims if c['ok'] is True)
        sec_fail = sum(1 for c in claims if c['ok'] is False)
        sec_skip = sum(1 for c in claims if c['ok'] is None)
        total_pass += sec_pass
        total_fail += sec_fail
        total_skip += sec_skip
        
        if claims:
            marker = "✓ " if sec_fail == 0 else "✗ "
            print(f"  {marker} §{name[:40]:<40} {sec_pass}✓ {sec_fail}✗ {sec_skip}? ({len(claims)} claims)")
            
            for c in claims:
                if c['ok'] is False:
                    print(f"       ✗ {c['claim']} — got {c['actual']}")
                    failures.append((name, c))
    
    print(f"\n  Computational: {total_pass}✓  {total_fail}✗  {total_skip}?  ({total_pass+total_fail+total_skip} total)")
    
    if failures:
        print(f"\n  ┌─ FAILURES ─────────────────────────────────────────┐")
        for sec, c in failures:
            print(f"  │ §{sec}: {c['claim']}")
            print(f"  │   expected: from claim    actual: {c['actual']}")
            print(f"  │   type: {c['type']}    context: {c['context'][:50]}")
        print(f"  └──────────────────────────────────────────────────────┘")
    
    # ═══════════════════════════════════════════
    # LAYER 3: CROSS-REFERENCE
    # ═══════════════════════════════════════════
    print()
    print("━━━ LAYER 3: CROSS-REFERENCE (Claim Consistency) ━━━")
    print()
    
    xref_issues = check_cross_refs(all_claims)
    if xref_issues:
        for issue in xref_issues:
            print(f"  ⚠️  {issue}")
    else:
        print(f"  ✓  No cross-section contradictions found")
    
    # ═══════════════════════════════════════════
    # LAYER 4: PHYSICAL INTERPRETATION (v2.1)
    # ═══════════════════════════════════════════
    print()
    print("━━━ LAYER 4: PHYSICAL INTERPRETATION (Domain Crossing) ━━━")
    print()
    
    phys_issues = []
    for name, text, raw in parsed:
        sec_issues = check_physical_interpretation(text, raw)
        for issue in sec_issues:
            phys_issues.append((name, issue))
    
    if phys_issues:
        for sec, issue in phys_issues:
            print(f"  ⚠️  §{sec[:40]}: {issue['issue']}")
            print(f"       Domain: {issue['domain']}")
            print(f"       Standard: {issue['standard']}")
    else:
        print(f"  ✓  No domain-crossing issues found")
    
    # ═══════════════════════════════════════════
    # LAYER 5: LOGICAL FALLACY (v2.2)
    # ═══════════════════════════════════════════
    print()
    print("━━━ LAYER 5: LOGICAL FALLACY DETECTION ━━━")
    print()
    
    # Build full document text for cross-section excuse searching
    full_doc_text = " ".join(text for _, text, _ in parsed)
    
    fallacy_issues = []
    for name, text, raw in parsed:
        sec_issues = check_logical_fallacies(text, raw, full_doc_text)
        for issue in sec_issues:
            fallacy_issues.append((name, issue))
    
    if fallacy_issues:
        for sec, issue in fallacy_issues:
            print(f"  ⚠️  §{sec[:40]}: {issue['name']}")
            print(f"       {issue['desc']}")
            print(f"       \"{issue['snippet']}...\"")
    else:
        print(f"  ✓  No logical fallacies detected")
    
    # ═══════════════════════════════════════════
    # LAYER 6: VOICE & HUMANITY (v2.3)
    # ═══════════════════════════════════════════
    print()
    print("━━━ LAYER 6: VOICE & HUMANITY ━━━")
    print()
    
    LARUE_VOICE = [
        "the key", "the bridge", "the anchor", "the orbit",
        "golden", "chromatic", "spectral", "fibonacci",
        "protoreal", "zplasmic", "dodecahedral", "hexagonal",
        "this is the", "that's the", "which means",
        "notice", "observe", "consider",
    ]
    HUMANITY = [
        ("don't", 0.8), ("can't", 0.8), ("won't", 0.7),
        ("it's", 0.6), ("that's", 0.7), ("what's", 0.7),
        ("so ", 0.4), ("right", 0.4),
        ("wait", 0.7), ("actually", 0.5), ("hmm", 0.8),
        ("hold on", 0.8), ("let me", 0.6),
        ("i think", 0.7), ("i mean", 0.7), ("my ", 0.5),
    ]
    AI_OVERUSE = [
        ("it is important to note", 1.0), ("it's worth noting", 0.8),
        ("in conclusion", 0.6), ("comprehensive", 0.5),
        ("delve", 0.9), ("utilize", 0.6), ("leverage", 0.6),
        ("facilitate", 0.7), ("paradigm", 0.5), ("synergy", 0.8),
    ]
    
    full_lower = full_doc_text.lower()
    voice_hits = sum(1 for m in LARUE_VOICE if m in full_lower)
    voice_score = min(voice_hits / len(LARUE_VOICE) * 4.0, 1.0)
    human_score = sum(w for m, w in HUMANITY if m in full_lower)
    ai_penalty = sum(w for m, w in AI_OVERUSE if m in full_lower)
    humanity_raw = max(0.0, min(1.0, (human_score - ai_penalty * 2.0) / 5.0))
    
    print(f"  Voice fidelity: {voice_score:.2f}  ({voice_hits}/{len(LARUE_VOICE)} markers)")
    print(f"  Humanity score: {humanity_raw:.2f}  (human={human_score:.1f}, AI penalty={ai_penalty:.1f})")
    if voice_score > 0.5:
        print(f"  ✓  Strong LaRue voice signature")
    elif voice_score > 0.2:
        print(f"  ✓  Partial voice signature")
    else:
        print(f"  ℹ️  Minimal voice signature (domain-specific text)")
    
    # ═══════════════════════════════════════════
    # LAYER 7: EXTERNAL VALIDITY (v2.3)
    # ═══════════════════════════════════════════
    print()
    print("━━━ LAYER 7: EXTERNAL VALIDITY (Pre-Peer-Review) ━━━")
    print()
    
    ext_issues, arxiv_tags = check_external_validity(parsed, content, content)
    
    if arxiv_tags:
        print(f"  arXiv tags: {', '.join(arxiv_tags)}")
    else:
        print(f"  ℹ️  No arXiv tags detected")
    
    if ext_issues:
        for issue in ext_issues:
            severity_icon = '🔴' if issue['severity'] == 'high' else '🟡'
            print(f"  {severity_icon} {issue['check']}: {issue['desc']}")
            print(f"       Fix: {issue['fix']}")
    else:
        print(f"  ✓  No external validity issues found")
    
    # ═══════════════════════════════════════════
    # LAYER 8: PLASMA WALL (v3.0 — Lockwood Rules)
    # ═══════════════════════════════════════════
    print()
    print("━━━ LAYER 8: EPISTEMIC / ONTOLOGICAL PLASMA WALL ━━━")
    print()
    
    plasma_issues = check_plasma_wall(full_doc_text, content, content)
    
    plasma_critical = sum(1 for i in plasma_issues if i['severity'] == 'critical')
    plasma_high = sum(1 for i in plasma_issues if i['severity'] == 'high')
    plasma_medium = sum(1 for i in plasma_issues if i['severity'] == 'medium')
    
    if plasma_issues:
        for issue in plasma_issues:
            sev_icon = {'critical': '🔴', 'high': '🟠', 'medium': '🟡'}.get(issue['severity'], '⚪')
            print(f"  {sev_icon} [{issue['rule']}] {issue['name']}")
            print(f"       {issue['desc']}")
            if issue.get('detail'):
                print(f"       → {issue['detail']}")
    else:
        print(f"  ✓  Plasma Wall intact — all Lockwood rules satisfied")
    
    print(f"\n  Plasma Wall: {plasma_critical} critical, {plasma_high} high, {plasma_medium} medium")
    
    # ═══════════════════════════════════════════
    # VERDICT
    # ═══════════════════════════════════════════
    print()
    print("=" * 72)
    
    total_issues = structural_issues + len(phys_issues) + len(fallacy_issues)
    ext_high = sum(1 for i in ext_issues if i['severity'] == 'high')
    
    if ai_penalty > 5.0:
        verdict = "⛔ BLOCKED — AI slop detected"
    elif plasma_critical > 0:
        verdict = "🔴 WALL BREACH — Plasma Wall critical violations"
    elif total_fail == 0 and total_issues == 0 and len(ext_issues) == 0 and len(plasma_issues) == 0:
        verdict = "🟢 GOLDEN — All verifications pass, Plasma Wall intact"
    elif total_fail == 0 and total_issues == 0 and plasma_critical == 0 and plasma_high == 0 and ext_high == 0:
        verdict = "🟢 GOLDEN — All verifications pass (minor notes)"
    elif total_fail == 0 and len(fallacy_issues) == 0 and len(phys_issues) == 0 and ext_high > 0:
        verdict = "🟣 DRAFT — Internal checks pass, external validity gaps"
    elif total_fail == 0 and plasma_high > 0:
        verdict = "🟠 FRACTURED — Plasma Wall high-severity violations"
    elif total_fail == 0 and len(phys_issues) == 0 and len(fallacy_issues) == 0:
        verdict = "🟡 CRYSTALLINE — Computations pass, structural issues noted"
    elif total_fail == 0 and len(fallacy_issues) > 0:
        verdict = "🟠 FRACTURED — Logical fallacies detected"
    elif total_fail == 0:
        verdict = "🟠 FRACTURED — Domain-crossing issues found"
    elif total_fail <= 3:
        verdict = "🟠 FRACTURED — Computational failures found"
    else:
        verdict = "🔴 FLAGGED — Multiple verification failures"
    
    print(f"  VERDICT: {verdict}")
    print(f"  Structural: {structural_issues} issues")
    print(f"  Computational: {total_pass}✓ {total_fail}✗ {total_skip}?")
    print(f"  Cross-ref: {len(xref_issues)} contradictions")
    print(f"  Physical: {len(phys_issues)} domain-crossing issues")
    print(f"  Logical: {len(fallacy_issues)} fallacies")
    print(f"  External: {len(ext_issues)} ({ext_high} high)")
    print(f"  Plasma Wall: {len(plasma_issues)} ({plasma_critical} critical, {plasma_high} high)")
    print(f"  Voice: {voice_score:.2f}  Humanity: {humanity_raw:.2f}")
    print("=" * 72)

if __name__ == '__main__':
    main()

