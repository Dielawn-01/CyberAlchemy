// Lean compiler output
// Module: CyberAlchemy.AgenticFrame
// Imports: public import Init public import CyberAlchemy.ProtorealMesh public import CyberAlchemy.ProtorealOperator public import CyberAlchemy.ProtorealAlgebra
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
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_AgenticFrame_intuition(lean_object*);
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
lean_object* lp_mathlib_Complex_ofReal(lean_object*);
static lean_once_cell_t lp_CyberAlchemy_AgenticFrame_agent__origin___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_AgenticFrame_agent__origin___closed__0;
extern lean_object* lp_CyberAlchemy_ProtorealManifold_omega;
static lean_once_cell_t lp_CyberAlchemy_AgenticFrame_agent__origin___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_AgenticFrame_agent__origin___closed__1;
extern lean_object* lp_CyberAlchemy_ProtorealManifold_iota;
static lean_once_cell_t lp_CyberAlchemy_AgenticFrame_agent__origin___closed__2_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_AgenticFrame_agent__origin___closed__2;
static lean_once_cell_t lp_CyberAlchemy_AgenticFrame_agent__origin___closed__3_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_AgenticFrame_agent__origin___closed__3;
LEAN_EXPORT lean_object* lp_CyberAlchemy_AgenticFrame_agent__origin;
LEAN_EXPORT lean_object* lp_CyberAlchemy_AgenticFrame_intuition(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; lean_object* x_4; lean_object* x_5; lean_object* x_6; uint8_t x_7; 
x_2 = lean_ctor_get(x_1, 0);
lean_inc_ref(x_2);
x_3 = lean_ctor_get(x_1, 1);
lean_inc_ref(x_3);
lean_dec_ref(x_1);
x_4 = lean_ctor_get(x_2, 1);
lean_inc_ref(x_4);
x_5 = lean_ctor_get(x_3, 1);
lean_inc_ref(x_5);
x_6 = lean_ctor_get(x_2, 0);
lean_inc_ref(x_6);
lean_dec_ref(x_2);
x_7 = !lean_is_exclusive(x_3);
if (x_7 == 0)
{
lean_object* x_8; lean_object* x_9; lean_object* x_10; lean_object* x_11; uint8_t x_12; 
x_8 = lean_ctor_get(x_3, 0);
x_9 = lean_ctor_get(x_3, 1);
lean_dec(x_9);
x_10 = lean_ctor_get(x_4, 0);
lean_inc(x_10);
x_11 = lean_ctor_get(x_4, 1);
lean_inc(x_11);
lean_dec_ref(x_4);
x_12 = !lean_is_exclusive(x_5);
if (x_12 == 0)
{
lean_object* x_13; lean_object* x_14; lean_object* x_15; lean_object* x_16; lean_object* x_17; lean_object* x_18; lean_object* x_19; lean_object* x_20; lean_object* x_21; lean_object* x_22; 
x_13 = lean_ctor_get(x_5, 0);
x_14 = lean_ctor_get(x_5, 1);
x_15 = lp_CyberAlchemy_ProtorealManifold_mul(x_6, x_8);
lean_inc(x_13);
lean_inc(x_10);
x_16 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_16, 0, x_10);
lean_closure_set(x_16, 1, x_13);
lean_inc(x_14);
lean_inc(x_11);
x_17 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_17, 0, x_11);
lean_closure_set(x_17, 1, x_14);
x_18 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_18, 0, x_17);
x_19 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_19, 0, x_16);
lean_closure_set(x_19, 1, x_18);
x_20 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_20, 0, x_10);
lean_closure_set(x_20, 1, x_14);
x_21 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_21, 0, x_11);
lean_closure_set(x_21, 1, x_13);
x_22 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_22, 0, x_20);
lean_closure_set(x_22, 1, x_21);
lean_ctor_set(x_5, 1, x_22);
lean_ctor_set(x_5, 0, x_19);
lean_ctor_set(x_3, 0, x_15);
return x_3;
}
else
{
lean_object* x_23; lean_object* x_24; lean_object* x_25; lean_object* x_26; lean_object* x_27; lean_object* x_28; lean_object* x_29; lean_object* x_30; lean_object* x_31; lean_object* x_32; lean_object* x_33; 
x_23 = lean_ctor_get(x_5, 0);
x_24 = lean_ctor_get(x_5, 1);
lean_inc(x_24);
lean_inc(x_23);
lean_dec(x_5);
x_25 = lp_CyberAlchemy_ProtorealManifold_mul(x_6, x_8);
lean_inc(x_23);
lean_inc(x_10);
x_26 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_26, 0, x_10);
lean_closure_set(x_26, 1, x_23);
lean_inc(x_24);
lean_inc(x_11);
x_27 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_27, 0, x_11);
lean_closure_set(x_27, 1, x_24);
x_28 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_28, 0, x_27);
x_29 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_29, 0, x_26);
lean_closure_set(x_29, 1, x_28);
x_30 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_30, 0, x_10);
lean_closure_set(x_30, 1, x_24);
x_31 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_31, 0, x_11);
lean_closure_set(x_31, 1, x_23);
x_32 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_32, 0, x_30);
lean_closure_set(x_32, 1, x_31);
x_33 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_33, 0, x_29);
lean_ctor_set(x_33, 1, x_32);
lean_ctor_set(x_3, 1, x_33);
lean_ctor_set(x_3, 0, x_25);
return x_3;
}
}
else
{
lean_object* x_34; lean_object* x_35; lean_object* x_36; lean_object* x_37; lean_object* x_38; lean_object* x_39; lean_object* x_40; lean_object* x_41; lean_object* x_42; lean_object* x_43; lean_object* x_44; lean_object* x_45; lean_object* x_46; lean_object* x_47; lean_object* x_48; lean_object* x_49; 
x_34 = lean_ctor_get(x_3, 0);
lean_inc(x_34);
lean_dec(x_3);
x_35 = lean_ctor_get(x_4, 0);
lean_inc(x_35);
x_36 = lean_ctor_get(x_4, 1);
lean_inc(x_36);
lean_dec_ref(x_4);
x_37 = lean_ctor_get(x_5, 0);
lean_inc(x_37);
x_38 = lean_ctor_get(x_5, 1);
lean_inc(x_38);
if (lean_is_exclusive(x_5)) {
 lean_ctor_release(x_5, 0);
 lean_ctor_release(x_5, 1);
 x_39 = x_5;
} else {
 lean_dec_ref(x_5);
 x_39 = lean_box(0);
}
x_40 = lp_CyberAlchemy_ProtorealManifold_mul(x_6, x_34);
lean_inc(x_37);
lean_inc(x_35);
x_41 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_41, 0, x_35);
lean_closure_set(x_41, 1, x_37);
lean_inc(x_38);
lean_inc(x_36);
x_42 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_42, 0, x_36);
lean_closure_set(x_42, 1, x_38);
x_43 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_43, 0, x_42);
x_44 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_44, 0, x_41);
lean_closure_set(x_44, 1, x_43);
x_45 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_45, 0, x_35);
lean_closure_set(x_45, 1, x_38);
x_46 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_46, 0, x_36);
lean_closure_set(x_46, 1, x_37);
x_47 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_47, 0, x_45);
lean_closure_set(x_47, 1, x_46);
if (lean_is_scalar(x_39)) {
 x_48 = lean_alloc_ctor(0, 2, 0);
} else {
 x_48 = x_39;
}
lean_ctor_set(x_48, 0, x_44);
lean_ctor_set(x_48, 1, x_47);
x_49 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_49, 0, x_40);
lean_ctor_set(x_49, 1, x_48);
return x_49;
}
}
}
static lean_object* _init_lp_CyberAlchemy_AgenticFrame_agent__origin___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; 
x_1 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
x_2 = lp_mathlib_Complex_ofReal(x_1);
return x_2;
}
}
static lean_object* _init_lp_CyberAlchemy_AgenticFrame_agent__origin___closed__1(void) {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lean_obj_once(&lp_CyberAlchemy_AgenticFrame_agent__origin___closed__0, &lp_CyberAlchemy_AgenticFrame_agent__origin___closed__0_once, _init_lp_CyberAlchemy_AgenticFrame_agent__origin___closed__0);
x_2 = lp_CyberAlchemy_ProtorealManifold_omega;
x_3 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_3, 0, x_2);
lean_ctor_set(x_3, 1, x_1);
return x_3;
}
}
static lean_object* _init_lp_CyberAlchemy_AgenticFrame_agent__origin___closed__2(void) {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lean_obj_once(&lp_CyberAlchemy_AgenticFrame_agent__origin___closed__0, &lp_CyberAlchemy_AgenticFrame_agent__origin___closed__0_once, _init_lp_CyberAlchemy_AgenticFrame_agent__origin___closed__0);
x_2 = lp_CyberAlchemy_ProtorealManifold_iota;
x_3 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_3, 0, x_2);
lean_ctor_set(x_3, 1, x_1);
return x_3;
}
}
static lean_object* _init_lp_CyberAlchemy_AgenticFrame_agent__origin___closed__3(void) {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lean_obj_once(&lp_CyberAlchemy_AgenticFrame_agent__origin___closed__2, &lp_CyberAlchemy_AgenticFrame_agent__origin___closed__2_once, _init_lp_CyberAlchemy_AgenticFrame_agent__origin___closed__2);
x_2 = lean_obj_once(&lp_CyberAlchemy_AgenticFrame_agent__origin___closed__1, &lp_CyberAlchemy_AgenticFrame_agent__origin___closed__1_once, _init_lp_CyberAlchemy_AgenticFrame_agent__origin___closed__1);
x_3 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_3, 0, x_2);
lean_ctor_set(x_3, 1, x_1);
return x_3;
}
}
static lean_object* _init_lp_CyberAlchemy_AgenticFrame_agent__origin(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_obj_once(&lp_CyberAlchemy_AgenticFrame_agent__origin___closed__3, &lp_CyberAlchemy_AgenticFrame_agent__origin___closed__3_once, _init_lp_CyberAlchemy_AgenticFrame_agent__origin___closed__3);
return x_1;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealMesh(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealOperator(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealAlgebra(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_AgenticFrame(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealMesh(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealOperator(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealAlgebra(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_AgenticFrame_agent__origin = _init_lp_CyberAlchemy_AgenticFrame_agent__origin();
lean_mark_persistent(lp_CyberAlchemy_AgenticFrame_agent__origin);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
