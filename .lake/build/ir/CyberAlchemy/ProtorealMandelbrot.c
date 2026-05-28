// Lean compiler output
// Module: CyberAlchemy.ProtorealMandelbrot
// Imports: public import Init public import Mathlib.Data.Real.Basic public import Mathlib.Tactic.Ring public import Mathlib.Tactic.NormNum public import Mathlib.Tactic.Linarith public import CyberAlchemy.ProtorealManifold
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
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_klein__square(lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__step(lean_object*, lean_object*);
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
static lean_once_cell_t lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit___closed__0;
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit___boxed(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_norm__sq(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit_match__1_splitter___redArg(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit_match__1_splitter___redArg___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit_match__1_splitter(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit_match__1_splitter___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_left__orbit(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_left__orbit___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_right__orbit(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_right__orbit___boxed(lean_object*, lean_object*);
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
static lean_once_cell_t lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_witness__c___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_witness__c___closed__0;
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_witness__c;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_klein__square(lean_object* x_1) {
_start:
{
lean_object* x_2; 
lean_inc_ref(x_1);
x_2 = lp_CyberAlchemy_ProtorealManifold_mul(x_1, x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__step(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; lean_object* x_4; lean_object* x_5; lean_object* x_6; lean_object* x_7; lean_object* x_8; uint8_t x_9; 
lean_inc_ref(x_1);
x_3 = lp_CyberAlchemy_ProtorealManifold_mul(x_1, x_1);
x_4 = lean_ctor_get(x_3, 0);
lean_inc(x_4);
x_5 = lean_ctor_get(x_3, 1);
lean_inc(x_5);
x_6 = lean_ctor_get(x_3, 2);
lean_inc(x_6);
x_7 = lean_ctor_get(x_3, 3);
lean_inc(x_7);
x_8 = lean_ctor_get(x_3, 4);
lean_inc(x_8);
lean_dec_ref(x_3);
x_9 = !lean_is_exclusive(x_2);
if (x_9 == 0)
{
lean_object* x_10; lean_object* x_11; lean_object* x_12; lean_object* x_13; lean_object* x_14; lean_object* x_15; lean_object* x_16; lean_object* x_17; lean_object* x_18; lean_object* x_19; 
x_10 = lean_ctor_get(x_2, 0);
x_11 = lean_ctor_get(x_2, 1);
x_12 = lean_ctor_get(x_2, 2);
x_13 = lean_ctor_get(x_2, 3);
x_14 = lean_ctor_get(x_2, 4);
x_15 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_15, 0, x_4);
lean_closure_set(x_15, 1, x_10);
x_16 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_16, 0, x_5);
lean_closure_set(x_16, 1, x_11);
x_17 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_17, 0, x_6);
lean_closure_set(x_17, 1, x_12);
x_18 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_18, 0, x_7);
lean_closure_set(x_18, 1, x_13);
x_19 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_19, 0, x_8);
lean_closure_set(x_19, 1, x_14);
lean_ctor_set(x_2, 4, x_19);
lean_ctor_set(x_2, 3, x_18);
lean_ctor_set(x_2, 2, x_17);
lean_ctor_set(x_2, 1, x_16);
lean_ctor_set(x_2, 0, x_15);
return x_2;
}
else
{
lean_object* x_20; lean_object* x_21; lean_object* x_22; lean_object* x_23; lean_object* x_24; lean_object* x_25; lean_object* x_26; lean_object* x_27; lean_object* x_28; lean_object* x_29; lean_object* x_30; 
x_20 = lean_ctor_get(x_2, 0);
x_21 = lean_ctor_get(x_2, 1);
x_22 = lean_ctor_get(x_2, 2);
x_23 = lean_ctor_get(x_2, 3);
x_24 = lean_ctor_get(x_2, 4);
lean_inc(x_24);
lean_inc(x_23);
lean_inc(x_22);
lean_inc(x_21);
lean_inc(x_20);
lean_dec(x_2);
x_25 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_25, 0, x_4);
lean_closure_set(x_25, 1, x_20);
x_26 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_26, 0, x_5);
lean_closure_set(x_26, 1, x_21);
x_27 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_27, 0, x_6);
lean_closure_set(x_27, 1, x_22);
x_28 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_28, 0, x_7);
lean_closure_set(x_28, 1, x_23);
x_29 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_29, 0, x_8);
lean_closure_set(x_29, 1, x_24);
x_30 = lean_alloc_ctor(0, 5, 0);
lean_ctor_set(x_30, 0, x_25);
lean_ctor_set(x_30, 1, x_26);
lean_ctor_set(x_30, 2, x_27);
lean_ctor_set(x_30, 3, x_28);
lean_ctor_set(x_30, 4, x_29);
return x_30;
}
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; 
x_1 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
x_2 = lean_alloc_ctor(0, 5, 0);
lean_ctor_set(x_2, 0, x_1);
lean_ctor_set(x_2, 1, x_1);
lean_ctor_set(x_2, 2, x_1);
lean_ctor_set(x_2, 3, x_1);
lean_ctor_set(x_2, 4, x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; uint8_t x_4; 
x_3 = lean_unsigned_to_nat(0u);
x_4 = lean_nat_dec_eq(x_2, x_3);
if (x_4 == 1)
{
lean_object* x_5; 
lean_dec_ref(x_1);
x_5 = lean_obj_once(&lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit___closed__0, &lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit___closed__0_once, _init_lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit___closed__0);
return x_5;
}
else
{
lean_object* x_6; lean_object* x_7; lean_object* x_8; lean_object* x_9; 
x_6 = lean_unsigned_to_nat(1u);
x_7 = lean_nat_sub(x_2, x_6);
lean_inc_ref(x_1);
x_8 = lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit(x_1, x_7);
lean_dec(x_7);
x_9 = lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__step(x_8, x_1);
return x_9;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit(x_1, x_2);
lean_dec(x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_norm__sq(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; lean_object* x_4; lean_object* x_5; lean_object* x_6; lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; lean_object* x_11; lean_object* x_12; lean_object* x_13; lean_object* x_14; lean_object* x_15; 
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
lean_inc(x_2);
x_7 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_7, 0, x_2);
lean_closure_set(x_7, 1, x_2);
lean_inc(x_3);
x_8 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_8, 0, x_3);
lean_closure_set(x_8, 1, x_3);
x_9 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_9, 0, x_7);
lean_closure_set(x_9, 1, x_8);
lean_inc(x_4);
x_10 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_10, 0, x_4);
lean_closure_set(x_10, 1, x_4);
x_11 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_11, 0, x_9);
lean_closure_set(x_11, 1, x_10);
lean_inc(x_5);
x_12 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_12, 0, x_5);
lean_closure_set(x_12, 1, x_5);
x_13 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_13, 0, x_11);
lean_closure_set(x_13, 1, x_12);
lean_inc(x_6);
x_14 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_14, 0, x_6);
lean_closure_set(x_14, 1, x_6);
x_15 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_15, 0, x_13);
lean_closure_set(x_15, 1, x_14);
return x_15;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit_match__1_splitter___redArg(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; uint8_t x_5; 
x_4 = lean_unsigned_to_nat(0u);
x_5 = lean_nat_dec_eq(x_1, x_4);
if (x_5 == 1)
{
lean_object* x_6; lean_object* x_7; 
lean_dec(x_3);
x_6 = lean_box(0);
x_7 = lean_apply_1(x_2, x_6);
return x_7;
}
else
{
lean_object* x_8; lean_object* x_9; lean_object* x_10; 
lean_dec(x_2);
x_8 = lean_unsigned_to_nat(1u);
x_9 = lean_nat_sub(x_1, x_8);
x_10 = lean_apply_1(x_3, x_9);
return x_10;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit_match__1_splitter___redArg___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; 
x_4 = lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit_match__1_splitter___redArg(x_1, x_2, x_3);
lean_dec(x_1);
return x_4;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit_match__1_splitter(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
lean_object* x_5; uint8_t x_6; 
x_5 = lean_unsigned_to_nat(0u);
x_6 = lean_nat_dec_eq(x_2, x_5);
if (x_6 == 1)
{
lean_object* x_7; lean_object* x_8; 
lean_dec(x_4);
x_7 = lean_box(0);
x_8 = lean_apply_1(x_3, x_7);
return x_8;
}
else
{
lean_object* x_9; lean_object* x_10; lean_object* x_11; 
lean_dec(x_3);
x_9 = lean_unsigned_to_nat(1u);
x_10 = lean_nat_sub(x_2, x_9);
x_11 = lean_apply_1(x_4, x_10);
return x_11;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit_match__1_splitter___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
lean_object* x_5; 
x_5 = lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_mandelbrot__orbit_match__1_splitter(x_1, x_2, x_3, x_4);
lean_dec(x_2);
return x_5;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_left__orbit(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; uint8_t x_4; 
x_3 = lean_unsigned_to_nat(0u);
x_4 = lean_nat_dec_eq(x_2, x_3);
if (x_4 == 1)
{
return x_1;
}
else
{
lean_object* x_5; lean_object* x_6; lean_object* x_7; lean_object* x_8; 
x_5 = lean_unsigned_to_nat(1u);
x_6 = lean_nat_sub(x_2, x_5);
lean_inc_ref(x_1);
x_7 = lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_left__orbit(x_1, x_6);
lean_dec(x_6);
x_8 = lp_CyberAlchemy_ProtorealManifold_mul(x_7, x_1);
return x_8;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_left__orbit___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_left__orbit(x_1, x_2);
lean_dec(x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_right__orbit(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; uint8_t x_4; 
x_3 = lean_unsigned_to_nat(0u);
x_4 = lean_nat_dec_eq(x_2, x_3);
if (x_4 == 1)
{
return x_1;
}
else
{
lean_object* x_5; lean_object* x_6; lean_object* x_7; lean_object* x_8; 
x_5 = lean_unsigned_to_nat(1u);
x_6 = lean_nat_sub(x_2, x_5);
lean_inc_ref(x_1);
x_7 = lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_right__orbit(x_1, x_6);
lean_dec(x_6);
x_8 = lp_CyberAlchemy_ProtorealManifold_mul(x_1, x_7);
return x_8;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_right__orbit___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lp_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot_right__orbit(x_1, x_2);
lean_dec(x_2);
return x_3;
}
}
static lean_object* _init_lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_witness__c___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
x_2 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
x_3 = lean_alloc_ctor(0, 5, 0);
lean_ctor_set(x_3, 0, x_2);
lean_ctor_set(x_3, 1, x_2);
lean_ctor_set(x_3, 2, x_2);
lean_ctor_set(x_3, 3, x_1);
lean_ctor_set(x_3, 4, x_1);
return x_3;
}
}
static lean_object* _init_lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_witness__c(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_obj_once(&lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_witness__c___closed__0, &lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_witness__c___closed__0_once, _init_lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_witness__c___closed__0);
return x_1;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Real_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_Ring(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_NormNum(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_Linarith(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealMandelbrot(uint8_t builtin) {
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
lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_witness__c = _init_lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_witness__c();
lean_mark_persistent(lp_CyberAlchemy___private_CyberAlchemy_ProtorealMandelbrot_0__CyberAlchemy_ProtorealMandelbrot_witness__c);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
