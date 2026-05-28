// Lean compiler output
// Module: CyberAlchemy.LangSemantics
// Imports: public import Init public import Mathlib.Data.Real.Basic public import CyberAlchemy.ProtorealManifold public import CyberAlchemy.ProtorealNorm public import CyberAlchemy.ProtorealGraph
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
lean_object* lp_mathlib_Nat_cast___at___00Nat_cast___at___00Nat_cast___at___00NNReal_instSemiring_spec__1_spec__2_spec__3(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_Nat_cast___at___00LangSemantics_cpp__cost_spec__0(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_LangSemantics_cpp__cost(lean_object*);
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_LangSemantics_rust__cost(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_Nat_cast___at___00LangSemantics_cpp__cost_spec__0(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_mathlib_Nat_cast___at___00Nat_cast___at___00Nat_cast___at___00NNReal_instSemiring_spec__1_spec__2_spec__3(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_LangSemantics_cpp__cost(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_mathlib_Nat_cast___at___00Nat_cast___at___00Nat_cast___at___00NNReal_instSemiring_spec__1_spec__2_spec__3(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_LangSemantics_rust__cost(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; lean_object* x_4; lean_object* x_5; lean_object* x_6; 
x_3 = lp_mathlib_Nat_cast___at___00Nat_cast___at___00Nat_cast___at___00NNReal_instSemiring_spec__1_spec__2_spec__3(x_1);
x_4 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
x_5 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_5, 0, x_4);
lean_closure_set(x_5, 1, x_2);
x_6 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_6, 0, x_3);
lean_closure_set(x_6, 1, x_5);
return x_6;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Real_Basic(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealNorm(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealGraph(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_LangSemantics(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Real_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealNorm(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealGraph(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
