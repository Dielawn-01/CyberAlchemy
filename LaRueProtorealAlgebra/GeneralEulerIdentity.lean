import Mathlib.Algebra.Group.Basic
import LaRueProtorealAlgebra.ArithmeticTypeTheory

set_option linter.all false

namespace LaRueProtorealAlgebra.GeneralEulerIdentity

variable [CyberAlchemy.ArithmeticTypeTheory]

def Constant [CyberAlchemy.ArithmeticTypeTheory] : Type := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{1}
def e [CyberAlchemy.ArithmeticTypeTheory] : Constant := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}
def i [CyberAlchemy.ArithmeticTypeTheory] : Constant := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}
def pi [CyberAlchemy.ArithmeticTypeTheory] : Constant := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}
def one [CyberAlchemy.ArithmeticTypeTheory] : Constant := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}
def zero [CyberAlchemy.ArithmeticTypeTheory] : Constant := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}
def phi [CyberAlchemy.ArithmeticTypeTheory] : Constant := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}
def alpha [CyberAlchemy.ArithmeticTypeTheory] : Constant := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}

def add [CyberAlchemy.ArithmeticTypeTheory] : Constant → Constant → Constant := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}
infixl:65 " + " => add

def sub [CyberAlchemy.ArithmeticTypeTheory] : Constant → Constant → Constant := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}
infixl:65 " - " => sub

def mul [CyberAlchemy.ArithmeticTypeTheory] : Constant → Constant → Constant := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}
infixl:70 " * " => mul

def div [CyberAlchemy.ArithmeticTypeTheory] : Constant → Constant → Constant := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}
infixl:70 " / " => div

def exp [CyberAlchemy.ArithmeticTypeTheory] : Constant → Constant → Constant := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}
notation:max base "^" exponent => exp base exponent

def ten [CyberAlchemy.ArithmeticTypeTheory] : Constant := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}
def twenty_seven [CyberAlchemy.ArithmeticTypeTheory] : Constant := CyberAlchemy.ArithmeticTypeTheory.blurr_type.{0}

def rarefied_alpha_identity [CyberAlchemy.ArithmeticTypeTheory] :
  (one / alpha) = (e ^ (phi * phi)) * (ten - (one / (twenty_seven * (pi * pi)))) := CyberAlchemy.ArithmeticTypeTheory.blurr_prop

end LaRueProtorealAlgebra.GeneralEulerIdentity
