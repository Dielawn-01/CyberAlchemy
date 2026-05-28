// Lean compiler output
// Module: CyberAlchemy.TopologicalImaginary
// Imports: public import Init public import CyberAlchemy.ProtorealManifold public import Mathlib.Data.Real.Basic
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
lean_object* lp_mathlib_npowRec___at___00NNReal_instSemiring_spec__2(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_TopologicalImaginary_bridge__norm(lean_object*);
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
LEAN_EXPORT lean_object* lp_CyberAlchemy_TopologicalImaginary_symplectic__J(lean_object*);
extern lean_object* lp_CyberAlchemy_ProtorealManifold_iota;
extern lean_object* lp_CyberAlchemy_ProtorealManifold_omega;
lean_object* lp_CyberAlchemy_ProtorealManifold_mul(lean_object*, lean_object*);
static lean_once_cell_t lp_CyberAlchemy_TopologicalImaginary_bridge__root__of__unity__order__2___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_TopologicalImaginary_bridge__root__of__unity__order__2___closed__0;
LEAN_EXPORT lean_object* lp_CyberAlchemy_TopologicalImaginary_bridge__root__of__unity__order__2;
LEAN_EXPORT lean_object* lp_CyberAlchemy_TopologicalImaginary_bridge__norm(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; lean_object* x_4; lean_object* x_5; lean_object* x_6; lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; lean_object* x_11; lean_object* x_12; lean_object* x_13; 
x_2 = lean_ctor_get(x_1, 0);
lean_inc(x_2);
x_3 = lean_ctor_get(x_1, 1);
lean_inc(x_3);
x_4 = lean_ctor_get(x_1, 2);
lean_inc(x_4);
x_5 = lean_ctor_get(x_1, 3);
lean_inc(x_5);
x_6 = lean_ctor_get(x_1, 4);
lean_inc(x_6);
lean_dec_ref(x_1);
x_7 = lean_unsigned_to_nat(2u);
x_8 = lp_mathlib_npowRec___at___00NNReal_instSemiring_spec__2(x_7, x_2);
x_9 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_9, 0, x_3);
lean_closure_set(x_9, 1, x_4);
x_10 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_10, 0, x_8);
lean_closure_set(x_10, 1, x_9);
x_11 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_11, 0, x_5);
lean_closure_set(x_11, 1, x_6);
x_12 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_12, 0, x_11);
x_13 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_13, 0, x_10);
lean_closure_set(x_13, 1, x_12);
return x_13;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_TopologicalImaginary_symplectic__J(lean_object* x_1) {
_start:
{
uint8_t x_2; 
x_2 = !lean_is_exclusive(x_1);
if (x_2 == 0)
{
lean_object* x_3; lean_object* x_4; lean_object* x_5; lean_object* x_6; lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; 
x_3 = lean_ctor_get(x_1, 1);
x_4 = lean_ctor_get(x_1, 2);
x_5 = lean_ctor_get(x_1, 3);
x_6 = lean_ctor_get(x_1, 4);
x_7 = lean_ctor_get(x_1, 0);
lean_dec(x_7);
x_8 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
x_9 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_9, 0, x_3);
x_10 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_10, 0, x_5);
lean_ctor_set(x_1, 4, x_10);
lean_ctor_set(x_1, 3, x_6);
lean_ctor_set(x_1, 2, x_9);
lean_ctor_set(x_1, 1, x_4);
lean_ctor_set(x_1, 0, x_8);
return x_1;
}
else
{
lean_object* x_11; lean_object* x_12; lean_object* x_13; lean_object* x_14; lean_object* x_15; lean_object* x_16; lean_object* x_17; lean_object* x_18; 
x_11 = lean_ctor_get(x_1, 1);
x_12 = lean_ctor_get(x_1, 2);
x_13 = lean_ctor_get(x_1, 3);
x_14 = lean_ctor_get(x_1, 4);
lean_inc(x_14);
lean_inc(x_13);
lean_inc(x_12);
lean_inc(x_11);
lean_dec(x_1);
x_15 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
x_16 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_16, 0, x_11);
x_17 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_17, 0, x_13);
x_18 = lean_alloc_ctor(0, 5, 0);
lean_ctor_set(x_18, 0, x_15);
lean_ctor_set(x_18, 1, x_12);
lean_ctor_set(x_18, 2, x_16);
lean_ctor_set(x_18, 3, x_14);
lean_ctor_set(x_18, 4, x_17);
return x_18;
}
}
}
static lean_object* _init_lp_CyberAlchemy_TopologicalImaginary_bridge__root__of__unity__order__2___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lp_CyberAlchemy_ProtorealManifold_iota;
x_2 = lp_CyberAlchemy_ProtorealManifold_omega;
x_3 = lp_CyberAlchemy_ProtorealManifold_mul(x_2, x_1);
return x_3;
}
}
static lean_object* _init_lp_CyberAlchemy_TopologicalImaginary_bridge__root__of__unity__order__2(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_obj_once(&lp_CyberAlchemy_TopologicalImaginary_bridge__root__of__unity__order__2___closed__0, &lp_CyberAlchemy_TopologicalImaginary_bridge__root__of__unity__order__2___closed__0_once, _init_lp_CyberAlchemy_TopologicalImaginary_bridge__root__of__unity__order__2___closed__0);
return x_1;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Real_Basic(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_TopologicalImaginary(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Real_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_TopologicalImaginary_bridge__root__of__unity__order__2 = _init_lp_CyberAlchemy_TopologicalImaginary_bridge__root__of__unity__order__2();
lean_mark_persistent(lp_CyberAlchemy_TopologicalImaginary_bridge__root__of__unity__order__2);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
