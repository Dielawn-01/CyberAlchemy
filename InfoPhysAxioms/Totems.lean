import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.ProtorealOperator
import LaRueProtorealAlgebra.MonsterInverse
import InfoPhysAxioms.Infochemistry

/-!
# Canonical Test Points

Four distinguished manifold points spanning the algebra's behavior space.
Each demonstrates a different regime of the Klein product.
-/

open ProtorealManifold
open MonsterInverse
open Infochemistry

namespace Totems

/-- Grounded fixed point: parity-locked (b=m), zero noise, zero depth. -/
def wolverine : ProtorealManifold :=
  { a := 1, b := 1, m := 1, e := 0, l := 0 }

/-- Exploratory state: structured noise (e=1/5), parity tension (b!=m). -/
noncomputable def cuttlefish : ProtorealManifold :=
  { a := 1, b := 1, m := 4/5, e := 1/5, l := 1 }

/-- Parity projection of the exploratory state. Forces b=m. -/
noncomputable def cobra : ProtorealManifold :=
  parity_projection cuttlefish

/-- Monster inverse of the exploratory state. Perspective flip. -/
noncomputable def raven : ProtorealManifold :=
  monster_inv cuttlefish

/-- Bonded suspension of all four points. -/
noncomputable def dragon_suspension : ProtorealManifold :=
  bond (bond (bond wolverine cobra) raven) cuttlefish

/-- Grown suspension: funct of consolidated suspension. Noise = 0. -/
noncomputable def grown_dragon : ProtorealManifold :=
  funct (consolidate dragon_suspension)

theorem grown_dragon_is_coherent : grown_dragon.e = 0 := by
  unfold grown_dragon funct; rfl

/-- Integration: consolidate output, clear noise. -/
def integrate (u : ProtorealManifold) : ProtorealManifold :=
  { a := u.a, b := u.b + 1, m := u.m, e := 0, l := u.l }

/-- Iterative funct application. The overnight learning cycle. -/
noncomputable def dream_run (u : ProtorealManifold) (n : Nat) : ProtorealManifold :=
  (funct^[n]) u

/-- Dream then integrate. Always clears noise. -/
noncomputable def overnight_cycle (u : ProtorealManifold) (n : Nat) : ProtorealManifold :=
  integrate (dream_run u n)


def suppress (u : ProtorealManifold) : ProtorealManifold :=
  { a := u.a, b := u.b, m := u.m + 1, e := u.e, l := u.l }

def horn_gate (u : ProtorealManifold) (threshold : ℝ) : Prop :=
  u.e < threshold

def ivory_gate (u : ProtorealManifold) (threshold : ℝ) : Prop :=
  u.e ≥ threshold

theorem integration_passes_horn (u : ProtorealManifold) (t : ℝ) (ht : 0 < t) :
    horn_gate (integrate u) t := by
  unfold horn_gate integrate
  simp
  exact ht
end Totems
