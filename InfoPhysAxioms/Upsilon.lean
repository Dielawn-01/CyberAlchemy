import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.MonsterInverse

/-!
# Upsilon Operator

The parity-locking operator. Forces b = m (parity lock) on any manifold point.
Idempotent: applying twice is the same as applying once.
-/

open ProtorealManifold
open MonsterInverse

namespace Upsilon

/-- Upsilon: force parity lock via projection. -/
noncomputable def upsilon (u : ProtorealManifold) : ProtorealManifold :=
  parity_projection u

theorem upsilon_locks_parity (u : ProtorealManifold) :
    (upsilon u).b = (upsilon u).m := by
  unfold upsilon parity_projection; ring

theorem upsilon_achieves_resonance (u : ProtorealManifold) :
    (upsilon u).b - (upsilon u).m = 0 := by
  have h := upsilon_locks_parity u; linarith

theorem upsilon_preserves_base (u : ProtorealManifold) :
    (upsilon u).a = u.a := by
  unfold upsilon parity_projection; ring

theorem upsilon_preserves_noise (u : ProtorealManifold) :
    (upsilon u).e = u.e := by
  unfold upsilon parity_projection; ring

theorem upsilon_preserves_depth (u : ProtorealManifold) :
    (upsilon u).l = u.l := by
  unfold upsilon parity_projection; ring

theorem upsilon_idempotent (u : ProtorealManifold) :
    upsilon (upsilon u) = upsilon u := by
  unfold upsilon parity_projection
  ext <;> simp <;> ring

end Upsilon
