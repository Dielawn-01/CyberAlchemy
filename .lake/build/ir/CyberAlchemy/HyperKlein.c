// Lean compiler output
// Module: CyberAlchemy.HyperKlein
// Imports: public import Init public import CyberAlchemy.ProtorealManifold public import CyberAlchemy.ProtorealOperator public import CyberAlchemy.FusionRing public import CyberAlchemy.PentagonCoherence public import CyberAlchemy.MonsterInverse public import CyberAlchemy.Invariance
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
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
extern lean_object* lp_CyberAlchemy_FusionRing_e1;
lean_object* lean_nat_sub(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HyperKlein_klein__pow(lean_object*, lean_object*);
lean_object* lp_CyberAlchemy_ProtorealManifold_mul(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HyperKlein_klein__pow___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_HyperKlein_klein__pow(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; uint8_t x_4; 
x_3 = lean_unsigned_to_nat(0u);
x_4 = lean_nat_dec_eq(x_2, x_3);
if (x_4 == 1)
{
lean_object* x_5; 
lean_dec_ref(x_1);
x_5 = lp_CyberAlchemy_FusionRing_e1;
return x_5;
}
else
{
lean_object* x_6; lean_object* x_7; lean_object* x_8; lean_object* x_9; 
x_6 = lean_unsigned_to_nat(1u);
x_7 = lean_nat_sub(x_2, x_6);
lean_inc_ref(x_1);
x_8 = lp_CyberAlchemy_HyperKlein_klein__pow(x_1, x_7);
lean_dec(x_7);
x_9 = lp_CyberAlchemy_ProtorealManifold_mul(x_8, x_1);
return x_9;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_HyperKlein_klein__pow___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lp_CyberAlchemy_HyperKlein_klein__pow(x_1, x_2);
lean_dec(x_2);
return x_3;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealOperator(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_FusionRing(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_PentagonCoherence(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_MonsterInverse(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_Invariance(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_HyperKlein(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealOperator(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_FusionRing(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_PentagonCoherence(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_MonsterInverse(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_Invariance(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
