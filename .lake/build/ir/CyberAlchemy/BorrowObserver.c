// Lean compiler output
// Module: CyberAlchemy.BorrowObserver
// Imports: public import Init public import Mathlib.Data.Real.Basic public import CyberAlchemy.ProtorealManifold public import CyberAlchemy.HolographicCollapse
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
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
static lean_once_cell_t lp_CyberAlchemy_BorrowObserver_borrow__collapse___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_BorrowObserver_borrow__collapse___closed__0;
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* lp_CyberAlchemy_HolographicCollapse_collapse__state(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_BorrowObserver_borrow__collapse(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_BorrowObserver_borrow__collapse___boxed(lean_object*);
static lean_object* _init_lp_CyberAlchemy_BorrowObserver_borrow__collapse___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; 
x_1 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
x_2 = lean_alloc_ctor(0, 3, 0);
lean_ctor_set(x_2, 0, x_1);
lean_ctor_set(x_2, 1, x_1);
lean_ctor_set(x_2, 2, x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_BorrowObserver_borrow__collapse(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; lean_object* x_4; lean_object* x_10; uint8_t x_11; 
x_2 = lean_ctor_get(x_1, 0);
x_3 = lean_ctor_get(x_1, 1);
x_4 = lean_ctor_get(x_1, 2);
x_10 = lean_unsigned_to_nat(1u);
x_11 = lean_nat_dec_eq(x_3, x_10);
if (x_11 == 0)
{
goto block_9;
}
else
{
lean_object* x_12; uint8_t x_13; 
x_12 = lean_unsigned_to_nat(0u);
x_13 = lean_nat_dec_eq(x_4, x_12);
if (x_13 == 0)
{
goto block_9;
}
else
{
lean_object* x_14; 
x_14 = lp_CyberAlchemy_HolographicCollapse_collapse__state(x_2);
return x_14;
}
}
block_9:
{
lean_object* x_5; uint8_t x_6; 
x_5 = lean_unsigned_to_nat(0u);
x_6 = lean_nat_dec_eq(x_3, x_5);
if (x_6 == 0)
{
lean_object* x_7; 
x_7 = lean_obj_once(&lp_CyberAlchemy_BorrowObserver_borrow__collapse___closed__0, &lp_CyberAlchemy_BorrowObserver_borrow__collapse___closed__0_once, _init_lp_CyberAlchemy_BorrowObserver_borrow__collapse___closed__0);
return x_7;
}
else
{
lean_object* x_8; 
x_8 = lp_CyberAlchemy_HolographicCollapse_collapse__state(x_2);
return x_8;
}
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_BorrowObserver_borrow__collapse___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_BorrowObserver_borrow__collapse(x_1);
lean_dec_ref(x_1);
return x_2;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Real_Basic(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_HolographicCollapse(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_BorrowObserver(uint8_t builtin) {
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
res = initialize_CyberAlchemy_CyberAlchemy_HolographicCollapse(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
