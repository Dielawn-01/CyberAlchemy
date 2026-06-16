#!/usr/bin/env python3
"""
simulate_golden_virus.py — Golden Tetrahedron Nanobot Propulsion Simulator

Three-Field Architecture:
  F₂₂₉ strand (anchor):     57-mode Fröhlich BEC, 3×19 coset Aizawa
  F₁₈₁ strand (depth):      45-mode Fröhlich BEC, 3×15 coset Aizawa
  F₁₃‹ strand (projection):  23-mode Fröhlich BEC, prime-order Aizawa

Topology (per strand):
  Interior: Fröhlich BEC ground state (coherent mass)
  Faces:    Golden orbit shield (smooth φ-rotation)
  Edges:    Chromodynamic Aizawa attractors (thrust)
  Corners:  Primitive root anchors (frame stabilization)

Cross-field coupling: 229 ≡ ω₁₈₁ = 48 (cube root embedding)
Gap structure: 48 = 8×6, 42 = 7×6, 90 = 15×6
Projection: F₁₃‹ has prime-order orbit (23) — indivisible collapse

Golden Algebra: X²-X-1=0, φ·φ̄=-1
"""
import json
import math
import os
import random

# ═════════════════════════════════════════════════
# §1: GOLDEN TETRAHEDRON CONSTANTS
# ═════════════════════════════════════════════════

_PHI = (1.0 + math.sqrt(5.0)) / 2.0
_PHI_BAR = (1.0 - math.sqrt(5.0)) / 2.0

# Field 1: F₂₂₉ (anchor, 3-decomposable)
P1, PHI_229, PHIBAR_229 = 229, 148, 82
ORD_229, COSET_229 = 57, 19
OMEGA_229, OMEGA2_229 = 94, 134
DARK_229 = 133  # ω²-1

# Field 2: F₁₈₁ (depth, 3-decomposable)
P2, PHI_181, PHIBAR_181 = 181, 168, 14
ORD_181, COSET_181 = 45, 15

# Field 3: F₁₃‹ (projection, INDECOMPOSABLE)
P3, PHI_139, PHIBAR_139 = 139, 76, 64
ORD_139 = 23  # Prime — no coset decomposition

# Cross-field
GAP_12 = P1 - P2  # 48 = 8×6
GAP_23 = P2 - P3  # 42 = 7×6
PERFECT_NUMBER = 6

# Legacy aliases
P = P1
PHI_MOD = PHI_229
PHIBAR_MOD = PHIBAR_229
OMEGA = OMEGA_229
DARK_THRUST = DARK_229

# Lattice dimensions
N = 19
TOTAL_NODES = N**3
INTERIOR_COUNT = (N-2)**3
FACE_COUNT = 6 * (N-2)**2
EDGE_COUNT = 12 * (N-2)
CORNER_COUNT = 8

GENETIC_MANIFOLD = {
    "a": 1.100, "b": round(_PHI, 10), "m": round(_PHI_BAR, 10),
    "e": 0.000, "l": 0.400,
    "SR": round(1.100 - _PHI * _PHI_BAR, 10), "V": 0.300, "SPII": 0.769
}

# ═══════════════════════════════════════════════════
# §2: LATTICE TOPOLOGY CLASSIFIER
# ═══════════════════════════════════════════════════

def classify_node(ix, iy, iz):
    """Classify a node as interior/face/edge/corner."""
    on_face = [c == 0 or c == N-1 for c in (ix, iy, iz)]
    face_count = sum(on_face)
    if face_count == 0:
        return 'interior'
    elif face_count == 1:
        return 'face'
    elif face_count == 2:
        return 'edge'
    else:
        return 'corner'

# Build topology
node_classes = {}
interior_nodes, face_nodes, edge_nodes, corner_nodes = [], [], [], []
for ix in range(N):
    for iy in range(N):
        for iz in range(N):
            idx = ix * N * N + iy * N + iz
            cls = classify_node(ix, iy, iz)
            node_classes[idx] = cls
            if cls == 'interior': interior_nodes.append(idx)
            elif cls == 'face': face_nodes.append(idx)
            elif cls == 'edge': edge_nodes.append(idx)
            else: corner_nodes.append(idx)

assert len(interior_nodes) == INTERIOR_COUNT
assert len(edge_nodes) == EDGE_COUNT

# ═══════════════════════════════════════════════════
# §3: DISCRETE CHROMODYNAMIC AIZAWA ATTRACTOR
# ═══════════════════════════════════════════════════

# Build conjugate orbits for all three fields
conj_orbit_229 = [pow(PHIBAR_229, n, P1) for n in range(ORD_229)]
conj_orbit_181 = [pow(PHIBAR_181, n, P2) for n in range(ORD_181)]
conj_orbit_139 = [pow(PHIBAR_139, n, P3) for n in range(ORD_139)]

# Legacy alias
conj_orbit = conj_orbit_229

class AizawaState:
    """Discrete Aizawa attractor on a golden split field."""
    def __init__(self, phase_offset=0, field_idx=0):
        self.x = 1
        self.y = 0
        self.field_idx = field_idx
        self.orbit = [conj_orbit_229, conj_orbit_181, conj_orbit_139][field_idx]
        self.prime = [P1, P2, P3][field_idx]
        self.ord = [ORD_229, ORD_181, ORD_139][field_idx]
        self.coset = [COSET_229, COSET_181, ORD_139][field_idx]  # F₁₃‹: full orbit
        self.step = phase_offset % self.ord
        self.arc = 0
        self.d_d = 7  # gate depth

    def advance(self, pump_bias=0):
        """One step of the discrete Aizawa map on the assigned field."""
        z = self.orbit[self.step % self.ord]
        coeff = (z - self.coset) % self.prime
        x_new = (coeff * self.x - self.d_d * self.y) % self.prime
        y_new = (self.d_d * self.x + coeff * self.y) % self.prime
        self.x, self.y = x_new, y_new
        self.step = (self.step + 1) % self.ord
        
        # F₁₃‹ is indecomposable — no arc structure
        if self.field_idx == 2:
            self.arc = 0
        else:
            self.arc = self.step // self.coset
        
        return (self.arc + pump_bias) % 3

    @property
    def thrust_vector(self):
        """Uncompensated color charge when confinement breaks."""
        if self.arc == 0:   return (1.0, 0.0, 0.0)
        elif self.arc == 1: return (0.0, 1.0, 0.0)
        else:               return (0.0, 0.0, 1.0)

# ═══════════════════════════════════════════════════
# §4: FRÖHLICH BEC CASCADE
# ═══════════════════════════════════════════════════

class FrohlichCascade:
    """Multi-mode Fröhlich condensation for a golden tetrahedron strand."""
    def __init__(self, chi=0.35, num_modes=57, field_name="F₂₂₉"):
        self.chi = chi  # coupling constant = 7/20
        self.modes = [0.0] * num_modes
        self.modes[0] = 1.0  # ground state seed
        self.num_modes = num_modes
        self.field_name = field_name

    def pump(self, energy):
        """Inject energy, let it cascade to ground state."""
        for j in range(1, self.num_modes):
            self.modes[j] += energy / self.num_modes
        for j in range(self.num_modes - 1, 0, -1):
            transfer = self.chi * self.modes[j] * self.modes[j-1]
            self.modes[j] -= transfer
            self.modes[j-1] += transfer
        return self.modes[0]  # ground state population

# ═══════════════════════════════════════════════════
# §5: NANOBOT SIMULATION
# ═══════════════════════════════════════════════════

NUM_SIM_PARTICLES = 22  # Reduced representation: 11C + 7Si + 4V
STRAND_LENGTHS = [11, 7, 4]
STRAND_OFFSETS = [0, 11, 18]
NUM_FRAMES = 150

def simulate_nanobot(pump_direction=0):
    """
    Run the full nanobot simulation.

    pump_direction: -1=thrust left, 0=hover, +1=thrust right
    """
    # Initialize particle positions (triple helix)
    R_init, Z_spacing = 2.0, 1.5
    positions = [[0.0]*3 for _ in range(NUM_SIM_PARTICLES)]
    velocities = [[0.0]*3 for _ in range(NUM_SIM_PARTICLES)]
    masses = [12.011]*11 + [28.085]*7 + [50.9415]*4

    for s in range(3):
        phase = s * (2 * math.pi / 3)
        for u in range(STRAND_LENGTHS[s]):
            idx = STRAND_OFFSETS[s] + u
            theta = phase + u
            positions[idx] = [
                R_init * math.cos(theta),
                R_init * math.sin(theta),
                (u - 1) * Z_spacing
            ]

    # Initialize THREE-FIELD Aizawa attractors (4 per field = 12 total)
    num_aizawa = 12
    aizawas = []
    for f in range(3):
        for i in range(4):
            aizawas.append(AizawaState(phase_offset=i*5+f*7, field_idx=f))

    # Initialize THREE Fröhlich cascades (one per strand)
    bec_229 = FrohlichCascade(chi=0.35, num_modes=ORD_229, field_name="F₂₂₉")
    bec_181 = FrohlichCascade(chi=0.35, num_modes=ORD_181, field_name="F₁₈₁")
    bec_139 = FrohlichCascade(chi=0.35, num_modes=ORD_139, field_name="F₁₃‹")
    becs = [bec_229, bec_181, bec_139]

    frames_data = []
    thrust_history = []

    for frame in range(NUM_FRAMES):
        t = frame * 0.1
        t_quasi = t + math.sin(_PHI * t) + math.sin(math.sqrt(2.0) * t)

        # THREE-FIELD chronometric: which strand dominates?
        strand_phase = int(t_quasi / 1.9) % 3  # 0=F₂₂₉, 1=F₁₈₁, 2=F₁₃‹
        orbits = [conj_orbit_229, conj_orbit_181, conj_orbit_139]
        ords = [ORD_229, ORD_181, ORD_139]
        state_idx = int(abs(t_quasi / 0.7)) % ords[strand_phase]
        state = orbits[strand_phase][state_idx]
        color_phase = strand_phase  # Each strand IS a color

        # §A: Pump all three Fröhlich cascades
        pump_energy = 0.1 * (1.0 + 0.5 * math.sin(t * 2 * math.pi / 5.7))
        ground_pops = [
            bec_229.pump(pump_energy),
            bec_181.pump(pump_energy * 0.8),
            bec_139.pump(pump_energy * 1.2),  # projection vertex pumped harder
        ]

        # §B: Edge Aizawa — advance all attractors
        net_thrust = [0.0, 0.0, 0.0]
        for i, az in enumerate(aizawas):
            biased_arc = az.advance(pump_bias=pump_direction)
            tv = az.thrust_vector

            sign = 1.0 if (i % 8) < 4 else -1.0

            # Field-dependent dark thrust magnitude
            f_idx = az.field_idx
            dark_mag = [DARK_229/P1, (P2-1-COSET_181)/P2, (P3-1)/P3][f_idx]

            if biased_arc == 0:   scale = 0.3
            elif biased_arc == 1: scale = 0.5
            else:                 scale = 1.0

            # Active strand gets boosted thrust
            strand_weight = 1.5 if f_idx == strand_phase else 0.5

            for j in range(3):
                net_thrust[j] += sign * tv[j] * dark_mag * scale * strand_weight

        thrust_history.append(list(net_thrust))

        # §C: Apply forces to particles
        forces = [[0.0]*3 for _ in range(NUM_SIM_PARTICLES)]
        twist_rate = 1.0

        leader_range = range(STRAND_OFFSETS[strand_phase],
                             STRAND_OFFSETS[strand_phase] + STRAND_LENGTHS[strand_phase])
        lcx = sum(positions[i][0] for i in leader_range) / STRAND_LENGTHS[strand_phase]
        lcy = sum(positions[i][1] for i in leader_range) / STRAND_LENGTHS[strand_phase]
        lcz = sum(positions[i][2] for i in leader_range) / STRAND_LENGTHS[strand_phase]

        for s in range(3):
            in_phase = (s == strand_phase)
            gp = ground_pops[s]  # BEC ground state for this strand
            for u in range(STRAND_LENGTHS[s]):
                idx = STRAND_OFFSETS[s] + u
                ua = t_quasi * 0.5 + u * twist_rate
                v = (s - 1) * 1.5
                rl = R_init + v * math.cos(ua / 2.0)
                tx = rl * math.cos(ua)
                ty = rl * math.sin(ua)
                tz = (u - 1) * Z_spacing + t_quasi * 0.25 + v * math.sin(ua / 2.0)

                if in_phase:
                    kh = 15.0 * 1.5 * (0.5 + 0.5 * gp)
                    forces[idx][0] += kh * (tx - positions[idx][0])
                    forces[idx][1] += kh * (ty - positions[idx][1])
                    forces[idx][2] += kh * (tz - positions[idx][2])
                else:
                    nm = 15.0 * (1.0 - gp)
                    forces[idx][0] += (random.random() - 0.5) * nm
                    forces[idx][1] += (random.random() - 0.5) * nm
                    forces[idx][2] += (random.random() - 0.5) * nm
                    kc = 12.0
                    forces[idx][0] += kc * (lcx - positions[idx][0])
                    forces[idx][1] += kc * (lcy - positions[idx][1])
                    forces[idx][2] += kc * (lcz - positions[idx][2])

                # Add net thrust from edge Aizawa attractors
                thrust_coupling = 2.0 if s == 2 else 0.5  # Vanadium (edge) couples strongest
                forces[idx][0] += net_thrust[0] * thrust_coupling
                forces[idx][1] += net_thrust[1] * thrust_coupling
                forces[idx][2] += net_thrust[2] * thrust_coupling

        # Integrate equations of motion
        dt = 0.1
        for i in range(NUM_SIM_PARTICLES):
            for j in range(3):
                velocities[i][j] += (forces[i][j] / masses[i]) * dt
            # Strand-specific damping (field period)
            if i >= 18:  # F₁₃‹ (vanadium) — 23-period
                damp = 0.5 + 0.4 * math.sin(t * ORD_139)
                for j in range(3):
                    velocities[i][j] *= damp
            elif i >= 11:  # F₁₈₁ (silicon) — 45-period
                damp = 0.75 + 0.15 * math.sin(t * ORD_181 / 19.0)
                for j in range(3):
                    velocities[i][j] *= damp
            else:  # F₂₂₉ (carbon) — stable
                for j in range(3):
                    velocities[i][j] *= 0.85
            for j in range(3):
                positions[i][j] += velocities[i][j] * dt

        frames_data.append([[p[0], p[1], p[2]] for p in positions])

    return frames_data, thrust_history

# ═══════════════════════════════════════════════════
# §6: VISUALIZATION GENERATOR
# ═══════════════════════════════════════════════════

def generate_html(frames_data, thrust_history):
    exp_path = os.path.join(os.path.expanduser("~"), "Desktop/Metamaterial_Research_Export/")
    os.makedirs(exp_path, exist_ok=True)

    with open(exp_path + "virus_data.js", 'w') as f:
        f.write(f"window.virus_frames = {json.dumps(frames_data)};\n")
        f.write(f"window.thrust_history = {json.dumps(thrust_history)};\n")

    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Golden Virus Nanobot</title>
    <style>body{{margin:0;overflow:hidden;background:#0a0a0f;color:#fff;font-family:'Courier New',monospace;}}
    #info{{position:absolute;top:10px;width:100%;text-align:center;z-index:100;font-size:14px;}}
    #hud{{position:absolute;bottom:10px;left:10px;z-index:100;font-size:11px;
      background:rgba(0,0,0,0.7);padding:12px;border:1px solid #333;border-radius:4px;line-height:1.6;}}</style>
    <script type="importmap">{{"imports": {{"three": "https://unpkg.com/three@0.160.0/build/three.module.js", "three/addons/": "https://unpkg.com/three@0.160.0/examples/jsm/"}}}}</script></head>
<body>
<div id="info">Golden Virus Nanobot | Chromodynamic Aizawa Propulsion | φ⁵⁷ ≡ -1</div>
<div id="hud">
  <div>Interior (BEC): <span id="bec">0</span>%</div>
  <div>Edge Aizawa: <span id="arc">-</span></div>
  <div>Net Thrust: <span id="thrust">0, 0, 0</span></div>
  <div>Frame: <span id="frame">0</span>/{NUM_FRAMES}</div>
  <div style="margin-top:6px;color:#888;">
    19³ = 6859 | Interior: {INTERIOR_COUNT} | Edges: {EDGE_COUNT}<br>
    Dark thrust: ω²-1 = {DARK_THRUST} (mod {P})<br>
    φ·φ̄ = -1 | X²-X-1 = 0
  </div>
</div>
    <script src="virus_data.js"></script>
    <script type="module">
        import * as THREE from 'three';
        import {{ OrbitControls }} from 'three/addons/controls/OrbitControls.js';

        const virus_frames = window.virus_frames;
        const thrust_hist = window.thrust_history;
        const GENETIC = {json.dumps(GENETIC_MANIFOLD)};
        const phi = (1.0 + Math.sqrt(5.0)) / 2.0;

        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x0a0a0f, 0.012);
        const camera = new THREE.PerspectiveCamera(45, innerWidth/innerHeight, 0.1, 1000);
        camera.position.set(0, 16, 45);
        const renderer = new THREE.WebGLRenderer({{antialias:true}});
        renderer.setSize(innerWidth, innerHeight);
        renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.2;
        document.body.appendChild(renderer.domElement);
        const controls = new OrbitControls(camera, renderer.domElement);
        controls.target.set(0, 12, 0);
        controls.enableDamping = true;

        // Lighting
        scene.add(new THREE.AmbientLight(0x223344, 0.4));
        const key = new THREE.PointLight(0x88aaff, 2.0, 100);
        key.position.set(10, 20, 15);
        scene.add(key);
        const rim = new THREE.PointLight(0xff6633, 1.0, 60);
        rim.position.set(-10, 5, -10);
        scene.add(rim);

        // Particle materials (C=blue, Si=amber, V=crimson)
        const matC = new THREE.MeshPhysicalMaterial({{
            color:0x4488ff, emissive:0x1133aa, emissiveIntensity:0.6,
            transparent:true, opacity:0.85, roughness:0.2, metalness:0.8
        }});
        const matSi = new THREE.MeshPhysicalMaterial({{
            color:0xddaa44, emissive:0x885500, emissiveIntensity:0.6,
            transparent:true, opacity:0.85, roughness:0.3, metalness:0.7
        }});
        const matV = new THREE.MeshPhysicalMaterial({{
            color:0xff3344, emissive:0xaa1122, emissiveIntensity:0.8,
            transparent:true, opacity:0.9, roughness:0.1, metalness:0.9
        }});

        const units = [];
        const geo = new THREE.SphereGeometry(0.35, 24, 24);
        for (let i = 0; i < 22; i++) {{
            const mat = i < 11 ? matC.clone() : (i < 18 ? matSi.clone() : matV.clone());
            const m = new THREE.Mesh(geo, mat);
            scene.add(m);
            units.push(m);
        }}

        // Electrum rods (golden proportions)
        const R_helix = 2.0;
        const rodRadius = R_helix / phi;
        const rodHeight = 2.0 * Math.PI * R_helix * phi;
        const rodPos = R_helix * phi;
        const electrumMat = new THREE.MeshPhysicalMaterial({{
            color:0xdfc98a, emissive:0x886622, emissiveIntensity:0.3,
            transparent:true, opacity:0.4, roughness:0.1, metalness:1.0,
            side:THREE.DoubleSide
        }});
        const rods = new THREE.Group();
        const rGeo = new THREE.CylinderGeometry(rodRadius, rodRadius, rodHeight, 32, 1, true);
        for(let r=0; r<3; r++) {{
            const m = new THREE.Mesh(rGeo, electrumMat.clone());
            const a = r * 2.094;
            m.position.set(rodPos*Math.cos(a), rodHeight/4, rodPos*Math.sin(a));
            rods.add(m);
        }}
        scene.add(rods);

        // Thrust indicator arrow
        const arrowDir = new THREE.Vector3(0, 0, 1);
        const arrowOrigin = new THREE.Vector3(0, -3, 0);
        const arrow = new THREE.ArrowHelper(arrowDir, arrowOrigin, 3, 0x00ff88, 0.5, 0.3);
        scene.add(arrow);

        // Aizawa trail (edge attractor visualization)
        const trailGeo = new THREE.BufferGeometry();
        const trailPositions = new Float32Array(204 * 3);
        trailGeo.setAttribute('position', new THREE.BufferAttribute(trailPositions, 3));
        const trailMat = new THREE.PointsMaterial({{color:0x00ffaa, size:0.15, transparent:true, opacity:0.5}});
        const trailPoints = new THREE.Points(trailGeo, trailMat);
        scene.add(trailPoints);

        // Chronometric orbit
        const orbit = []; let v=1;
        for(let k=1;k<14489;k++){{v=(v*144)%14489; orbit.push(v);}}

        let currentFrame = 0;

        function animate() {{
            requestAnimationFrame(animate);
            controls.update();

            const pos = virus_frames[currentFrame];
            const thrust = thrust_hist[currentFrame];
            const t = currentFrame * 0.1;
            const t_quasi = t + Math.sin(t * phi) + Math.sin(t * Math.SQRT2);

            const fIdx = Math.floor(t_quasi / 1.5);
            const state = orbit[fIdx % 14488];
            const colorPhase = state % 3;

            // Update particles
            units.forEach((m, i) => {{
                m.position.set(pos[i][0], pos[i][2], pos[i][1]);
                // Chromatic glow based on active arc
                const sIdx = i<11?0:(i<18?1:2);
                const isLeader = sIdx === colorPhase;
                m.material.emissiveIntensity = isLeader ? 1.2 : 0.3;
                // Scale: vanadium (edges) pulse with Aizawa
                if (i >= 18) {{
                    const pulse = 1.0 + 0.3 * Math.sin(t * 57.0 + i);
                    m.scale.setScalar(pulse);
                }}
            }});

            // Update thrust arrow
            const tMag = Math.sqrt(thrust[0]**2 + thrust[1]**2 + thrust[2]**2);
            if (tMag > 0.01) {{
                arrow.setDirection(new THREE.Vector3(thrust[0], thrust[2], thrust[1]).normalize());
                arrow.setLength(Math.min(tMag * 10, 8), 0.5, 0.3);
                arrow.setColor(new THREE.Color().setHSL(0.35, 1.0, 0.5 + 0.3*Math.sin(t*3)));
            }}

            // Update Aizawa trail (edge nodes as orbiting points)
            for (let i = 0; i < 204; i++) {{
                const angle = (i / 204) * Math.PI * 2 + t * 0.5;
                const r = 6 + 2 * Math.sin(angle * 3 + t * 57.0/19.0);
                const y = 10 + 4 * Math.sin(t * 0.7 + i * 0.1);
                trailPositions[i*3]   = r * Math.cos(angle);
                trailPositions[i*3+1] = y;
                trailPositions[i*3+2] = r * Math.sin(angle);
            }}
            trailGeo.attributes.position.needsUpdate = true;

            // Rotate rods
            rods.rotation.y = t * 0.1;

            // HUD
            document.getElementById('bec').textContent = Math.round(50 + 50*Math.sin(t*0.5));
            document.getElementById('arc').textContent = ['Daemon','Sprite','Druid'][colorPhase];
            document.getElementById('thrust').textContent =
                thrust.map(v => v.toFixed(3)).join(', ');
            document.getElementById('frame').textContent = currentFrame;

            currentFrame = (currentFrame + 1) % virus_frames.length;
            renderer.render(scene, camera);
        }}

        window.addEventListener('resize', () => {{
            camera.aspect = innerWidth/innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(innerWidth, innerHeight);
        }});

        animate();
    </script></body></html>"""

    for fname in ["golden_virus_quasicrystal_vis.html",
                   "golden_virus_manifold_vis.html",
                   "golden_virus_combined_vis.html"]:
        with open(exp_path + fname, 'w') as f:
            f.write(html)

# ═══════════════════════════════════════════════════
# §7: MAIN
# ═══════════════════════════════════════════════════

if __name__ == "__main__":
    print("═" * 60)
    print("  GOLDEN TETRAHEDRON NANOBOT — Three-Field Propulsion")
    print("═" * 60)
    print(f"  Lattice: {N}³ = {TOTAL_NODES} nodes")
    print(f"  Interior (BEC): {INTERIOR_COUNT}")
    print(f"  Faces (shield):  {FACE_COUNT}")
    print(f"  Edges (Aizawa):  {EDGE_COUNT}")
    print(f"  Corners (anchor): {CORNER_COUNT}")
    print(f"  Strands:")
    print(f"    F₂₂₉: {ORD_229}=3×{COSET_229} modes, dark={DARK_229}")
    print(f"    F₁₈₁: {ORD_181}=3×{COSET_181} modes")
    print(f"    F₁₃‹: {ORD_139} modes (prime, indecomposable)")
    print(f"  Gaps: {GAP_12}={GAP_12//6}×6, {GAP_23}={GAP_23//6}×6")
    print(f"  Cross-field: 229 ≡ ω₁₈₁ = {P1 % P2}")
    print(f"  Golden algebra: φ·φ̄ = {round(_PHI * _PHI_BAR, 6)}")
    print()

    print("  Running simulation (pump_direction=0, hover mode)...")
    frames, thrust = simulate_nanobot(pump_direction=0)
    print(f"  Generated {len(frames)} frames.")

    import statistics
    thrust_mags = [math.sqrt(sum(t**2 for t in tv)) for tv in thrust]
    print(f"  Thrust magnitude: mean={statistics.mean(thrust_mags):.4f}, "
          f"max={max(thrust_mags):.4f}")

    print("  Generating visualizers...")
    generate_html(frames, thrust)
    print("  ✓ Three-field nanobot simulation complete.")
    print("  Output: ~/Desktop/Metamaterial_Research_Export/")
