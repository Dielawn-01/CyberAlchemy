// Lean compiler output
// Module: CyberAlchemy.FrenetSerretCybernetics
// Imports: public import Init public import CyberAlchemy.HolographicCollapse public import CyberAlchemy.ProtorealOperator public import CyberAlchemy.TensorImaginaryBridge
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
lean_object* lp_CyberAlchemy_HolographicCollapse_collapse__state(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_FrenetSerretCybernetics_osculating__plane(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_FrenetSerretCybernetics_osculating__plane___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_FrenetSerretCybernetics_binormal__vector(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_FrenetSerretCybernetics_binormal__vector___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_FrenetSerretCybernetics_osculating__plane(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_HolographicCollapse_collapse__state(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_FrenetSerretCybernetics_osculating__plane___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_FrenetSerretCybernetics_osculating__plane(x_1);
lean_dec_ref(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_FrenetSerretCybernetics_binormal__vector(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; lean_object* x_4; 
x_2 = lean_ctor_get(x_1, 3);
x_3 = lean_ctor_get(x_1, 4);
lean_inc(x_3);
lean_inc(x_2);
x_4 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_4, 0, x_2);
lean_ctor_set(x_4, 1, x_3);
return x_4;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_FrenetSerretCybernetics_binormal__vector___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_FrenetSerretCybernetics_binormal__vector(x_1);
lean_dec_ref(x_1);
return x_2;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_HolographicCollapse(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealOperator(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_TensorImaginaryBridge(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_FrenetSerretCybernetics(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_HolographicCollapse(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealOperator(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_TensorImaginaryBridge(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
