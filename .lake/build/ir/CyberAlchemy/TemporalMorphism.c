// Lean compiler output
// Module: CyberAlchemy.TemporalMorphism
// Imports: public import Init public import CyberAlchemy.Uncomplex
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
extern lean_object* lp_CyberAlchemy_ProtorealManifold_omega;
lean_object* lp_CyberAlchemy_ProtorealManifold_mul(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_time__step(lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_time__evolution(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_time__evolution___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_time__step(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; 
x_2 = lp_CyberAlchemy_ProtorealManifold_omega;
x_3 = lp_CyberAlchemy_ProtorealManifold_mul(x_1, x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_time__evolution(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; uint8_t x_4; 
x_3 = lean_unsigned_to_nat(0u);
x_4 = lean_nat_dec_eq(x_1, x_3);
if (x_4 == 1)
{
lean_inc_ref(x_2);
return x_2;
}
else
{
lean_object* x_5; lean_object* x_6; lean_object* x_7; lean_object* x_8; 
x_5 = lean_unsigned_to_nat(1u);
x_6 = lean_nat_sub(x_1, x_5);
x_7 = lp_CyberAlchemy_CyberAlchemy_time__evolution(x_6, x_2);
lean_dec(x_6);
x_8 = lp_CyberAlchemy_CyberAlchemy_time__step(x_7);
return x_8;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_time__evolution___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lp_CyberAlchemy_CyberAlchemy_time__evolution(x_1, x_2);
lean_dec_ref(x_2);
lean_dec(x_1);
return x_3;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_Uncomplex(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_TemporalMorphism(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_Uncomplex(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
