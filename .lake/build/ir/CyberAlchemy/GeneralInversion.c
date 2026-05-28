// Lean compiler output
// Module: CyberAlchemy.GeneralInversion
// Imports: public import Init public import CyberAlchemy.ProtorealManifold public import CyberAlchemy.MonsterInverse public import CyberAlchemy.DualityTheorem public import CyberAlchemy.ProtorealOperator
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
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealAlgebra_precession(lean_object*);
lean_object* lp_CyberAlchemy_DualityTheorem_standard__resonance(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealAlgebra_subtraction(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealAlgebra_precession(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_MonsterInverse_monster__inv(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_ProtorealAlgebra_subtraction(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_DualityTheorem_standard__resonance(x_1);
return x_2;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_MonsterInverse(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_DualityTheorem(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealOperator(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_GeneralInversion(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_MonsterInverse(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_DualityTheorem(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealOperator(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
