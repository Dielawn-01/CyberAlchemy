import LaRueProtorealAlgebra.Basic
import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.TemporalOperators
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

open ProtorealManifold
open LaRueProtorealAlgebra.TemporalOperators

def gns_star (u : ProtorealManifold) : ProtorealManifold :=
  { a := u.a + 2 * u.e, b := -u.m, m := u.b, e := -u.l, l := u.e }

def gns_omega (u : ProtorealManifold) : ℝ :=
  u.a

def in_null_space (u : ProtorealManifold) : Prop :=
  gns_omega (gns_star u * u) = 0

theorem gns_inner_product_expansion (u : ProtorealManifold) :
    gns_omega (gns_star u * u) = (u.a + u.e) * (u.a + u.e) + u.b * u.b + u.m * u.m + u.l * u.l := by
  unfold gns_omega gns_star
  simp
  ring

theorem gns_null_implies_aqft_kernel (u : ProtorealManifold) (h : in_null_space u) :
    superepsilon_depth u = 0 := by
  have h1 : gns_omega (gns_star u * u) = 0 := h
  rw [gns_inner_product_expansion] at h1
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

