// Lean compiler output
// Module: CyberAlchemy.ProtorealGraph
// Imports: public import Init public import Mathlib.Combinatorics.SimpleGraph.Basic public import Mathlib.Data.Fin.Basic public import CyberAlchemy.ProtorealManifold
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
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_idx__a;
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_idx__omega;
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_idx__iota;
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_idx__eps;
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_idx__lam;
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_component(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_component___boxed(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_CyberAlchemy_ProtorealGraph_klein__adj__bool(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_klein__adj__bool___boxed(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_CyberAlchemy_ProtorealGraph_klein__adj__decidable___aux__1(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_klein__adj__decidable___aux__1___boxed(lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_CyberAlchemy_ProtorealGraph_klein__adj__decidable(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_klein__adj__decidable___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_observation__graph;
LEAN_EXPORT uint8_t lp_CyberAlchemy_ProtorealGraph_instDecidableRelFinOfNatNatAdjObservation__graph(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_instDecidableRelFinOfNatNatAdjObservation__graph___boxed(lean_object*, lean_object*);
static lean_object* _init_lp_CyberAlchemy_ProtorealGraph_idx__a(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(0u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_ProtorealGraph_idx__omega(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(1u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_ProtorealGraph_idx__iota(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(2u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_ProtorealGraph_idx__eps(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(3u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_ProtorealGraph_idx__lam(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(4u);
return x_1;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_component(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; uint8_t x_4; 
x_3 = lean_unsigned_to_nat(0u);
x_4 = lean_nat_dec_eq(x_2, x_3);
if (x_4 == 1)
{
lean_object* x_5; 
x_5 = lean_ctor_get(x_1, 0);
lean_inc(x_5);
return x_5;
}
else
{
lean_object* x_6; lean_object* x_7; uint8_t x_8; 
x_6 = lean_unsigned_to_nat(1u);
x_7 = lean_nat_sub(x_2, x_6);
x_8 = lean_nat_dec_eq(x_7, x_3);
if (x_8 == 1)
{
lean_object* x_9; 
lean_dec(x_7);
x_9 = lean_ctor_get(x_1, 1);
lean_inc(x_9);
return x_9;
}
else
{
lean_object* x_10; uint8_t x_11; 
x_10 = lean_nat_sub(x_7, x_6);
lean_dec(x_7);
x_11 = lean_nat_dec_eq(x_10, x_3);
if (x_11 == 1)
{
lean_object* x_12; 
lean_dec(x_10);
x_12 = lean_ctor_get(x_1, 2);
lean_inc(x_12);
return x_12;
}
else
{
lean_object* x_13; uint8_t x_14; 
x_13 = lean_nat_sub(x_10, x_6);
lean_dec(x_10);
x_14 = lean_nat_dec_eq(x_13, x_3);
if (x_14 == 1)
{
lean_object* x_15; 
lean_dec(x_13);
x_15 = lean_ctor_get(x_1, 3);
lean_inc(x_15);
return x_15;
}
else
{
lean_object* x_16; uint8_t x_17; lean_object* x_18; 
x_16 = lean_nat_sub(x_13, x_6);
lean_dec(x_13);
x_17 = lean_nat_dec_eq(x_16, x_3);
lean_dec(x_16);
x_18 = lean_ctor_get(x_1, 4);
lean_inc(x_18);
return x_18;
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_component___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lp_CyberAlchemy_ProtorealGraph_component(x_1, x_2);
lean_dec(x_2);
lean_dec_ref(x_1);
return x_3;
}
}
LEAN_EXPORT uint8_t lp_CyberAlchemy_ProtorealGraph_klein__adj__bool(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; uint8_t x_4; 
x_3 = lean_unsigned_to_nat(0u);
x_4 = lean_nat_dec_eq(x_1, x_3);
if (x_4 == 0)
{
lean_object* x_5; uint8_t x_6; 
x_5 = lean_unsigned_to_nat(1u);
x_6 = lean_nat_dec_eq(x_1, x_5);
if (x_6 == 0)
{
lean_object* x_7; uint8_t x_8; 
x_7 = lean_unsigned_to_nat(2u);
x_8 = lean_nat_dec_eq(x_1, x_7);
if (x_8 == 0)
{
lean_object* x_9; uint8_t x_10; 
x_9 = lean_unsigned_to_nat(3u);
x_10 = lean_nat_dec_eq(x_1, x_9);
if (x_10 == 0)
{
lean_object* x_11; uint8_t x_12; 
x_11 = lean_unsigned_to_nat(4u);
x_12 = lean_nat_dec_eq(x_1, x_11);
if (x_12 == 0)
{
return x_12;
}
else
{
uint8_t x_13; 
x_13 = lean_nat_dec_eq(x_2, x_3);
if (x_13 == 0)
{
uint8_t x_14; 
x_14 = lean_nat_dec_eq(x_2, x_9);
return x_14;
}
else
{
return x_13;
}
}
}
else
{
uint8_t x_15; 
x_15 = lean_nat_dec_eq(x_2, x_3);
if (x_15 == 0)
{
lean_object* x_16; uint8_t x_17; 
x_16 = lean_unsigned_to_nat(4u);
x_17 = lean_nat_dec_eq(x_2, x_16);
return x_17;
}
else
{
return x_15;
}
}
}
else
{
uint8_t x_18; 
x_18 = lean_nat_dec_eq(x_2, x_3);
if (x_18 == 0)
{
uint8_t x_19; 
x_19 = lean_nat_dec_eq(x_2, x_5);
return x_19;
}
else
{
return x_18;
}
}
}
else
{
uint8_t x_20; 
x_20 = lean_nat_dec_eq(x_2, x_3);
if (x_20 == 0)
{
lean_object* x_21; uint8_t x_22; 
x_21 = lean_unsigned_to_nat(2u);
x_22 = lean_nat_dec_eq(x_2, x_21);
return x_22;
}
else
{
return x_20;
}
}
}
else
{
lean_object* x_23; uint8_t x_24; 
x_23 = lean_unsigned_to_nat(1u);
x_24 = lean_nat_dec_eq(x_2, x_23);
if (x_24 == 0)
{
lean_object* x_25; uint8_t x_26; 
x_25 = lean_unsigned_to_nat(2u);
x_26 = lean_nat_dec_eq(x_2, x_25);
if (x_26 == 0)
{
lean_object* x_27; uint8_t x_28; 
x_27 = lean_unsigned_to_nat(3u);
x_28 = lean_nat_dec_eq(x_2, x_27);
if (x_28 == 0)
{
lean_object* x_29; uint8_t x_30; 
x_29 = lean_unsigned_to_nat(4u);
x_30 = lean_nat_dec_eq(x_2, x_29);
return x_30;
}
else
{
return x_28;
}
}
else
{
return x_26;
}
}
else
{
return x_24;
}
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_klein__adj__bool___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
uint8_t x_3; lean_object* x_4; 
x_3 = lp_CyberAlchemy_ProtorealGraph_klein__adj__bool(x_1, x_2);
lean_dec(x_2);
lean_dec(x_1);
x_4 = lean_box(x_3);
return x_4;
}
}
LEAN_EXPORT uint8_t lp_CyberAlchemy_ProtorealGraph_klein__adj__decidable___aux__1(lean_object* x_1, lean_object* x_2) {
_start:
{
uint8_t x_3; 
x_3 = lp_CyberAlchemy_ProtorealGraph_klein__adj__bool(x_1, x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_klein__adj__decidable___aux__1___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
uint8_t x_3; lean_object* x_4; 
x_3 = lp_CyberAlchemy_ProtorealGraph_klein__adj__decidable___aux__1(x_1, x_2);
lean_dec(x_2);
lean_dec(x_1);
x_4 = lean_box(x_3);
return x_4;
}
}
LEAN_EXPORT uint8_t lp_CyberAlchemy_ProtorealGraph_klein__adj__decidable(lean_object* x_1, lean_object* x_2) {
_start:
{
uint8_t x_3; 
x_3 = lp_CyberAlchemy_ProtorealGraph_klein__adj__bool(x_1, x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_klein__adj__decidable___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
uint8_t x_3; lean_object* x_4; 
x_3 = lp_CyberAlchemy_ProtorealGraph_klein__adj__decidable(x_1, x_2);
lean_dec(x_2);
lean_dec(x_1);
x_4 = lean_box(x_3);
return x_4;
}
}
static lean_object* _init_lp_CyberAlchemy_ProtorealGraph_observation__graph(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_box(0);
return x_1;
}
}
LEAN_EXPORT uint8_t lp_CyberAlchemy_ProtorealGraph_instDecidableRelFinOfNatNatAdjObservation__graph(lean_object* x_1, lean_object* x_2) {
_start:
{
uint8_t x_3; 
x_3 = lp_CyberAlchemy_ProtorealGraph_klein__adj__bool(x_1, x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealGraph_instDecidableRelFinOfNatNatAdjObservation__graph___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
uint8_t x_3; lean_object* x_4; 
x_3 = lp_CyberAlchemy_ProtorealGraph_instDecidableRelFinOfNatNatAdjObservation__graph(x_1, x_2);
lean_dec(x_2);
lean_dec(x_1);
x_4 = lean_box(x_3);
return x_4;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Combinatorics_SimpleGraph_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Fin_Basic(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealGraph(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Combinatorics_SimpleGraph_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Fin_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_ProtorealGraph_idx__a = _init_lp_CyberAlchemy_ProtorealGraph_idx__a();
lean_mark_persistent(lp_CyberAlchemy_ProtorealGraph_idx__a);
lp_CyberAlchemy_ProtorealGraph_idx__omega = _init_lp_CyberAlchemy_ProtorealGraph_idx__omega();
lean_mark_persistent(lp_CyberAlchemy_ProtorealGraph_idx__omega);
lp_CyberAlchemy_ProtorealGraph_idx__iota = _init_lp_CyberAlchemy_ProtorealGraph_idx__iota();
lean_mark_persistent(lp_CyberAlchemy_ProtorealGraph_idx__iota);
lp_CyberAlchemy_ProtorealGraph_idx__eps = _init_lp_CyberAlchemy_ProtorealGraph_idx__eps();
lean_mark_persistent(lp_CyberAlchemy_ProtorealGraph_idx__eps);
lp_CyberAlchemy_ProtorealGraph_idx__lam = _init_lp_CyberAlchemy_ProtorealGraph_idx__lam();
lean_mark_persistent(lp_CyberAlchemy_ProtorealGraph_idx__lam);
lp_CyberAlchemy_ProtorealGraph_observation__graph = _init_lp_CyberAlchemy_ProtorealGraph_observation__graph();
lean_mark_persistent(lp_CyberAlchemy_ProtorealGraph_observation__graph);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
