// Lean compiler output
// Module: CyberAlchemy.TopologicalFirewall
// Imports: public import Init public import CyberAlchemy.TensorImaginaryBridge public import CyberAlchemy.QuaternionInverse public import CyberAlchemy.CognitiveSecurity public import Mathlib.Data.Complex.Basic
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
lean_object* lp_CyberAlchemy_ZBuddyCybernetics_protoreal__collapse(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_TopologicalSecurity_sanitize__payload(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_TopologicalSecurity_sanitize__payload___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_TopologicalSecurity_sanitize__payload(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_ZBuddyCybernetics_protoreal__collapse(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_TopologicalSecurity_sanitize__payload___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_TopologicalSecurity_sanitize__payload(x_1);
lean_dec_ref(x_1);
return x_2;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_TensorImaginaryBridge(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_QuaternionInverse(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_CognitiveSecurity(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Complex_Basic(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_TopologicalFirewall(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_TensorImaginaryBridge(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_QuaternionInverse(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_CognitiveSecurity(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Complex_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
