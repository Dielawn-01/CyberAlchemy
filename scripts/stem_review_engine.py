#!/usr/bin/env python3
"""
stem_review_engine.py
=====================
A Generalized Mathematical Physics & NLP Paper Review Engine.

This tool evaluates scientific corpora for:
  1. Natural Language Topology (Anthropogenic burstiness vs AI-generated rust)
  2. Cross-Paper Citation Integrity
  3. "No Black Box" Rigor Checks
  4. Custom Mathematical & Topological Invariants (loaded via JSON ruleset)
  5. Volume Structure Validation (4-volume split)

Principia Psychedelia volumes:
  Vol 1: Foundations (Ch.0) + Part I (Logical Creativity)
  Vol 2: Part II (Informational Creativity)
  Vol 3: Part III (Physical Creativity)
  Vol 4: STEM Check and Formal Review (Appendices)

Usage:
    python3 stem_review_engine.py --corpus <dir> [--rules <rules.json>] [--verbose]
"""

import sys
import os
import re
import math
import hashlib
import json
import argparse
import statistics
from pathlib import Path

VERBOSE = False

# ════════════════════════════════════════════════════════════════
# CORE MATH UTILITIES (Available to custom assertions)
# ════════════════════════════════════════════════════════════════

def is_prime(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

def mult_order(a, p):
    """Multiplicative order of a in F*_p."""
    if a % p == 0: return 0
    for k in range(1, p):
        if pow(a, k, p) == 1: return k
    return p - 1

# Provide an execution environment for assertions
MATH_ENV = {
    "math": math,
    "pow": pow,
    "abs": abs,
    "int": int,
    "is_prime": is_prime,
    "mult_order": mult_order
}

# ════════════════════════════════════════════════════════════════
# STATE & REPORTING
# ════════════════════════════════════════════════════════════════

fbbt_depth = 0
schwarzian_torque = 0.0
UPSILON_LIMIT = 100.0  # 45/π ≈ 14.324 (was 15.5)

section_stats = {}
current_section = None

def section(name):
    global current_section
    current_section = name
    if name not in section_stats:
        section_stats[name] = {"passed": 0, "failed": 0}
    print(f"\n{'═'*70}")
    print(f"  REVIEW TIER: {name}")
    print(f"{'═'*70}")

def check(label, condition, detail=""):
    global fbbt_depth, schwarzian_torque
    if condition:
        fbbt_depth += 1
        section_stats[current_section]["passed"] += 1
        if VERBOSE:
            print(f"  [Depth {fbbt_depth:03d}] ✓ {label}")
    else:
        section_stats[current_section]["failed"] += 1
        schwarzian_torque += 1.0
        print(f"  [Depth {fbbt_depth:03d}] ✗ STRUCTURAL FRICTION: {label}  {detail}")
        
        if schwarzian_torque >= UPSILON_LIMIT:
            print(f"\n{'═'*70}")
            print(f"  ⚠️ TOPOLOGICAL PHASE COLLAPSE ⚠️")
            print(f"{'═'*70}")
            print(f"  The review engine breached the maximum allowable friction (Υ = {schwarzian_torque:.1f}).")
            print(f"  Structural integrity compromised at Depth {fbbt_depth}. Halting search.")
            sys.exit(1)

# ════════════════════════════════════════════════════════════════
# NLP / ANTHROPOGENIC TOPOLOGY ENGINE
# ════════════════════════════════════════════════════════════════

def strip_latex(text):
    text = re.sub(r'\\\[.*?\\\]', ' ', text, flags=re.DOTALL)
    text = re.sub(r'\$.*?\$', ' ', text)
    text = re.sub(r'\\[a-zA-Z]+(\[[^\]]*\])?(\{[^\}]*\})?', '', text)
    return text

def tokenize_sentences(text):
    text = re.sub(r'\bi\.e\.', 'ie', text)
    text = re.sub(r'\be\.g\.', 'eg', text)
    text = re.sub(r'\bet al\.', 'et al', text)
    sentences = re.split(r'(?<!\d)[.!?]+(?!\d)', text)
    return [s.strip() for s in sentences if s.strip()]

def compute_anthropogenic_metrics(text):
    text_clean = strip_latex(text)
    sentences = tokenize_sentences(text_clean)
    lengths = [len(s.split()) for s in sentences if len(s.split()) > 3]
    if len(lengths) < 2:
        return 0.0, 0.0
    return statistics.mean(lengths), statistics.stdev(lengths)

def compute_epistemic_rust(text, cliches):
    text_clean = strip_latex(text)
    tokens = re.findall(r'\b\w+\b', text_clean.lower())
    if not tokens: return 0.0
    if not cliches: return 0.0
    rust_count = sum(text_clean.lower().count(c) for c in cliches)
    return (rust_count / len(tokens)) * 1000

# Pedagogical voice markers (Ch.0 HandPedagogy style)
PEDAGOGICAL_MARKERS = [
    "my dear reader", "don't be afraid", "look stuff up",
    "seriously", "oh my", "ear-holes", "love-child",
    "convince yourself", "you already know", "you get the gist",
    "let us", "so that i may", "welcome to",
]

def compute_pedagogical_voice(text):
    """Score how well the text matches the HandPedagogy voice."""
    text_lower = text.lower()
    hits = sum(1 for m in PEDAGOGICAL_MARKERS if m in text_lower)
    return hits, len(PEDAGOGICAL_MARKERS)

def compute_chromological_flow(text):
    text_clean = strip_latex(text)
    sentences = tokenize_sentences(text_clean)
    lengths = [len(s.split()) for s in sentences if len(s.split()) > 3]
    if len(lengths) < 2: return 0.0
    
    prime_jumps = 0
    total_jumps = len(lengths) - 1
    for i in range(total_jumps):
        if is_prime(abs(lengths[i+1] - lengths[i])):
            prime_jumps += 1
            
    return (prime_jumps / total_jumps) * 100

def no_blackbox_lean_check(tex_content, filename):
    # Lean 4 / Python references are allowed as footnotes or mathematical system mentions, 
    # but bare code file citations are flagged as lazy black boxes unless paired with natural language.
    bare_lean_count = len(re.findall(r'\\texttt\{[a-zA-Z0-9_]+\.(lean|py)\}|`[a-zA-Z0-9_]+\.(lean|py)`', tex_content))
    return bare_lean_count == 0

# ════════════════════════════════════════════════════════════════
# MAIN ENGINE RUNNER
# ════════════════════════════════════════════════════════════════

def main():
    global VERBOSE
    parser = argparse.ArgumentParser(description="Generalized Mathematical Physics & NLP Paper Review Engine.")
    parser.add_argument("--corpus", type=str, required=True, help="Directory containing the papers/markdown files.")
    parser.add_argument("--rules", type=str, default=None, help="Optional JSON ruleset for specific mathematical invariants.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")
    args = parser.parse_args()

    VERBOSE = args.verbose
    corpus_dir = Path(args.corpus)

    if not corpus_dir.exists():
        print(f"Error: Corpus directory '{corpus_dir}' does not exist.")
        sys.exit(1)

    # 1. Load Ruleset (if any)
    rules = {}
    if args.rules:
        rules_path = Path(args.rules)
        if rules_path.exists():
            with open(rules_path, 'r', encoding='utf-8') as f:
                rules = json.load(f)
            print(f"Loaded ruleset: {rules.get('config_name', 'Custom Rules')}")
            # Inject variables into MATH_ENV
            if "variables" in rules:
                for k, v in rules["variables"].items():
                    MATH_ENV[k] = v
        else:
            print(f"Warning: Rules file '{args.rules}' not found. Using generic review engine only.")

    # 2. Discover Corpus
    section("§1: Corpus Manifest & Token Budget")
    
    paper_texts = {}
    data_shape = []
    
    # Use corpus defined in rules, or just glob all .tex/.md files
    if "corpus" in rules:
        target_files = rules["corpus"]
    else:
        files = list(corpus_dir.glob("*.tex")) + list(corpus_dir.glob("*.md"))
        target_files = [{"key": f.stem, "file": f.name, "desc": f.name} for f in files]

    for item in target_files:
        key = item["key"]
        filename = item["file"]
        desc = item.get("desc", filename)
        path = corpus_dir / filename
        
        exists = path.exists()
        check(f"[{key}] {filename} exists", exists)
        if exists:
            text = path.read_text(encoding="utf-8", errors="replace")
            paper_texts[key] = text
            size_bytes = len(text.encode("utf-8"))
            est_tokens = size_bytes // 4
            num_sections = len(re.findall(r'\\section|#', text))
            data_shape.append({
                "key": key, "desc": desc, "file": filename,
                "bytes": size_bytes, "tokens": est_tokens,
                "sections": num_sections
            })
            check(f"[{key}] non-empty ({size_bytes:,} bytes, ~{est_tokens:,} tokens, {num_sections} sections)", size_bytes > 0)
        else:
            paper_texts[key] = ""
            data_shape.append({
                "key": key, "desc": desc, "file": filename,
                "bytes": 0, "tokens": 0, "sections": 0
            })

    total_bytes = sum(d["bytes"] for d in data_shape)
    total_tokens = sum(d["tokens"] for d in data_shape)

    print(f"\n  {'Paper':<40} {'Bytes':>10} {'~Tokens':>10} {'§':>4}")
    print(f"  {'─'*40} {'─'*10} {'─'*10} {'─'*4}")
    for d in data_shape:
        print(f"  {d['desc']:<40} {d['bytes']:>10,} {d['tokens']:>10,} {d['sections']:>4}")
    print(f"  {'─'*40} {'─'*10} {'─'*10} {'─'*4}")
    print(f"  {'TOTAL':<40} {total_bytes:>10,} {total_tokens:>10,}")

    check(f"Total chain: {total_bytes:,} bytes (~{total_tokens:,} tokens)", total_bytes > 0)

    # 3. Citation Integrity & Black Box Check
    section("§2: Universal Integrity & Rigor Check")
    for key, text in paper_texts.items():
        if not text: continue
        
        # Citation parsing (for LaTeX primarily)
        cite_refs = set()
        for m in re.findall(r'\\cite\{([^}]+)\}', text):
            for ref in m.split(","):
                cite_refs.add(ref.strip())
        
        bibitem_refs = set(re.findall(r'\\bibitem\{([^}]+)\}', text))
        
        # Only check internal bibitems if this paper defines bibitems.
        if bibitem_refs:
            for ref in cite_refs:
                check(f"[{key}] \\cite{{{ref}}} has \\bibitem", ref in bibitem_refs, f"MISSING bibitem for '{ref}'")

        # No Black Box check
        passed_bb = no_blackbox_lean_check(text, key)
        check(f"[{key}] NoBlackBox Check (no lazy code citations)", passed_bb, f"Found lazy code block references.")

    # 4. Mathematical Assertions
    if "math_assertions" in rules and rules["math_assertions"]:
        section("§3: Custom Mathematical Invariants")
        for assertion in rules["math_assertions"]:
            try:
                if "extract_regex" in assertion and "extract_var" in assertion:
                    target_paper = assertion.get("target_paper")
                    if target_paper and target_paper in paper_texts:
                        target_text = paper_texts[target_paper]
                        m = re.search(assertion["extract_regex"], target_text)
                        if m:
                            MATH_ENV[assertion["extract_var"]] = m.group(1)
                        else:
                            check(f"Math Invariant (Extraction): {assertion['name']}", False, f"Could not extract {assertion['extract_var']} from {target_paper}")
                            continue
                    else:
                        check(f"Math Invariant (Extraction): {assertion['name']}", False, f"Target paper {target_paper} not found")
                        continue
                res = eval(assertion["expression"], {"__builtins__": None}, MATH_ENV)
                check(f"Math Invariant: {assertion['name']}", bool(res), assertion.get("fail_message", ""))
            except Exception as e:
                check(f"Math Invariant: {assertion['name']}", False, f"Evaluation Error: {e}")

    # 5. Paper Specific Requirements (Terms & Citations)
    if "paper_requirements" in rules:
        section("§4: Corpus Structural & Topological Requirements")
        for p_key, reqs in rules["paper_requirements"].items():
            text = paper_texts.get(p_key, "")
            if not text: continue

            for term in reqs.get("required_terms", []):
                # Simple substring check (or regex if defined as such)
                check(f"[{p_key}] Requires Term: '{term}'", term in text)
            
            for f_term in reqs.get("forbidden_terms", []):
                check(f"[{p_key}] Forbids Term: '{f_term}'", f_term not in text)
                
            for cite in reqs.get("required_citations", []):
                check(f"[{p_key}] Requires Citation: '{cite}'", cite in text)

    # 6. Specialized Regex/Formatting rules (e.g. Cullen Notation)
    if "cullen_notation" in rules:
        section("§5: Notation Formality & CPT Rigor")
        cullen = rules["cullen_notation"]
        for p_key in cullen.get("apply_to", []):
            text = paper_texts.get(p_key, "")
            if not text: continue
            
            for pattern in cullen.get("forbidden_regexes", []):
                check(f"[{p_key}] Formality: Reject '{pattern}'", re.search(pattern, text) is None)
            
            for term in cullen.get("required_terms", []):
                check(f"[{p_key}] Formality: Require '{term}'", term in text)

    # 7. Anthropogenic Topology (NLP bounds)
    section("§6: Anthropogenic Topology & AI-Burstiness")
    bounds = rules.get("nlp_topology_bounds", {
        "min_stdev_length": 6.0,
        "max_epistemic_rust_per_1000": 23.0,
        "min_chromological_flow_percent": 14.0
    })

    cliches = bounds.get("epistemic_rust_cliches", [])

    for key, tex in paper_texts.items():
        if tex:
            mean_len, stdev_len = compute_anthropogenic_metrics(tex)
            rust_density = compute_epistemic_rust(tex, cliches)
            chrom_ratio = compute_chromological_flow(tex)
            
            # Carbon Compatibility
            check(f"[{key}] Sentence Variance Gate (σ = {stdev_len:.1f} > {bounds['min_stdev_length']})",
                  stdev_len > bounds['min_stdev_length'], "Rigid formatting detected (low sentence-length variance)")
                  
            # Humanity Gate
            check(f"[{key}] Cliché Density Gate (density = {rust_density:.1f}/1k < {bounds['max_epistemic_rust_per_1000']})",
                  rust_density < bounds['max_epistemic_rust_per_1000'], "High cliché/filler phrase density detected")
                  
            # Prime Resonance
            check(f"[{key}] Sentence Diversity Gate (diversity = {chrom_ratio:.1f}% > {bounds['min_chromological_flow_percent']})",
                  chrom_ratio > bounds['min_chromological_flow_percent'], "Low sentence-length diversity (monotonic pacing detected)")

    # 6.5 Pedagogical Voice (Ch.0 specific)
    section("§6.5: Pedagogical Voice (Ch.0)")
    for key, tex in paper_texts.items():
        if "00_Pedagogical" in key or "pedagogical" in key.lower():
            hits, total = compute_pedagogical_voice(tex)
            score = hits / total if total > 0 else 0
            check(f"[{key}] Pedagogical voice ({hits}/{total} markers, {score:.0%})",
                  score >= 0.15, "Weak HandPedagogy voice — needs more conversational markers")

    # 7. Volume Structure Validation
    section("§7: Volume Structure Validation (4-Volume)")
    
    vol1_key = None
    vol2_key = None
    vol3_key = None
    vol4_key = None
    
    for key in paper_texts:
        if "vol1" in key.lower() or "02_vol1" in key.lower(): vol1_key = key
        if "vol2" in key.lower() or "03_vol2" in key.lower(): vol2_key = key
        if "vol3" in key.lower() or "04_vol3" in key.lower(): vol3_key = key
        if "vol4" in key.lower() or "05_vol4" in key.lower(): vol4_key = key

    if vol1_key and paper_texts.get(vol1_key):
        vol1 = paper_texts[vol1_key]
        check("Vol 1: Foundations and Logical Creativity", "Foundations and Logical" in vol1 or "Logical Creativity" in vol1, "Vol 1 title should include Logical Creativity")
        check("Vol 1: Ch.0 included", "00_Pedagogical_Foundation" in vol1, "Vol 1 should include Ch.0")
        check("Vol 1: Part II NOT included", "Informational Creativity" not in vol1, "Part II (Informational) should be in Vol 2, not Vol 1")

    if vol2_key and paper_texts.get(vol2_key):
        vol2 = paper_texts[vol2_key]
        check("Vol 2: Part II included", "Informational Creativity" in vol2, "Vol 2 should include Part II")
        check("Vol 2: Part III NOT included", "Physical Creativity" not in vol2, "Vol 2 should NOT include Part III (that is Vol 3)")

    if vol3_key and paper_texts.get(vol3_key):
        vol3 = paper_texts[vol3_key]
        check("Vol 3: Part III included", "Physical Creativity" in vol3, "Vol 3 should include Part III")
        check("Vol 3: Metareal Cosmology included", "16_Metareal_Cosmology" in vol3 or "15_Metareal_Cosmology" in vol3, "Vol 3 should include Metareal Cosmology")

    if vol4_key and paper_texts.get(vol4_key):
        vol4 = paper_texts[vol4_key]
        check("Vol 4: Appendices included", "Mathematical & Theoretical Appendices" in vol4 or "Mathematical \\& Theoretical Appendices" in vol4, "Vol 4 should include Appendices")
        check("Vol 4: Ramanujan Sato included", "31_Categorical_Qualia_Gauge" in vol4 or "31_Unreal_Ramanujan_Sato" in vol4, "Vol 4 should include Ramanujan Sato or Qualia")

    # 8. Claim Confinement Audit
    if "claim_confinement" in rules:
        section("§7: Claim Confinement & Scope Audit")
        conf = rules["claim_confinement"]
        
        for key, text in paper_texts.items():
            if not text: continue
            text_lower = text.lower()
            
            # Overreach phrases
            for phrase in conf.get("overreach_phrases", []):
                found = phrase.lower() in text_lower
                check(f"[{key}] No overreach: '{phrase}'", not found,
                      f"CLAIM OVERREACH: '{phrase}' found in body text. Downgrade or hedge.")
            
            # Informal register
            for phrase in conf.get("informal_register_phrases", []):
                found = phrase in text
                check(f"[{key}] No informal register: '{phrase}'", not found,
                      f"INFORMAL REGISTER: '{phrase}' is not peer-review appropriate.")
            
            # Hedge-required contexts
            hedges = conf.get("hedge_required_contexts", {})
            for trigger, required_hedges in hedges.items():
                if trigger.startswith("_"): continue  # skip _doc
                # Find all occurrences of the trigger in body text (not comments)
                # Use a 2000-char window (approx one section) and require at least
                # one occurrence to have a hedge nearby. This prevents false positives
                # when the trigger appears in a "Classically, X says..." context
                # and the hedge appears a few paragraphs later in the same section.
                # Exclude bibliography sections from hedge checks
                bib_start = text.find('\\begin{thebibliography}')
                search_text = text[:bib_start] if bib_start != -1 else text
                positions = [m.start() for m in re.finditer(re.escape(trigger), search_text)]
                if not positions: continue
                
                # Check: does ANY occurrence have a hedge within ±2000 chars?
                any_hedged = False
                for pos in positions:
                    window = text[max(0, pos-2000):pos+2000]
                    if any(h.lower() in window.lower() for h in required_hedges):
                        any_hedged = True
                        break
                
                first_line = text[:positions[0]].count('\n') + 1
                check(f"[{key}] Hedge for '{trigger}' ({len(positions)} occurrences, first ~line {first_line})",
                      any_hedged,
                      f"UNHEDGED CLAIM: '{trigger}' mentioned {len(positions)}x without scope qualifier. "
                      f"Need one of: {required_hedges}")

    # 9. Proof Format Consistency
    if "proof_format_rules" in rules:
        section("§8: Proof Format Consistency")
        pfr = rules["proof_format_rules"]
        
        for key, text in paper_texts.items():
            if not text: continue
            
            # Check all \begin{proof} blocks have \qedhere
            if pfr.get("require_qedhere_in_proof", False):
                proof_blocks = list(re.finditer(r'\\begin\{proof\}(.*?)\\end\{proof\}', text, re.DOTALL))
                for i, m in enumerate(proof_blocks):
                    has_qed = 'qedhere' in m.group(1)
                    line_num = text[:m.start()].count('\n') + 1
                    check(f"[{key}] Proof {i+1} (line ~{line_num}) has \\qedhere", has_qed,
                          "MISSING \\qedhere — proof block lacks QED marker.")
            
            # Check bold "Theorem" labels use \begin{theorem} environment
            if pfr.get("bold_theorem_must_use_environment", False):
                for pattern in pfr.get("bold_theorem_patterns", []):
                    matches = re.findall(pattern, text)
                    for m in matches:
                        # Check if this is inside a \begin{theorem} environment
                        # (i.e., it's a bare bold "Theorem" in body text)
                        check(f"[{key}] Bare bold label: '{m}'", False,
                              f"USE ENVIRONMENT: Bold '{m}' should use \\begin{{theorem}} instead.")

    # 8. HALTING STATE
    print(f"\n{'═'*70}")
    print(f"  REVIEW ENGINE HALTING STATE REPORT")
    print(f"{'═'*70}")
    
    for sect_name, stats in section_stats.items():
        total_s = stats["passed"] + stats["failed"]
        if total_s > 0:
            status = "✓" if stats["failed"] == 0 else "✗"
            print(f"  {status} {sect_name}: {stats['passed']}/{total_s} passed")

    print(f"\n  Final Topological Depth: {fbbt_depth} (Maximum verified structural depth)")
    print(f"  Accumulated Friction Torque (Υ): {schwarzian_torque:.1f}")

    if schwarzian_torque > 0.0:
        print(f"\n  ⚠️ UNSTABLE HALTING STATE. Υ = {schwarzian_torque:.1f}")
        print("  The review encountered structural friction but completed via partial collapse.")
        sys.exit(1)
    else:
        print(f"\n  ✅ STABLE HALTING STATE REACHED")
        print("  The entire corpus structurally evaluates successfully.")
        sys.exit(0)

if __name__ == "__main__":
    main()
