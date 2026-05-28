// Lean compiler output
// Module: CyberAlchemy.Deriv
// Imports: public import Init public import CyberAlchemy.ProtorealManifold
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
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealManifold_mesh__deriv(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealManifold_mesh__deriv___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealManifold_noise__drift(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealManifold_noise__drift___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealManifold_mesh__deriv(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lean_ctor_get(x_1, 2);
lean_inc(x_2);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealManifold_mesh__deriv___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_ProtorealManifold_mesh__deriv(x_1);
lean_dec_ref(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealManifold_noise__drift(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lean_ctor_get(x_1, 3);
lean_inc(x_2);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealManifold_noise__drift___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_ProtorealManifold_noise__drift(x_1);
lean_dec_ref(x_1);
return x_2;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_Deriv(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
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
