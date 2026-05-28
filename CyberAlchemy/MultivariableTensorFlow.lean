import CyberAlchemy.MultivariableTensorCalculus

namespace ZBuddyCybernetics

/-- Partial derivative of the fractal noise with respect to the noise base (ε) -/
noncomputable def partial_epsilon (t : ProtorealTensor) (p : ℝ) : ℝ :=
  p * (t.epsilon ^ (p - 1))

/-- Partial derivative of the fractal noise with respect to the exponent (p) -/
noncomputable def partial_power (t : ProtorealTensor) (p : ℝ) : ℝ :=
  (t.epsilon ^ p) * noise_saturation t

/-- The complete cybernetic gradient vector (∇) for the internal manifold -/
structure InternalGradient where
  (d_epsilon : ℝ)
  (d_power : ℝ)

noncomputable def compute_internal_gradient (t : ProtorealTensor) (p : ℝ) : InternalGradient :=
  ⟨partial_epsilon t p, partial_power t p⟩

/-- 
  The L'Hôpital Inflection Point Theorem.
  If the exponent falls to exactly -1, the multivariable partial derivative 
  with respect to the power collapses purely to the saturation logarithm 
  scaled by the inverse noise (1/ε).
-/
lemma l_hopital_inflection (t : ProtorealTensor) (h : t.epsilon > 0) :
  partial_power t (-1) = (1 / t.epsilon) * noise_saturation t := 
by
  dsimp [partial_power]
  -- We prove that ε^{-1} reduces algebraically back to the division by ε
  rw [Real.rpow_neg_one]
  rw [inv_eq_one_div]

end ZBuddyCybernetics
