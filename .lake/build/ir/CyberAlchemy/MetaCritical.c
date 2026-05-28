// Lean compiler output
// Module: CyberAlchemy.MetaCritical
// Imports: public import Init public import Mathlib.Tactic.NormNum public import CyberAlchemy.ProtorealManifold
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
LEAN_EXPORT lean_object* lp_CyberAlchemy_MetaCritical_p;
LEAN_EXPORT lean_object* lp_CyberAlchemy_MetaCritical_phi;
LEAN_EXPORT lean_object* lp_CyberAlchemy_MetaCritical_phi__bar;
LEAN_EXPORT lean_object* lp_CyberAlchemy_MetaCritical_sigma;
static lean_object* _init_lp_CyberAlchemy_MetaCritical_p(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(139u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_MetaCritical_phi(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(64u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_MetaCritical_phi__bar(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(76u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_MetaCritical_sigma(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(28u);
return x_1;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_NormNum(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_MetaCritical(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Tactic_NormNum(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_MetaCritical_p = _init_lp_CyberAlchemy_MetaCritical_p();
lean_mark_persistent(lp_CyberAlchemy_MetaCritical_p);
lp_CyberAlchemy_MetaCritical_phi = _init_lp_CyberAlchemy_MetaCritical_phi();
lean_mark_persistent(lp_CyberAlchemy_MetaCritical_phi);
lp_CyberAlchemy_MetaCritical_phi__bar = _init_lp_CyberAlchemy_MetaCritical_phi__bar();
lean_mark_persistent(lp_CyberAlchemy_MetaCritical_phi__bar);
lp_CyberAlchemy_MetaCritical_sigma = _init_lp_CyberAlchemy_MetaCritical_sigma();
lean_mark_persistent(lp_CyberAlchemy_MetaCritical_sigma);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
