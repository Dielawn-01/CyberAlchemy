// Lean compiler output
// Module: CyberAlchemy.ParityStability
// Imports: public import Init public import CyberAlchemy.ProtorealManifold public import CyberAlchemy.DualityTheorem public import CyberAlchemy.MonsterInverse public import CyberAlchemy.ProtorealOperator
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
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_npowRec___at___00Cardinal_cantorFunctionAux_spec__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealAlgebra_parity__tension(lean_object*);
lean_object* lp_CyberAlchemy_DualityTheorem_standard__resonance(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealAlgebra_spectral__energy(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealAlgebra_parity__tension(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; lean_object* x_4; lean_object* x_5; lean_object* x_6; lean_object* x_7; 
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
x_6 = lean_unsigned_to_nat(2u);
x_7 = lp_mathlib_npowRec___at___00Cardinal_cantorFunctionAux_spec__0(x_6, x_5);
return x_7;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealAlgebra_spectral__energy(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; lean_object* x_4; lean_object* x_5; lean_object* x_6; 
lean_inc_ref(x_1);
x_2 = lp_CyberAlchemy_DualityTheorem_standard__resonance(x_1);
x_3 = lean_unsigned_to_nat(2u);
x_4 = lp_mathlib_npowRec___at___00Cardinal_cantorFunctionAux_spec__0(x_3, x_2);
x_5 = lp_CyberAlchemy_ProtorealAlgebra_parity__tension(x_1);
x_6 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_6, 0, x_4);
lean_closure_set(x_6, 1, x_5);
return x_6;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_DualityTheorem(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_MonsterInverse(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealOperator(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_ParityStability(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_DualityTheorem(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_MonsterInverse(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealOperator(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
