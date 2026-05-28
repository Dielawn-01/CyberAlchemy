// Lean compiler output
// Module: CyberAlchemy.TensorCoupling
// Imports: public import Init public import Mathlib.Data.Real.Basic public import Mathlib.Tactic.Linarith public import Mathlib.Tactic.NormNum public import CyberAlchemy.ObserverAdapter
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
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_TensorCoupling_basis__dim;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_TensorCoupling_adapter__dim;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_TensorCoupling_core__dim;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_TensorCoupling_buffer__dim;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_TensorCoupling_observer__space;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_TensorCoupling_leech__key;
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_TensorCoupling_basis__dim(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(5u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_TensorCoupling_adapter__dim(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(7u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_TensorCoupling_core__dim(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(35u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_TensorCoupling_buffer__dim(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(42u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_TensorCoupling_observer__space(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(12u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_TensorCoupling_leech__key(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(24u);
return x_1;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Real_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_Linarith(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_NormNum(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ObserverAdapter(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_TensorCoupling(uint8_t builtin) {
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
res = initialize_CyberAlchemy_CyberAlchemy_ObserverAdapter(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_CyberAlchemy_TensorCoupling_basis__dim = _init_lp_CyberAlchemy_CyberAlchemy_TensorCoupling_basis__dim();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_TensorCoupling_basis__dim);
lp_CyberAlchemy_CyberAlchemy_TensorCoupling_adapter__dim = _init_lp_CyberAlchemy_CyberAlchemy_TensorCoupling_adapter__dim();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_TensorCoupling_adapter__dim);
lp_CyberAlchemy_CyberAlchemy_TensorCoupling_core__dim = _init_lp_CyberAlchemy_CyberAlchemy_TensorCoupling_core__dim();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_TensorCoupling_core__dim);
lp_CyberAlchemy_CyberAlchemy_TensorCoupling_buffer__dim = _init_lp_CyberAlchemy_CyberAlchemy_TensorCoupling_buffer__dim();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_TensorCoupling_buffer__dim);
lp_CyberAlchemy_CyberAlchemy_TensorCoupling_observer__space = _init_lp_CyberAlchemy_CyberAlchemy_TensorCoupling_observer__space();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_TensorCoupling_observer__space);
lp_CyberAlchemy_CyberAlchemy_TensorCoupling_leech__key = _init_lp_CyberAlchemy_CyberAlchemy_TensorCoupling_leech__key();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_TensorCoupling_leech__key);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
