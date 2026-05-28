// Lean compiler output
// Module: CyberAlchemy.AgenticRank
// Imports: public import Init public import Mathlib.Data.Real.Basic public import CyberAlchemy.ProtorealManifold public import CyberAlchemy.ComputationalCharge public import CyberAlchemy.EmotionalLFunctions public import CyberAlchemy.OrchOR
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
lean_object* lp_CyberAlchemy_ComputationalCharge_rho(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_AgenticRank_cognitive__execution(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_AgenticRank_cognitive__execution___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_AgenticRank_cognitive__execution(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lp_CyberAlchemy_ComputationalCharge_rho(x_1, x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_AgenticRank_cognitive__execution___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lp_CyberAlchemy_AgenticRank_cognitive__execution(x_1, x_2);
lean_dec(x_2);
return x_3;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Real_Basic(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ComputationalCharge(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_EmotionalLFunctions(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_OrchOR(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_AgenticRank(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Real_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ComputationalCharge(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_EmotionalLFunctions(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_OrchOR(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
