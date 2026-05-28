// Lean compiler output
// Module: CyberAlchemy.HodgeConjecture
// Imports: public import Init public import CyberAlchemy.HodgeDecomposition public import CyberAlchemy.KleinTopology public import CyberAlchemy.GlialDopant
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
lean_object* lp_CyberAlchemy_MonsterInverse_monster__inv(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HodgeConjecture_hodge__star(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HodgeConjecture_cycle__to__manifold(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HodgeConjecture_cycle__to__manifold___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HodgeConjecture_hodge__star(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_MonsterInverse_monster__inv(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HodgeConjecture_cycle__to__manifold(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; lean_object* x_4; lean_object* x_5; lean_object* x_6; 
x_2 = lean_ctor_get(x_1, 0);
x_3 = lean_ctor_get(x_1, 1);
x_4 = lean_ctor_get(x_1, 2);
x_5 = lean_ctor_get(x_1, 3);
lean_inc(x_5);
lean_inc(x_4);
lean_inc_n(x_3, 2);
lean_inc(x_2);
x_6 = lean_alloc_ctor(0, 5, 0);
lean_ctor_set(x_6, 0, x_2);
lean_ctor_set(x_6, 1, x_3);
lean_ctor_set(x_6, 2, x_3);
lean_ctor_set(x_6, 3, x_4);
lean_ctor_set(x_6, 4, x_5);
return x_6;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HodgeConjecture_cycle__to__manifold___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_HodgeConjecture_cycle__to__manifold(x_1);
lean_dec_ref(x_1);
return x_2;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_HodgeDecomposition(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_KleinTopology(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_GlialDopant(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_HodgeConjecture(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_HodgeDecomposition(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_KleinTopology(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_GlialDopant(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
