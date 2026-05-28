// Lean compiler output
// Module: CyberAlchemy.NilradicalGeneralization
// Imports: public import Init public import Mathlib.Tactic public import Mathlib.RingTheory.Nilpotent.Defs public import CyberAlchemy.ProtorealManifold
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
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero___lam__0(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero___lam__0___boxed(lean_object*);
static const lean_closure_object lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero___lam__0___boxed, .m_arity = 1, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero___closed__0 = (const lean_object*)&lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero___closed__0_value;
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero___boxed(lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
uint8_t lean_nat_dec_lt(lean_object*, lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_epsilon__shift___lam__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_epsilon__shift___lam__0___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_epsilon__shift(lean_object*, lean_object*);
lean_object* lean_nat_add(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_lambda__shift___lam__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_lambda__shift___lam__0___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_lambda__shift(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_derivative__depth(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_derivative__depth___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero___lam__0(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero___lam__0___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero___lam__0(x_1);
lean_dec(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = ((lean_object*)(lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero___closed__0));
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_NilradicalGeneralization_JetElement_instZero(x_1);
lean_dec(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_epsilon__shift___lam__0(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; uint8_t x_5; 
x_4 = lean_unsigned_to_nat(0u);
x_5 = lean_nat_dec_eq(x_3, x_4);
if (x_5 == 0)
{
uint8_t x_6; 
x_6 = lean_nat_dec_lt(x_3, x_1);
if (x_6 == 0)
{
lean_object* x_7; 
lean_dec(x_2);
x_7 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
return x_7;
}
else
{
lean_object* x_8; lean_object* x_9; lean_object* x_10; 
x_8 = lean_unsigned_to_nat(1u);
x_9 = lean_nat_sub(x_3, x_8);
x_10 = lean_apply_1(x_2, x_9);
return x_10;
}
}
else
{
lean_object* x_11; 
lean_dec(x_2);
x_11 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
return x_11;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_epsilon__shift___lam__0___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; 
x_4 = lp_CyberAlchemy_NilradicalGeneralization_epsilon__shift___lam__0(x_1, x_2, x_3);
lean_dec(x_3);
lean_dec(x_1);
return x_4;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_epsilon__shift(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lean_alloc_closure((void*)(lp_CyberAlchemy_NilradicalGeneralization_epsilon__shift___lam__0___boxed), 3, 2);
lean_closure_set(x_3, 0, x_1);
lean_closure_set(x_3, 1, x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_lambda__shift___lam__0(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; lean_object* x_5; uint8_t x_6; 
x_4 = lean_unsigned_to_nat(1u);
x_5 = lean_nat_add(x_3, x_4);
x_6 = lean_nat_dec_lt(x_5, x_1);
if (x_6 == 0)
{
lean_object* x_7; 
lean_dec(x_5);
lean_dec(x_2);
x_7 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
return x_7;
}
else
{
lean_object* x_8; 
x_8 = lean_apply_1(x_2, x_5);
return x_8;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_lambda__shift___lam__0___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; 
x_4 = lp_CyberAlchemy_NilradicalGeneralization_lambda__shift___lam__0(x_1, x_2, x_3);
lean_dec(x_3);
lean_dec(x_1);
return x_4;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_lambda__shift(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lean_alloc_closure((void*)(lp_CyberAlchemy_NilradicalGeneralization_lambda__shift___lam__0___boxed), 3, 2);
lean_closure_set(x_3, 0, x_1);
lean_closure_set(x_3, 1, x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_derivative__depth(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; 
x_2 = lean_unsigned_to_nat(1u);
x_3 = lean_nat_sub(x_1, x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_NilradicalGeneralization_derivative__depth___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_NilradicalGeneralization_derivative__depth(x_1);
lean_dec(x_1);
return x_2;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_RingTheory_Nilpotent_Defs(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_NilradicalGeneralization(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Tactic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_RingTheory_Nilpotent_Defs(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
