// Lean compiler output
// Module: CyberAlchemy.GaugeEmergence
// Imports: public import Init public import Mathlib.Data.Real.Basic public import Mathlib.Tactic.Linarith public import Mathlib.Tactic.NormNum public import CyberAlchemy.CyberBundle
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
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_g2__fundamental;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_g2__adjoint;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_u1__singlet;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_su3__fundamental;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_su3__antifundamental;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__U1;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__SU2;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__SU3;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_standard__model__generators;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_gauge__forces;
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_g2__fundamental(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(7u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_g2__adjoint(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(14u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_u1__singlet(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(1u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_su3__fundamental(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(3u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_su3__antifundamental(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(3u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__U1(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(1u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__SU2(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(3u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__SU3(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(8u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_standard__model__generators(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(12u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_gauge__forces(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(3u);
return x_1;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Real_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_Linarith(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_NormNum(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_CyberBundle(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_GaugeEmergence(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Real_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Tactic_Linarith(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Tactic_NormNum(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_CyberBundle(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_g2__fundamental = _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_g2__fundamental();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_g2__fundamental);
lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_g2__adjoint = _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_g2__adjoint();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_g2__adjoint);
lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_u1__singlet = _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_u1__singlet();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_u1__singlet);
lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_su3__fundamental = _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_su3__fundamental();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_su3__fundamental);
lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_su3__antifundamental = _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_su3__antifundamental();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_su3__antifundamental);
lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__U1 = _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__U1();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__U1);
lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__SU2 = _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__SU2();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__SU2);
lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__SU3 = _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__SU3();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_dim__SU3);
lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_standard__model__generators = _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_standard__model__generators();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_standard__model__generators);
lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_gauge__forces = _init_lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_gauge__forces();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_GaugeEmergence_gauge__forces);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
