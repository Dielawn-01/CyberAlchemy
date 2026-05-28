// Lean compiler output
// Module: CyberAlchemy.MayerVietoris
// Imports: public import Init public import CyberAlchemy.EulerPerception public import CyberAlchemy.AgenticFrame
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
LEAN_EXPORT lean_object* lp_CyberAlchemy_MayerVietoris_full__overlap(lean_object*);
lean_object* lean_nat_to_int(lean_object*);
static lean_once_cell_t lp_CyberAlchemy_MayerVietoris_disjoint__perspective___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_MayerVietoris_disjoint__perspective___closed__0;
lean_object* lean_int_add(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_MayerVietoris_disjoint__perspective(lean_object*, lean_object*);
extern lean_object* lp_CyberAlchemy_EulerPerception_euler__perception;
static lean_once_cell_t lp_CyberAlchemy_MayerVietoris_agentic__perspective___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_MayerVietoris_agentic__perspective___closed__0;
LEAN_EXPORT lean_object* lp_CyberAlchemy_MayerVietoris_agentic__perspective;
lean_object* lean_int_sub(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_MayerVietoris_compose__perspectives(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_MayerVietoris_compose__perspectives___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_MayerVietoris_full__overlap(lean_object* x_1) {
_start:
{
lean_object* x_2; 
lean_inc_n(x_1, 3);
x_2 = lean_alloc_ctor(0, 4, 0);
lean_ctor_set(x_2, 0, x_1);
lean_ctor_set(x_2, 1, x_1);
lean_ctor_set(x_2, 2, x_1);
lean_ctor_set(x_2, 3, x_1);
return x_2;
}
}
static lean_object* _init_lp_CyberAlchemy_MayerVietoris_disjoint__perspective___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; 
x_1 = lean_unsigned_to_nat(0u);
x_2 = lean_nat_to_int(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_MayerVietoris_disjoint__perspective(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; lean_object* x_4; lean_object* x_5; 
x_3 = lean_obj_once(&lp_CyberAlchemy_MayerVietoris_disjoint__perspective___closed__0, &lp_CyberAlchemy_MayerVietoris_disjoint__perspective___closed__0_once, _init_lp_CyberAlchemy_MayerVietoris_disjoint__perspective___closed__0);
x_4 = lean_int_add(x_1, x_2);
x_5 = lean_alloc_ctor(0, 4, 0);
lean_ctor_set(x_5, 0, x_1);
lean_ctor_set(x_5, 1, x_2);
lean_ctor_set(x_5, 2, x_3);
lean_ctor_set(x_5, 3, x_4);
return x_5;
}
}
static lean_object* _init_lp_CyberAlchemy_MayerVietoris_agentic__perspective___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; 
x_1 = lp_CyberAlchemy_EulerPerception_euler__perception;
x_2 = lean_alloc_ctor(0, 4, 0);
lean_ctor_set(x_2, 0, x_1);
lean_ctor_set(x_2, 1, x_1);
lean_ctor_set(x_2, 2, x_1);
lean_ctor_set(x_2, 3, x_1);
return x_2;
}
}
static lean_object* _init_lp_CyberAlchemy_MayerVietoris_agentic__perspective(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_obj_once(&lp_CyberAlchemy_MayerVietoris_agentic__perspective___closed__0, &lp_CyberAlchemy_MayerVietoris_agentic__perspective___closed__0_once, _init_lp_CyberAlchemy_MayerVietoris_agentic__perspective___closed__0);
return x_1;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_MayerVietoris_compose__perspectives(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
uint8_t x_4; 
x_4 = !lean_is_exclusive(x_2);
if (x_4 == 0)
{
lean_object* x_5; lean_object* x_6; lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; lean_object* x_11; 
x_5 = lean_ctor_get(x_1, 3);
x_6 = lean_ctor_get(x_2, 3);
x_7 = lean_ctor_get(x_2, 2);
lean_dec(x_7);
x_8 = lean_ctor_get(x_2, 1);
lean_dec(x_8);
x_9 = lean_ctor_get(x_2, 0);
lean_dec(x_9);
x_10 = lean_int_add(x_5, x_6);
x_11 = lean_int_sub(x_10, x_3);
lean_dec(x_10);
lean_inc(x_5);
lean_ctor_set(x_2, 3, x_11);
lean_ctor_set(x_2, 2, x_3);
lean_ctor_set(x_2, 1, x_6);
lean_ctor_set(x_2, 0, x_5);
return x_2;
}
else
{
lean_object* x_12; lean_object* x_13; lean_object* x_14; lean_object* x_15; lean_object* x_16; 
x_12 = lean_ctor_get(x_1, 3);
x_13 = lean_ctor_get(x_2, 3);
lean_inc(x_13);
lean_dec(x_2);
x_14 = lean_int_add(x_12, x_13);
x_15 = lean_int_sub(x_14, x_3);
lean_dec(x_14);
lean_inc(x_12);
x_16 = lean_alloc_ctor(0, 4, 0);
lean_ctor_set(x_16, 0, x_12);
lean_ctor_set(x_16, 1, x_13);
lean_ctor_set(x_16, 2, x_3);
lean_ctor_set(x_16, 3, x_15);
return x_16;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_MayerVietoris_compose__perspectives___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; 
x_4 = lp_CyberAlchemy_MayerVietoris_compose__perspectives(x_1, x_2, x_3);
lean_dec_ref(x_1);
return x_4;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_EulerPerception(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_AgenticFrame(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_MayerVietoris(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_EulerPerception(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_AgenticFrame(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_MayerVietoris_agentic__perspective = _init_lp_CyberAlchemy_MayerVietoris_agentic__perspective();
lean_mark_persistent(lp_CyberAlchemy_MayerVietoris_agentic__perspective);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
