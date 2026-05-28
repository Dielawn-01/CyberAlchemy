// Lean compiler output
// Module: CyberAlchemy.C46Unification
// Imports: public import Init public import CyberAlchemy.Basic public import Mathlib.Data.Real.Basic
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
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_C46Unification_iterate___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_C46Unification_iterate___redArg___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_C46Unification_iterate(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_C46Unification_iterate___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_C46Unification_wasserstein__distance__1d(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_C46Unification_wasserstein__distance__1d___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_C46Unification_iterate___redArg(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; uint8_t x_5; 
x_4 = lean_unsigned_to_nat(0u);
x_5 = lean_nat_dec_eq(x_2, x_4);
if (x_5 == 1)
{
lean_dec(x_1);
lean_inc(x_3);
return x_3;
}
else
{
lean_object* x_6; lean_object* x_7; lean_object* x_8; lean_object* x_9; 
x_6 = lean_unsigned_to_nat(1u);
x_7 = lean_nat_sub(x_2, x_6);
lean_inc(x_1);
x_8 = lp_CyberAlchemy_CyberAlchemy_C46Unification_iterate___redArg(x_1, x_7, x_3);
lean_dec(x_7);
x_9 = lean_apply_1(x_1, x_8);
return x_9;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_C46Unification_iterate___redArg___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; 
x_4 = lp_CyberAlchemy_CyberAlchemy_C46Unification_iterate___redArg(x_1, x_2, x_3);
lean_dec(x_3);
lean_dec(x_2);
return x_4;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_C46Unification_iterate(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
lean_object* x_5; 
x_5 = lp_CyberAlchemy_CyberAlchemy_C46Unification_iterate___redArg(x_2, x_3, x_4);
return x_5;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_C46Unification_iterate___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
lean_object* x_5; 
x_5 = lp_CyberAlchemy_CyberAlchemy_C46Unification_iterate(x_1, x_2, x_3, x_4);
lean_dec(x_4);
lean_dec(x_3);
return x_5;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_C46Unification_wasserstein__distance__1d(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
return x_3;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_C46Unification_wasserstein__distance__1d___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lp_CyberAlchemy_CyberAlchemy_C46Unification_wasserstein__distance__1d(x_1, x_2);
lean_dec(x_2);
lean_dec(x_1);
return x_3;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Real_Basic(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_C46Unification(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Real_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
