// Lean compiler output
// Module: CyberAlchemy.HoloneticNS
// Imports: public import Init public import Mathlib.Data.Real.Basic public import Mathlib.Tactic.Ring public import Mathlib.Tactic.NormNum public import Mathlib.Tactic.Linarith public import CyberAlchemy.ProtorealManifold public import CyberAlchemy.MassGap public import CyberAlchemy.CommutatorGap public import CyberAlchemy.ProtorealMandelbrot
#include <lean/lean.h>
#if defined(__clang__)
#pragma clang diagnostic ignored "-Wunused-parameter"
#pragma clang diagnostic ignored "-Wunused-label"
#elif defined(__GNUC__) && !defined(__CLANG__)
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-label"
#pragma GCC diagnostic ignored "-Wunused-but-set-variable"
#endif
#ifdef __cplusplus
extern "C" {
#endif
lean_object* lp_CyberAlchemy_ProtorealManifold_mul(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_convective(lean_object*);
lean_object* lp_CyberAlchemy_funct(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_viscous__step(lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_divergence(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_l__space__dim(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_l__space__dim___boxed(lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
lean_object* lean_nat_mul(lean_object*, lean_object*);
lean_object* lean_nat_shiftr(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_playing__field__couplings(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_playing__field__couplings___boxed(lean_object*);
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_project__to__3d(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_convective(lean_object* x_1) {
_start:
{
lean_object* x_2; 
lean_inc_ref(x_1);
x_2 = lp_CyberAlchemy_ProtorealManifold_mul(x_1, x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_viscous__step(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_funct(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_divergence(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; lean_object* x_4; lean_object* x_5; 
x_2 = lean_ctor_get(x_1, 1);
lean_inc(x_2);
x_3 = lean_ctor_get(x_1, 2);
lean_inc(x_3);
lean_dec_ref(x_1);
x_4 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_4, 0, x_3);
x_5 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_5, 0, x_2);
lean_closure_set(x_5, 1, x_4);
return x_5;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_l__space__dim(lean_object* x_1) {
_start:
{
lean_inc(x_1);
return x_1;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_l__space__dim___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_CyberAlchemy_HoloneticNS_l__space__dim(x_1);
lean_dec(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_playing__field__couplings(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; lean_object* x_4; lean_object* x_5; 
x_2 = lean_unsigned_to_nat(1u);
x_3 = lean_nat_sub(x_1, x_2);
x_4 = lean_nat_mul(x_1, x_3);
lean_dec(x_3);
x_5 = lean_nat_shiftr(x_4, x_2);
lean_dec(x_4);
return x_5;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_playing__field__couplings___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_CyberAlchemy_HoloneticNS_playing__field__couplings(x_1);
lean_dec(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_HoloneticNS_project__to__3d(lean_object* x_1) {
_start:
{
uint8_t x_2; 
x_2 = !lean_is_exclusive(x_1);
if (x_2 == 0)
{
lean_object* x_3; lean_object* x_4; lean_object* x_5; 
x_3 = lean_ctor_get(x_1, 4);
lean_dec(x_3);
x_4 = lean_ctor_get(x_1, 3);
lean_dec(x_4);
x_5 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
lean_ctor_set(x_1, 4, x_5);
lean_ctor_set(x_1, 3, x_5);
return x_1;
}
else
{
lean_object* x_6; lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; 
x_6 = lean_ctor_get(x_1, 0);
x_7 = lean_ctor_get(x_1, 1);
x_8 = lean_ctor_get(x_1, 2);
lean_inc(x_8);
lean_inc(x_7);
lean_inc(x_6);
lean_dec(x_1);
x_9 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
x_10 = lean_alloc_ctor(0, 5, 0);
lean_ctor_set(x_10, 0, x_6);
lean_ctor_set(x_10, 1, x_7);
lean_ctor_set(x_10, 2, x_8);
lean_ctor_set(x_10, 3, x_9);
lean_ctor_set(x_10, 4, x_9);
return x_10;
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Real_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_Ring(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_NormNum(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_Linarith(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_MassGap(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_CommutatorGap(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_HoloneticNS(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Real_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Tactic_Ring(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Tactic_NormNum(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Tactic_Linarith(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_MassGap(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_CommutatorGap(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
