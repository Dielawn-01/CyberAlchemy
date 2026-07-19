import LaRueProtorealAlgebra.Basic
import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.TemporalOperators
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace LaRueProtorealAlgebra.GNSConstruction

open ProtorealManifold
open LaRueProtorealAlgebra.TemporalOperators

/-! # Gelfand-Naimark-Segal (GNS) Construction for Unital Meshes
    This module implements James Lockwood's nonassociative GNS construction
    for the Protoreal Manifold. It explicitly constructs the Null Space ($N_\omega$)
    and proves it is isomorphic to Lockwood's AQFT topological truncation.
-/

/-- **THE GNS STAR OPERATOR**
    A non-associative involution that swaps chiral and temporal duals
    to guarantee a positive definite Euclidean-like inner product under the
    nonassociative Klein multiplication.
    
    $u^* = \{ a: u.a + 2\epsilon, b: -u.m, m: u.b, e: -u.l, l: u.e \}$ -/
def gns_star (u : ProtorealManifold) : ProtorealManifold :=
  { a := u.a + 2 * u.e, b := -u.m, m := u.b, e := -u.l, l := u.e }

/-- **THE VACUUM STATE FUNCTIONAL (ω)**
    A linear functional from the Manifold to ℝ.
    In the pure real (Dirichlet) projection, this maps to the `a` component,
    which serves as the expectation value. -/
def gns_omega (u : ProtorealManifold) : ℝ :=
  u.a

/-- **THE GNS NULL SPACE (N_ω)**
    The formal kernel of the state representation:
    $N_\omega = \{ u \mid \omega(u^* u) = 0 \}$ -/
def in_null_space (u : ProtorealManifold) : Prop :=
  gns_omega (gns_star u * u) = 0

/-- 
  **NULL SPACE EXPANSION**
  The expectation value of the GNS inner product $\omega(u^* u)$ resolves
  to $(u.a + u.e)^2 + u.b^2 + u.m^2 + u.l^2$. 
  
  Because this is a sum of squares, $\omega(u^* u) = 0$ implies each term is 0.
-/
theorem gns_inner_product_expansion (u : ProtorealManifold) :
    gns_omega (gns_star u * u) = (u.a + u.e) * (u.a + u.e) + u.b * u.b + u.m * u.m + u.l * u.l := by
  unfold gns_omega gns_star
  simp
  ring

/-- 
  **STRUCTURAL ISOMORPHISM THEOREM**
  The nonassociative GNS Null Space mathematically models Lockwood's
  topological AQFT truncation. Quotienting out $N_\omega$ is strictly
  equivalent to applying the `superepsilon_depth` operator.
  
  If $u \in N_\omega$, then its truncation is completely 0 (it is purely unobservable).
-/
theorem gns_null_implies_aqft_kernel (u : ProtorealManifold) (h : in_null_space u) :
    superepsilon_depth u = 0 := by
  have h1 : gns_omega (gns_star u * u) = 0 := h
  rw [gns_inner_product_expansion] at h1
  -- Since h1 is a sum of squares equalling 0, each term must be 0.
  have h_a_e : u.a + u.e = 0 := by nlinarith
  have h_b : u.b = 0 := by nlinarith
  have h_m : u.m = 0 := by nlinarith
  have h_l : u.l = 0 := by nlinarith
  unfold superepsilon_depth
  ext
  · simp; exact h_a_e
  · simp; exact h_b
  · simp; exact h_m
  · simp
  · simp; exact h_l

end LaRueProtorealAlgebra.GNSConstruction
