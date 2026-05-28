// Lean compiler output
// Module: CyberAlchemy.SpectralFiber
// Imports: public import Init public import CyberAlchemy.RiemannFunctionalEquation public import CyberAlchemy.SpectralFixedPoint public import CyberAlchemy.StructuralHeterogeneity
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
lean_object* lp_CyberAlchemy_Nat_cast___at___00Nat_cast___at___00Nat_cast___at___00consolidate_spec__0_spec__0_spec__1(lean_object*);
static lean_once_cell_t lp_CyberAlchemy_SpectralFiber_conic__discriminant___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_SpectralFiber_conic__discriminant___closed__0;
lean_object* lp_mathlib_npowRec___at___00Cardinal_cantorFunctionAux_spec__0(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_SpectralFiber_conic__discriminant(lean_object*, lean_object*, lean_object*);
static lean_object* _init_lp_CyberAlchemy_SpectralFiber_conic__discriminant___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; 
x_1 = lean_unsigned_to_nat(4u);
x_2 = lp_CyberAlchemy_Nat_cast___at___00Nat_cast___at___00Nat_cast___at___00consolidate_spec__0_spec__0_spec__1(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_SpectralFiber_conic__discriminant(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; lean_object* x_5; lean_object* x_6; lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; 
x_4 = lean_unsigned_to_nat(2u);
x_5 = lp_mathlib_npowRec___at___00Cardinal_cantorFunctionAux_spec__0(x_4, x_2);
x_6 = lean_obj_once(&lp_CyberAlchemy_SpectralFiber_conic__discriminant___closed__0, &lp_CyberAlchemy_SpectralFiber_conic__discriminant___closed__0_once, _init_lp_CyberAlchemy_SpectralFiber_conic__discriminant___closed__0);
x_7 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_7, 0, x_6);
lean_closure_set(x_7, 1, x_1);
x_8 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_8, 0, x_7);
lean_closure_set(x_8, 1, x_3);
x_9 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_9, 0, x_8);
x_10 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_10, 0, x_5);
lean_closure_set(x_10, 1, x_9);
return x_10;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_RiemannFunctionalEquation(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_SpectralFixedPoint(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_StructuralHeterogeneity(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_SpectralFiber(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_RiemannFunctionalEquation(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_SpectralFixedPoint(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_StructuralHeterogeneity(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
