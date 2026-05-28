// Lean compiler output
// Module: CyberAlchemy.GlialDopant
// Imports: public import Init public import CyberAlchemy.ProtorealOperator public import CyberAlchemy.EulerPerception public import CyberAlchemy.CommutatorGap public import CyberAlchemy.AgenticFrame
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
lean_object* lp_CyberAlchemy_consolidate(lean_object*);
lean_object* lp_CyberAlchemy_funct(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_dopant__cycle(lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_dopant__iterate(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_dopant__iterate_match__1_splitter___redArg(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_dopant__iterate_match__1_splitter___redArg___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_dopant__iterate_match__1_splitter(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_dopant__iterate_match__1_splitter___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* lean_nat_add(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_fib(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_fib___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_fib_match__1_splitter___redArg(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_fib_match__1_splitter___redArg___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_fib_match__1_splitter(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_fib_match__1_splitter___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_CyberAlchemy_GlialDopant_is__dopant__step___lam__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_is__dopant__step___lam__0___boxed(lean_object*, lean_object*);
lean_object* l_List_range(lean_object*);
uint8_t l_List_any___redArg(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_CyberAlchemy_GlialDopant_is__dopant__step(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_is__dopant__step___boxed(lean_object*);
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
extern lean_object* lp_CyberAlchemy_AgenticFrame_agent__origin;
static lean_once_cell_t lp_CyberAlchemy_GlialDopant_GlialAgent_origin___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_GlialDopant_GlialAgent_origin___closed__0;
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_GlialAgent_origin;
lean_object* lp_mathlib_Complex_ofReal(lean_object*);
static lean_once_cell_t lp_CyberAlchemy_GlialDopant_GlialAgent_glial__step___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_GlialDopant_GlialAgent_glial__step___closed__0;
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_GlialAgent_glial__step(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_dopant__cycle(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; 
x_2 = lp_CyberAlchemy_consolidate(x_1);
x_3 = lp_CyberAlchemy_funct(x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_dopant__iterate(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; uint8_t x_4; 
x_3 = lean_unsigned_to_nat(0u);
x_4 = lean_nat_dec_eq(x_2, x_3);
if (x_4 == 1)
{
lean_dec(x_2);
return x_1;
}
else
{
lean_object* x_5; lean_object* x_6; lean_object* x_7; 
x_5 = lean_unsigned_to_nat(1u);
x_6 = lean_nat_sub(x_2, x_5);
lean_dec(x_2);
x_7 = lp_CyberAlchemy_GlialDopant_dopant__cycle(x_1);
x_1 = x_7;
x_2 = x_6;
goto _start;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_dopant__iterate_match__1_splitter___redArg(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
lean_object* x_5; uint8_t x_6; 
x_5 = lean_unsigned_to_nat(0u);
x_6 = lean_nat_dec_eq(x_2, x_5);
if (x_6 == 1)
{
lean_object* x_7; 
lean_dec(x_4);
x_7 = lean_apply_1(x_3, x_1);
return x_7;
}
else
{
lean_object* x_8; lean_object* x_9; lean_object* x_10; 
lean_dec(x_3);
x_8 = lean_unsigned_to_nat(1u);
x_9 = lean_nat_sub(x_2, x_8);
x_10 = lean_apply_2(x_4, x_1, x_9);
return x_10;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_dopant__iterate_match__1_splitter___redArg___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
lean_object* x_5; 
x_5 = lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_dopant__iterate_match__1_splitter___redArg(x_1, x_2, x_3, x_4);
lean_dec(x_2);
return x_5;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_dopant__iterate_match__1_splitter(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4, lean_object* x_5) {
_start:
{
lean_object* x_6; uint8_t x_7; 
x_6 = lean_unsigned_to_nat(0u);
x_7 = lean_nat_dec_eq(x_3, x_6);
if (x_7 == 1)
{
lean_object* x_8; 
lean_dec(x_5);
x_8 = lean_apply_1(x_4, x_2);
return x_8;
}
else
{
lean_object* x_9; lean_object* x_10; lean_object* x_11; 
lean_dec(x_4);
x_9 = lean_unsigned_to_nat(1u);
x_10 = lean_nat_sub(x_3, x_9);
x_11 = lean_apply_2(x_5, x_2, x_10);
return x_11;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_dopant__iterate_match__1_splitter___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4, lean_object* x_5) {
_start:
{
lean_object* x_6; 
x_6 = lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_dopant__iterate_match__1_splitter(x_1, x_2, x_3, x_4, x_5);
lean_dec(x_3);
return x_6;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_fib(lean_object* x_1) {
_start:
{
lean_object* x_2; uint8_t x_3; 
x_2 = lean_unsigned_to_nat(0u);
x_3 = lean_nat_dec_eq(x_1, x_2);
if (x_3 == 1)
{
lean_object* x_4; 
x_4 = lean_unsigned_to_nat(1u);
return x_4;
}
else
{
lean_object* x_5; lean_object* x_6; uint8_t x_7; 
x_5 = lean_unsigned_to_nat(1u);
x_6 = lean_nat_sub(x_1, x_5);
x_7 = lean_nat_dec_eq(x_6, x_2);
if (x_7 == 1)
{
lean_dec(x_6);
return x_5;
}
else
{
lean_object* x_8; lean_object* x_9; lean_object* x_10; lean_object* x_11; lean_object* x_12; 
x_8 = lean_nat_sub(x_6, x_5);
lean_dec(x_6);
x_9 = lean_nat_add(x_8, x_5);
x_10 = lp_CyberAlchemy_GlialDopant_fib(x_9);
lean_dec(x_9);
x_11 = lp_CyberAlchemy_GlialDopant_fib(x_8);
lean_dec(x_8);
x_12 = lean_nat_add(x_10, x_11);
lean_dec(x_11);
lean_dec(x_10);
return x_12;
}
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_fib___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_GlialDopant_fib(x_1);
lean_dec(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_fib_match__1_splitter___redArg(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
lean_object* x_5; uint8_t x_6; 
x_5 = lean_unsigned_to_nat(0u);
x_6 = lean_nat_dec_eq(x_1, x_5);
if (x_6 == 1)
{
lean_object* x_7; lean_object* x_8; 
lean_dec(x_4);
lean_dec(x_3);
x_7 = lean_box(0);
x_8 = lean_apply_1(x_2, x_7);
return x_8;
}
else
{
lean_object* x_9; lean_object* x_10; uint8_t x_11; 
lean_dec(x_2);
x_9 = lean_unsigned_to_nat(1u);
x_10 = lean_nat_sub(x_1, x_9);
x_11 = lean_nat_dec_eq(x_10, x_5);
if (x_11 == 1)
{
lean_object* x_12; lean_object* x_13; 
lean_dec(x_10);
lean_dec(x_4);
x_12 = lean_box(0);
x_13 = lean_apply_1(x_3, x_12);
return x_13;
}
else
{
lean_object* x_14; lean_object* x_15; 
lean_dec(x_3);
x_14 = lean_nat_sub(x_10, x_9);
lean_dec(x_10);
x_15 = lean_apply_1(x_4, x_14);
return x_15;
}
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_fib_match__1_splitter___redArg___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
lean_object* x_5; 
x_5 = lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_fib_match__1_splitter___redArg(x_1, x_2, x_3, x_4);
lean_dec(x_1);
return x_5;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_fib_match__1_splitter(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4, lean_object* x_5) {
_start:
{
lean_object* x_6; uint8_t x_7; 
x_6 = lean_unsigned_to_nat(0u);
x_7 = lean_nat_dec_eq(x_2, x_6);
if (x_7 == 1)
{
lean_object* x_8; lean_object* x_9; 
lean_dec(x_5);
lean_dec(x_4);
x_8 = lean_box(0);
x_9 = lean_apply_1(x_3, x_8);
return x_9;
}
else
{
lean_object* x_10; lean_object* x_11; uint8_t x_12; 
lean_dec(x_3);
x_10 = lean_unsigned_to_nat(1u);
x_11 = lean_nat_sub(x_2, x_10);
x_12 = lean_nat_dec_eq(x_11, x_6);
if (x_12 == 1)
{
lean_object* x_13; lean_object* x_14; 
lean_dec(x_11);
lean_dec(x_5);
x_13 = lean_box(0);
x_14 = lean_apply_1(x_4, x_13);
return x_14;
}
else
{
lean_object* x_15; lean_object* x_16; 
lean_dec(x_4);
x_15 = lean_nat_sub(x_11, x_10);
lean_dec(x_11);
x_16 = lean_apply_1(x_5, x_15);
return x_16;
}
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_fib_match__1_splitter___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4, lean_object* x_5) {
_start:
{
lean_object* x_6; 
x_6 = lp_CyberAlchemy___private_CyberAlchemy_GlialDopant_0__GlialDopant_fib_match__1_splitter(x_1, x_2, x_3, x_4, x_5);
lean_dec(x_2);
return x_6;
}
}
LEAN_EXPORT uint8_t lp_CyberAlchemy_GlialDopant_is__dopant__step___lam__0(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; uint8_t x_4; 
x_3 = lp_CyberAlchemy_GlialDopant_fib(x_2);
x_4 = lean_nat_dec_eq(x_3, x_1);
lean_dec(x_3);
return x_4;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_is__dopant__step___lam__0___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
uint8_t x_3; lean_object* x_4; 
x_3 = lp_CyberAlchemy_GlialDopant_is__dopant__step___lam__0(x_1, x_2);
lean_dec(x_2);
lean_dec(x_1);
x_4 = lean_box(x_3);
return x_4;
}
}
LEAN_EXPORT uint8_t lp_CyberAlchemy_GlialDopant_is__dopant__step(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; lean_object* x_4; lean_object* x_5; uint8_t x_6; 
lean_inc(x_1);
x_2 = lean_alloc_closure((void*)(lp_CyberAlchemy_GlialDopant_is__dopant__step___lam__0___boxed), 2, 1);
lean_closure_set(x_2, 0, x_1);
x_3 = lean_unsigned_to_nat(2u);
x_4 = lean_nat_add(x_1, x_3);
lean_dec(x_1);
x_5 = l_List_range(x_4);
x_6 = l_List_any___redArg(x_5, x_2);
return x_6;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_is__dopant__step___boxed(lean_object* x_1) {
_start:
{
uint8_t x_2; lean_object* x_3; 
x_2 = lp_CyberAlchemy_GlialDopant_is__dopant__step(x_1);
x_3 = lean_box(x_2);
return x_3;
}
}
static lean_object* _init_lp_CyberAlchemy_GlialDopant_GlialAgent_origin___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; lean_object* x_4; 
x_1 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
x_2 = lean_unsigned_to_nat(0u);
x_3 = lp_CyberAlchemy_AgenticFrame_agent__origin;
x_4 = lean_alloc_ctor(0, 3, 0);
lean_ctor_set(x_4, 0, x_3);
lean_ctor_set(x_4, 1, x_2);
lean_ctor_set(x_4, 2, x_1);
return x_4;
}
}
static lean_object* _init_lp_CyberAlchemy_GlialDopant_GlialAgent_origin(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_obj_once(&lp_CyberAlchemy_GlialDopant_GlialAgent_origin___closed__0, &lp_CyberAlchemy_GlialDopant_GlialAgent_origin___closed__0_once, _init_lp_CyberAlchemy_GlialDopant_GlialAgent_origin___closed__0);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_GlialDopant_GlialAgent_glial__step___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; 
x_1 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
x_2 = lp_mathlib_Complex_ofReal(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_GlialDopant_GlialAgent_glial__step(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; lean_object* x_4; lean_object* x_5; lean_object* x_6; lean_object* x_7; lean_object* x_8; uint8_t x_24; lean_object* x_25; 
x_3 = lean_ctor_get(x_1, 0);
lean_inc_ref(x_3);
x_4 = lean_ctor_get(x_1, 1);
lean_inc(x_4);
x_5 = lean_ctor_get(x_1, 2);
lean_inc(x_5);
if (lean_is_exclusive(x_1)) {
 lean_ctor_release(x_1, 0);
 lean_ctor_release(x_1, 1);
 lean_ctor_release(x_1, 2);
 x_6 = x_1;
} else {
 lean_dec_ref(x_1);
 x_6 = lean_box(0);
}
lean_inc(x_4);
x_24 = lp_CyberAlchemy_GlialDopant_is__dopant__step(x_4);
if (x_24 == 0)
{
lean_object* x_29; 
lean_inc_ref(x_2);
x_29 = lp_CyberAlchemy_funct(x_2);
x_25 = x_29;
goto block_28;
}
else
{
lean_object* x_30; 
lean_inc_ref(x_2);
x_30 = lp_CyberAlchemy_consolidate(x_2);
x_25 = x_30;
goto block_28;
}
block_23:
{
uint8_t x_9; 
x_9 = !lean_is_exclusive(x_3);
if (x_9 == 0)
{
lean_object* x_10; lean_object* x_11; lean_object* x_12; lean_object* x_13; lean_object* x_14; lean_object* x_15; 
x_10 = lean_ctor_get(x_3, 0);
lean_dec(x_10);
x_11 = lean_obj_once(&lp_CyberAlchemy_GlialDopant_GlialAgent_glial__step___closed__0, &lp_CyberAlchemy_GlialDopant_GlialAgent_glial__step___closed__0_once, _init_lp_CyberAlchemy_GlialDopant_GlialAgent_glial__step___closed__0);
x_12 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_12, 0, x_7);
lean_ctor_set(x_12, 1, x_11);
lean_ctor_set(x_3, 0, x_12);
x_13 = lean_unsigned_to_nat(1u);
x_14 = lean_nat_add(x_4, x_13);
lean_dec(x_4);
if (lean_is_scalar(x_6)) {
 x_15 = lean_alloc_ctor(0, 3, 0);
} else {
 x_15 = x_6;
}
lean_ctor_set(x_15, 0, x_3);
lean_ctor_set(x_15, 1, x_14);
lean_ctor_set(x_15, 2, x_8);
return x_15;
}
else
{
lean_object* x_16; lean_object* x_17; lean_object* x_18; lean_object* x_19; lean_object* x_20; lean_object* x_21; lean_object* x_22; 
x_16 = lean_ctor_get(x_3, 1);
lean_inc(x_16);
lean_dec(x_3);
x_17 = lean_obj_once(&lp_CyberAlchemy_GlialDopant_GlialAgent_glial__step___closed__0, &lp_CyberAlchemy_GlialDopant_GlialAgent_glial__step___closed__0_once, _init_lp_CyberAlchemy_GlialDopant_GlialAgent_glial__step___closed__0);
x_18 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_18, 0, x_7);
lean_ctor_set(x_18, 1, x_17);
x_19 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_19, 0, x_18);
lean_ctor_set(x_19, 1, x_16);
x_20 = lean_unsigned_to_nat(1u);
x_21 = lean_nat_add(x_4, x_20);
lean_dec(x_4);
if (lean_is_scalar(x_6)) {
 x_22 = lean_alloc_ctor(0, 3, 0);
} else {
 x_22 = x_6;
}
lean_ctor_set(x_22, 0, x_19);
lean_ctor_set(x_22, 1, x_21);
lean_ctor_set(x_22, 2, x_8);
return x_22;
}
}
block_28:
{
if (x_24 == 0)
{
lean_object* x_26; lean_object* x_27; 
x_26 = lean_ctor_get(x_2, 3);
lean_inc(x_26);
lean_dec_ref(x_2);
x_27 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_27, 0, x_5);
lean_closure_set(x_27, 1, x_26);
x_7 = x_25;
x_8 = x_27;
goto block_23;
}
else
{
lean_dec_ref(x_2);
x_7 = x_25;
x_8 = x_5;
goto block_23;
}
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealOperator(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_EulerPerception(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_CommutatorGap(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_AgenticFrame(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_GlialDopant(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealOperator(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_EulerPerception(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_CommutatorGap(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_AgenticFrame(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_GlialDopant_GlialAgent_origin = _init_lp_CyberAlchemy_GlialDopant_GlialAgent_origin();
lean_mark_persistent(lp_CyberAlchemy_GlialDopant_GlialAgent_origin);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
