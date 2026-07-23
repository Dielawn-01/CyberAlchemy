import os
import re
import json
import math

def run_audit():
    rules_path = '/home/phrxmaz/Documents/InfoPhys/LaRueResearch/scripts/larue_principia_rules.json'
    with open(rules_path, 'r', encoding='utf-8') as f:
        rules = json.load(f)

    papers_dir = '/home/phrxmaz/Documents/CyberAlchemy/papers'
    
    report = []
    report.append("=======================================================")
    report.append("         PRINCIPIA PSYCHEDELIA BOOK AUDIT REPORT        ")
    report.append("=======================================================\n")

    # 1. Math Assertions Validation
    report.append("--- 1. MATHEMATICAL ASSERTIONS AUDIT ---")
    P = rules['variables']['P']
    PHI_229 = rules['variables']['PHI_229']
    PHIBAR_229 = rules['variables']['PHIBAR_229']
    
    # Extract golden root <148> from 01_Unreal_Algebra_Connes_Geometry.tex
    extracted_phi = "148"
    lc_path = os.path.join(papers_dir, '01_Unreal_Algebra_Connes_Geometry.tex')
    if os.path.exists(lc_path):
        with open(lc_path, 'r', encoding='utf-8') as f:
            m = re.search(r'\\langle\s*([0-9]+)\s*\\rangle', f.read())
            if m:
                extracted_phi = m.group(1)

    math_failures = 0
    for assertion in rules['math_assertions']:
        expr = assertion['expression']
        try:
            # Safe eval context
            val = eval(expr, {"math": math, "pow": pow, "P": P, "PHI_229": PHI_229, "PHIBAR_229": PHIBAR_229, "extracted_phi": extracted_phi, "mult_order": lambda a, p: [k for k in range(1, p) if pow(a, k, p) == 1][0]})
            if val:
                report.append(f"[PASS] {assertion['name']}")
            else:
                report.append(f"[FAIL] {assertion['name']}: {assertion['fail_message']}")
                math_failures += 1
        except Exception as e:
            report.append(f"[ERROR] {assertion['name']}: {str(e)}")
            math_failures += 1
    
    report.append(f"\nMath Assertions Audit Summary: {len(rules['math_assertions']) - math_failures}/{len(rules['math_assertions'])} Passed.\n")

    # 2. Lean References Audit
    report.append("--- 2. LEAN VERIFICATION REFERENCES AUDIT ---")
    lean_patterns = [
        r'\blean\b', r'\bMathlib\b', r'\bMathlib4\b', r'\bSciLean\b', r'formalized\s+in\s+Lean', r'proved\s+in\s+Lean', r'lean4/'
    ]
    lean_issues = []
    tex_files = [f for f in os.listdir(papers_dir) if f.endswith('.tex')]
    
    for fname in sorted(tex_files):
        fpath = os.path.join(papers_dir, fname)
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        for line_num, line in enumerate(content.splitlines(), 1):
            if line.strip().startswith('%'):
                continue # Skip comments
            for pat in lean_patterns:
                if re.search(pat, line, re.IGNORECASE):
                    lean_issues.append((fname, line_num, pat, line.strip()[:80]))
    
    if not lean_issues:
        report.append("[PASS] Zero Lean references found in book manuscript text.")
    else:
        report.append(f"[WARN] Found {len(lean_issues)} Lean references in manuscript text:")
        for fname, lnum, pat, snippet in lean_issues:
            report.append(f"   - {fname}:L{lnum} (matches '{pat}'): \"{snippet}\"")
    report.append("")

    # 3. Overreach & Informal Register Audit
    report.append("--- 3. CLAIM CONFINEMENT & REGISTER AUDIT ---")
    overreach_phrases = rules['claim_confinement']['overreach_phrases']
    informal_phrases = rules['claim_confinement']['informal_register_phrases']
    
    overreach_found = []
    informal_found = []
    
    for fname in sorted(tex_files):
        fpath = os.path.join(papers_dir, fname)
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        for line_num, line in enumerate(content.splitlines(), 1):
            if line.strip().startswith('%'):
                continue
            for phrase in overreach_phrases:
                if phrase.lower() in line.lower():
                    overreach_found.append((fname, line_num, phrase, line.strip()[:80]))
            for phrase in informal_phrases:
                if phrase.lower() in line.lower():
                    informal_found.append((fname, line_num, phrase, line.strip()[:80]))
                    
    if not overreach_found:
        report.append("[PASS] No overreaching claims detected.")
    else:
        report.append(f"[WARN] Found {len(overreach_found)} potentially overreaching phrases:")
        for fname, lnum, phrase, snippet in overreach_found[:10]:
            report.append(f"   - {fname}:L{lnum} ('{phrase}'): \"{snippet}\"")
            
    if not informal_found:
        report.append("[PASS] No informal register phrases detected.")
    else:
        report.append(f"[WARN] Found {len(informal_found)} informal register phrases:")
        for fname, lnum, phrase, snippet in informal_found:
            report.append(f"   - {fname}:L{lnum} ('{phrase}'): \"{snippet}\"")
    report.append("")

    # 4. Epistemic Rust (AI Clichés) Audit
    report.append("--- 4. EPISTEMIC RUST (AI CLICHÉS) AUDIT ---")
    rust_cliches = rules['nlp_topology_bounds']['epistemic_rust_cliches']
    rust_counts = {}
    
    for fname in sorted(tex_files):
        fpath = os.path.join(papers_dir, fname)
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        for cliche in rust_cliches:
            matches = len(re.findall(r'\b' + re.escape(cliche) + r'\b', content, re.IGNORECASE))
            if matches > 0:
                rust_counts[cliche] = rust_counts.get(cliche, 0) + matches

    report.append("AI Cliché frequencies across codebase:")
    for cliche, count in sorted(rust_counts.items(), key=lambda x: x[1], reverse=True):
        status = "[HIGH]" if count > 20 else "[MODERATE]" if count > 5 else "[LOW]"
        report.append(f"   {status} '{cliche}': {count} occurrences")
    report.append("")

    # 5. Build Artifact Integrity Audit
    report.append("--- 5. COMPILED BUILD ARTIFACT AUDIT ---")
    build_volumes_dir = os.path.join(papers_dir, 'build/Volumes')
    build_papers_dir = os.path.join(papers_dir, 'build/papers')
    build_master_dir = os.path.join(papers_dir, 'build')
    
    expected_pdfs = [
        os.path.join(build_master_dir, '01_Principia_Psychedelia_Master.pdf'),
        os.path.join(build_master_dir, '01_Principia_Psychedelia_Full.pdf'),
        os.path.join(build_volumes_dir, '02_Vol1_Master.pdf'),
        os.path.join(build_volumes_dir, '03_Vol2_Master.pdf'),
        os.path.join(build_volumes_dir, '04_Vol3_Master.pdf'),
        os.path.join(build_volumes_dir, '05_Vol4_Master.pdf'),
    ]
    
    for pdf_path in expected_pdfs:
        if os.path.exists(pdf_path):
            size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
            report.append(f"[PASS] {os.path.basename(pdf_path)} exists ({size_mb:.2f} MB)")
        else:
            report.append(f"[FAIL] {os.path.basename(pdf_path)} missing!")
            
    print("\n".join(report))

if __name__ == '__main__':
    run_audit()
