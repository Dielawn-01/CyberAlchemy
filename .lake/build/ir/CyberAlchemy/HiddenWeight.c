// Lean compiler output
// Module: CyberAlchemy.HiddenWeight
// Imports: public import Init public import Mathlib.Tactic.NormNum public import Mathlib.Tactic.Linarith public import Mathlib.Data.Nat.Prime.Basic public import Mathlib.Data.Real.Basic public import CyberAlchemy.ProtorealManifold
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
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_parity__order;
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_entropy__order;
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_certainty__order;
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_ctorIdx(uint8_t);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_ctorIdx___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_toCtorIdx(uint8_t);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_toCtorIdx___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_ctorElim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_ctorElim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_ctorElim(lean_object*, lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_ctorElim___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_success_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_success_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_success_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_success_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_syntax__error_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_syntax__error_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_syntax__error_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_syntax__error_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_tactic__error_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_tactic__error_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_tactic__error_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_tactic__error_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_content__error_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_content__error_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_content__error_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_content__error_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
static const lean_string_object lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 29, .m_capacity = 29, .m_length = 28, .m_data = "HiddenWeight.Outcome.success"};
static const lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__0 = (const lean_object*)&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__0_value;
static const lean_ctor_object lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__0_value)}};
static const lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__1 = (const lean_object*)&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__1_value;
static const lean_string_object lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 34, .m_capacity = 34, .m_length = 33, .m_data = "HiddenWeight.Outcome.syntax_error"};
static const lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__2 = (const lean_object*)&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__2_value;
static const lean_ctor_object lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__2_value)}};
static const lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__3 = (const lean_object*)&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__3_value;
static const lean_string_object lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 34, .m_capacity = 34, .m_length = 33, .m_data = "HiddenWeight.Outcome.tactic_error"};
static const lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__4 = (const lean_object*)&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__4_value;
static const lean_ctor_object lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__4_value)}};
static const lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__5 = (const lean_object*)&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__5_value;
static const lean_string_object lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 35, .m_capacity = 35, .m_length = 34, .m_data = "HiddenWeight.Outcome.content_error"};
static const lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__6 = (const lean_object*)&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__6_value;
static const lean_ctor_object lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__6_value)}};
static const lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__7 = (const lean_object*)&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__7_value;
lean_object* lean_nat_to_int(lean_object*);
static lean_once_cell_t lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8;
static lean_once_cell_t lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9;
lean_object* l_Repr_addAppParen(lean_object*, lean_object*);
uint8_t lean_nat_dec_le(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr(uint8_t, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___boxed(lean_object*, lean_object*);
static const lean_closure_object lp_CyberAlchemy_HiddenWeight_instReprOutcome___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___boxed, .m_arity = 2, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome___closed__0 = (const lean_object*)&lp_CyberAlchemy_HiddenWeight_instReprOutcome___closed__0_value;
LEAN_EXPORT const lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome = (const lean_object*)&lp_CyberAlchemy_HiddenWeight_instReprOutcome___closed__0_value;
uint8_t lean_nat_dec_le(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_CyberAlchemy_HiddenWeight_Outcome_ofNat(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_ofNat___boxed(lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_CyberAlchemy_HiddenWeight_instDecidableEqOutcome(uint8_t, uint8_t);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_instDecidableEqOutcome___boxed(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_modulate(lean_object*, lean_object*);
static lean_object* _init_lp_CyberAlchemy_HiddenWeight_parity__order(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(2u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_HiddenWeight_entropy__order(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(5u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_HiddenWeight_certainty__order(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(23u);
return x_1;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_ctorIdx(uint8_t x_1) {
_start:
{
switch (x_1) {
case 0:
{
lean_object* x_2; 
x_2 = lean_unsigned_to_nat(0u);
return x_2;
}
case 1:
{
lean_object* x_3; 
x_3 = lean_unsigned_to_nat(1u);
return x_3;
}
case 2:
{
lean_object* x_4; 
x_4 = lean_unsigned_to_nat(2u);
return x_4;
}
default: 
{
lean_object* x_5; 
x_5 = lean_unsigned_to_nat(3u);
return x_5;
}
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_ctorIdx___boxed(lean_object* x_1) {
_start:
{
uint8_t x_2; lean_object* x_3; 
x_2 = lean_unbox(x_1);
x_3 = lp_CyberAlchemy_HiddenWeight_Outcome_ctorIdx(x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_toCtorIdx(uint8_t x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_HiddenWeight_Outcome_ctorIdx(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_toCtorIdx___boxed(lean_object* x_1) {
_start:
{
uint8_t x_2; lean_object* x_3; 
x_2 = lean_unbox(x_1);
x_3 = lp_CyberAlchemy_HiddenWeight_Outcome_toCtorIdx(x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_ctorElim___redArg(lean_object* x_1) {
_start:
{
lean_inc(x_1);
return x_1;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_ctorElim___redArg___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_HiddenWeight_Outcome_ctorElim___redArg(x_1);
lean_dec(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_ctorElim(lean_object* x_1, lean_object* x_2, uint8_t x_3, lean_object* x_4, lean_object* x_5) {
_start:
{
lean_inc(x_5);
return x_5;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_ctorElim___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4, lean_object* x_5) {
_start:
{
uint8_t x_6; lean_object* x_7; 
x_6 = lean_unbox(x_3);
x_7 = lp_CyberAlchemy_HiddenWeight_Outcome_ctorElim(x_1, x_2, x_6, x_4, x_5);
lean_dec(x_5);
lean_dec(x_2);
return x_7;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_success_elim___redArg(lean_object* x_1) {
_start:
{
lean_inc(x_1);
return x_1;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_success_elim___redArg___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_HiddenWeight_Outcome_success_elim___redArg(x_1);
lean_dec(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_success_elim(lean_object* x_1, uint8_t x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
lean_inc(x_4);
return x_4;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_success_elim___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
uint8_t x_5; lean_object* x_6; 
x_5 = lean_unbox(x_2);
x_6 = lp_CyberAlchemy_HiddenWeight_Outcome_success_elim(x_1, x_5, x_3, x_4);
lean_dec(x_4);
return x_6;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_syntax__error_elim___redArg(lean_object* x_1) {
_start:
{
lean_inc(x_1);
return x_1;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_syntax__error_elim___redArg___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_HiddenWeight_Outcome_syntax__error_elim___redArg(x_1);
lean_dec(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_syntax__error_elim(lean_object* x_1, uint8_t x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
lean_inc(x_4);
return x_4;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_syntax__error_elim___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
uint8_t x_5; lean_object* x_6; 
x_5 = lean_unbox(x_2);
x_6 = lp_CyberAlchemy_HiddenWeight_Outcome_syntax__error_elim(x_1, x_5, x_3, x_4);
lean_dec(x_4);
return x_6;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_tactic__error_elim___redArg(lean_object* x_1) {
_start:
{
lean_inc(x_1);
return x_1;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_tactic__error_elim___redArg___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_HiddenWeight_Outcome_tactic__error_elim___redArg(x_1);
lean_dec(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_tactic__error_elim(lean_object* x_1, uint8_t x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
lean_inc(x_4);
return x_4;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_tactic__error_elim___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
uint8_t x_5; lean_object* x_6; 
x_5 = lean_unbox(x_2);
x_6 = lp_CyberAlchemy_HiddenWeight_Outcome_tactic__error_elim(x_1, x_5, x_3, x_4);
lean_dec(x_4);
return x_6;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_content__error_elim___redArg(lean_object* x_1) {
_start:
{
lean_inc(x_1);
return x_1;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_content__error_elim___redArg___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_HiddenWeight_Outcome_content__error_elim___redArg(x_1);
lean_dec(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_content__error_elim(lean_object* x_1, uint8_t x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
lean_inc(x_4);
return x_4;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_content__error_elim___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
uint8_t x_5; lean_object* x_6; 
x_5 = lean_unbox(x_2);
x_6 = lp_CyberAlchemy_HiddenWeight_Outcome_content__error_elim(x_1, x_5, x_3, x_4);
lean_dec(x_4);
return x_6;
}
}
static lean_object* _init_lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8(void) {
_start:
{
lean_object* x_1; lean_object* x_2; 
x_1 = lean_unsigned_to_nat(2u);
x_2 = lean_nat_to_int(x_1);
return x_2;
}
}
static lean_object* _init_lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9(void) {
_start:
{
lean_object* x_1; lean_object* x_2; 
x_1 = lean_unsigned_to_nat(1u);
x_2 = lean_nat_to_int(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr(uint8_t x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; lean_object* x_10; lean_object* x_17; lean_object* x_24; 
switch (x_1) {
case 0:
{
lean_object* x_31; uint8_t x_32; 
x_31 = lean_unsigned_to_nat(1024u);
x_32 = lean_nat_dec_le(x_31, x_2);
if (x_32 == 0)
{
lean_object* x_33; 
x_33 = lean_obj_once(&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8, &lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8_once, _init_lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8);
x_3 = x_33;
goto block_9;
}
else
{
lean_object* x_34; 
x_34 = lean_obj_once(&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9, &lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9_once, _init_lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9);
x_3 = x_34;
goto block_9;
}
}
case 1:
{
lean_object* x_35; uint8_t x_36; 
x_35 = lean_unsigned_to_nat(1024u);
x_36 = lean_nat_dec_le(x_35, x_2);
if (x_36 == 0)
{
lean_object* x_37; 
x_37 = lean_obj_once(&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8, &lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8_once, _init_lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8);
x_10 = x_37;
goto block_16;
}
else
{
lean_object* x_38; 
x_38 = lean_obj_once(&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9, &lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9_once, _init_lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9);
x_10 = x_38;
goto block_16;
}
}
case 2:
{
lean_object* x_39; uint8_t x_40; 
x_39 = lean_unsigned_to_nat(1024u);
x_40 = lean_nat_dec_le(x_39, x_2);
if (x_40 == 0)
{
lean_object* x_41; 
x_41 = lean_obj_once(&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8, &lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8_once, _init_lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8);
x_17 = x_41;
goto block_23;
}
else
{
lean_object* x_42; 
x_42 = lean_obj_once(&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9, &lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9_once, _init_lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9);
x_17 = x_42;
goto block_23;
}
}
default: 
{
lean_object* x_43; uint8_t x_44; 
x_43 = lean_unsigned_to_nat(1024u);
x_44 = lean_nat_dec_le(x_43, x_2);
if (x_44 == 0)
{
lean_object* x_45; 
x_45 = lean_obj_once(&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8, &lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8_once, _init_lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__8);
x_24 = x_45;
goto block_30;
}
else
{
lean_object* x_46; 
x_46 = lean_obj_once(&lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9, &lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9_once, _init_lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__9);
x_24 = x_46;
goto block_30;
}
}
}
block_9:
{
lean_object* x_4; lean_object* x_5; uint8_t x_6; lean_object* x_7; lean_object* x_8; 
x_4 = ((lean_object*)(lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__1));
x_5 = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(x_5, 0, x_3);
lean_ctor_set(x_5, 1, x_4);
x_6 = 0;
x_7 = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(x_7, 0, x_5);
lean_ctor_set_uint8(x_7, sizeof(void*)*1, x_6);
x_8 = l_Repr_addAppParen(x_7, x_2);
return x_8;
}
block_16:
{
lean_object* x_11; lean_object* x_12; uint8_t x_13; lean_object* x_14; lean_object* x_15; 
x_11 = ((lean_object*)(lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__3));
x_12 = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(x_12, 0, x_10);
lean_ctor_set(x_12, 1, x_11);
x_13 = 0;
x_14 = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(x_14, 0, x_12);
lean_ctor_set_uint8(x_14, sizeof(void*)*1, x_13);
x_15 = l_Repr_addAppParen(x_14, x_2);
return x_15;
}
block_23:
{
lean_object* x_18; lean_object* x_19; uint8_t x_20; lean_object* x_21; lean_object* x_22; 
x_18 = ((lean_object*)(lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__5));
x_19 = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(x_19, 0, x_17);
lean_ctor_set(x_19, 1, x_18);
x_20 = 0;
x_21 = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(x_21, 0, x_19);
lean_ctor_set_uint8(x_21, sizeof(void*)*1, x_20);
x_22 = l_Repr_addAppParen(x_21, x_2);
return x_22;
}
block_30:
{
lean_object* x_25; lean_object* x_26; uint8_t x_27; lean_object* x_28; lean_object* x_29; 
x_25 = ((lean_object*)(lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___closed__7));
x_26 = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(x_26, 0, x_24);
lean_ctor_set(x_26, 1, x_25);
x_27 = 0;
x_28 = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(x_28, 0, x_26);
lean_ctor_set_uint8(x_28, sizeof(void*)*1, x_27);
x_29 = l_Repr_addAppParen(x_28, x_2);
return x_29;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
uint8_t x_3; lean_object* x_4; 
x_3 = lean_unbox(x_1);
x_4 = lp_CyberAlchemy_HiddenWeight_instReprOutcome_repr(x_3, x_2);
lean_dec(x_2);
return x_4;
}
}
LEAN_EXPORT uint8_t lp_CyberAlchemy_HiddenWeight_Outcome_ofNat(lean_object* x_1) {
_start:
{
lean_object* x_2; uint8_t x_3; 
x_2 = lean_unsigned_to_nat(1u);
x_3 = lean_nat_dec_le(x_1, x_2);
if (x_3 == 0)
{
lean_object* x_4; uint8_t x_5; 
x_4 = lean_unsigned_to_nat(2u);
x_5 = lean_nat_dec_le(x_1, x_4);
if (x_5 == 0)
{
uint8_t x_6; 
x_6 = 3;
return x_6;
}
else
{
uint8_t x_7; 
x_7 = 2;
return x_7;
}
}
else
{
lean_object* x_8; uint8_t x_9; 
x_8 = lean_unsigned_to_nat(0u);
x_9 = lean_nat_dec_le(x_1, x_8);
if (x_9 == 0)
{
uint8_t x_10; 
x_10 = 1;
return x_10;
}
else
{
uint8_t x_11; 
x_11 = 0;
return x_11;
}
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_Outcome_ofNat___boxed(lean_object* x_1) {
_start:
{
uint8_t x_2; lean_object* x_3; 
x_2 = lp_CyberAlchemy_HiddenWeight_Outcome_ofNat(x_1);
lean_dec(x_1);
x_3 = lean_box(x_2);
return x_3;
}
}
LEAN_EXPORT uint8_t lp_CyberAlchemy_HiddenWeight_instDecidableEqOutcome(uint8_t x_1, uint8_t x_2) {
_start:
{
lean_object* x_3; lean_object* x_4; uint8_t x_5; 
x_3 = lp_CyberAlchemy_HiddenWeight_Outcome_ctorIdx(x_1);
x_4 = lp_CyberAlchemy_HiddenWeight_Outcome_ctorIdx(x_2);
x_5 = lean_nat_dec_eq(x_3, x_4);
lean_dec(x_4);
lean_dec(x_3);
return x_5;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_instDecidableEqOutcome___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
uint8_t x_3; uint8_t x_4; uint8_t x_5; lean_object* x_6; 
x_3 = lean_unbox(x_1);
x_4 = lean_unbox(x_2);
x_5 = lp_CyberAlchemy_HiddenWeight_instDecidableEqOutcome(x_3, x_4);
x_6 = lean_box(x_5);
return x_6;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HiddenWeight_modulate(lean_object* x_1, lean_object* x_2) {
_start:
{
uint8_t x_3; 
x_3 = !lean_is_exclusive(x_1);
if (x_3 == 0)
{
lean_object* x_4; lean_object* x_5; lean_object* x_6; lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; lean_object* x_11; lean_object* x_12; 
x_4 = lean_ctor_get(x_1, 3);
x_5 = lean_ctor_get(x_1, 4);
x_6 = lean_ctor_get(x_2, 1);
lean_inc(x_6);
x_7 = lean_ctor_get(x_2, 2);
lean_inc(x_7);
lean_dec_ref(x_2);
x_8 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_8, 0, x_6);
x_9 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_9, 0, x_4);
lean_closure_set(x_9, 1, x_8);
lean_inc(x_7);
x_10 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_10, 0, x_7);
x_11 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_11, 0, x_9);
lean_closure_set(x_11, 1, x_10);
x_12 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_12, 0, x_5);
lean_closure_set(x_12, 1, x_7);
lean_ctor_set(x_1, 4, x_12);
lean_ctor_set(x_1, 3, x_11);
return x_1;
}
else
{
lean_object* x_13; lean_object* x_14; lean_object* x_15; lean_object* x_16; lean_object* x_17; lean_object* x_18; lean_object* x_19; lean_object* x_20; lean_object* x_21; lean_object* x_22; lean_object* x_23; lean_object* x_24; lean_object* x_25; 
x_13 = lean_ctor_get(x_1, 0);
x_14 = lean_ctor_get(x_1, 1);
x_15 = lean_ctor_get(x_1, 2);
x_16 = lean_ctor_get(x_1, 3);
x_17 = lean_ctor_get(x_1, 4);
lean_inc(x_17);
lean_inc(x_16);
lean_inc(x_15);
lean_inc(x_14);
lean_inc(x_13);
lean_dec(x_1);
x_18 = lean_ctor_get(x_2, 1);
lean_inc(x_18);
x_19 = lean_ctor_get(x_2, 2);
lean_inc(x_19);
lean_dec_ref(x_2);
x_20 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_20, 0, x_18);
x_21 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_21, 0, x_16);
lean_closure_set(x_21, 1, x_20);
lean_inc(x_19);
x_22 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_22, 0, x_19);
x_23 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_23, 0, x_21);
lean_closure_set(x_23, 1, x_22);
x_24 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_24, 0, x_17);
lean_closure_set(x_24, 1, x_19);
x_25 = lean_alloc_ctor(0, 5, 0);
lean_ctor_set(x_25, 0, x_13);
lean_ctor_set(x_25, 1, x_14);
lean_ctor_set(x_25, 2, x_15);
lean_ctor_set(x_25, 3, x_23);
lean_ctor_set(x_25, 4, x_24);
return x_25;
}
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_NormNum(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_Linarith(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Nat_Prime_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Real_Basic(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_HiddenWeight(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Tactic_NormNum(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Tactic_Linarith(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Nat_Prime_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Real_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_HiddenWeight_parity__order = _init_lp_CyberAlchemy_HiddenWeight_parity__order();
lean_mark_persistent(lp_CyberAlchemy_HiddenWeight_parity__order);
lp_CyberAlchemy_HiddenWeight_entropy__order = _init_lp_CyberAlchemy_HiddenWeight_entropy__order();
lean_mark_persistent(lp_CyberAlchemy_HiddenWeight_entropy__order);
lp_CyberAlchemy_HiddenWeight_certainty__order = _init_lp_CyberAlchemy_HiddenWeight_certainty__order();
lean_mark_persistent(lp_CyberAlchemy_HiddenWeight_certainty__order);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
