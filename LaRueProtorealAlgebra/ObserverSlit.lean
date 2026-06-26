import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

/-!
# Observer Slit — Wave Interference Model
Models double-slit interference as a real-valued amplitude function
in the Protoreal observation framework.
-/

namespace ObserverSlit

/-- A monochromatic wave with amplitude and wavelength. -/
structure Wave where
  amplitude : ℝ
  wavelength : ℝ
  pos_wavelength : wavelength > 0

/-- A slit with position and width. -/
structure Slit where
  position : ℝ
  width : ℝ
  pos_width : width > 0

/-- The interference pattern at position x from two slits.
    Uses the cosine sum as a simplified interference model. -/
noncomputable def interference_pattern (wave : Wave) (slit1 slit2 : Slit) (x : ℝ) : ℝ :=
  wave.amplitude * (Real.cos ((x - slit1.position) / wave.wavelength) +
                    Real.cos ((x - slit2.position) / wave.wavelength))

end ObserverSlit