// Lean compiler output
// Module: CyberAlchemy.RelativisticContinuum
// Imports: public import Init public import CyberAlchemy.ProtorealManifold public import CyberAlchemy.FusionRing public import CyberAlchemy.ProtorealAxioms
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
LEAN_EXPORT lean_object* lp_CyberAlchemy_RelativisticContinuum_speed__of__light;
extern lean_object* lp_CyberAlchemy_ProtorealManifold_iota;
LEAN_EXPORT lean_object* lp_CyberAlchemy_RelativisticContinuum_reduced__planck;
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
static lean_once_cell_t lp_CyberAlchemy_RelativisticContinuum_planck__floor___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_RelativisticContinuum_planck__floor___closed__0;
LEAN_EXPORT lean_object* lp_CyberAlchemy_RelativisticContinuum_planck__floor;
static lean_once_cell_t lp_CyberAlchemy_RelativisticContinuum_hubble__ceiling___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_RelativisticContinuum_hubble__ceiling___closed__0;
LEAN_EXPORT lean_object* lp_CyberAlchemy_RelativisticContinuum_hubble__ceiling;
static lean_object* _init_lp_CyberAlchemy_RelativisticContinuum_speed__of__light(void) {
_start:
{
lean_object* x_1; 
x_1 = lp_CyberAlchemy_ProtorealManifold_omega;
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_RelativisticContinuum_reduced__planck(void) {
_start:
{
lean_object* x_1; 
x_1 = lp_CyberAlchemy_ProtorealManifold_iota;
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_RelativisticContinuum_planck__floor___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
x_2 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
x_3 = lean_alloc_ctor(0, 5, 0);
lean_ctor_set(x_3, 0, x_2);
lean_ctor_set(x_3, 1, x_2);
lean_ctor_set(x_3, 2, x_2);
lean_ctor_set(x_3, 3, x_1);
lean_ctor_set(x_3, 4, x_2);
return x_3;
}
}
static lean_object* _init_lp_CyberAlchemy_RelativisticContinuum_planck__floor(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_obj_once(&lp_CyberAlchemy_RelativisticContinuum_planck__floor___closed__0, &lp_CyberAlchemy_RelativisticContinuum_planck__floor___closed__0_once, _init_lp_CyberAlchemy_RelativisticContinuum_planck__floor___closed__0);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_RelativisticContinuum_hubble__ceiling___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
x_2 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
x_3 = lean_alloc_ctor(0, 5, 0);
lean_ctor_set(x_3, 0, x_2);
lean_ctor_set(x_3, 1, x_2);
lean_ctor_set(x_3, 2, x_2);
lean_ctor_set(x_3, 3, x_2);
lean_ctor_set(x_3, 4, x_1);
return x_3;
}
}
static lean_object* _init_lp_CyberAlchemy_RelativisticContinuum_hubble__ceiling(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_obj_once(&lp_CyberAlchemy_RelativisticContinuum_hubble__ceiling___closed__0, &lp_CyberAlchemy_RelativisticContinuum_hubble__ceiling___closed__0_once, _init_lp_CyberAlchemy_RelativisticContinuum_hubble__ceiling___closed__0);
return x_1;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_FusionRing(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealAxioms(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_RelativisticContinuum(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_FusionRing(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealAxioms(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_RelativisticContinuum_speed__of__light = _init_lp_CyberAlchemy_RelativisticContinuum_speed__of__light();
lean_mark_persistent(lp_CyberAlchemy_RelativisticContinuum_speed__of__light);
lp_CyberAlchemy_RelativisticContinuum_reduced__planck = _init_lp_CyberAlchemy_RelativisticContinuum_reduced__planck();
lean_mark_persistent(lp_CyberAlchemy_RelativisticContinuum_reduced__planck);
lp_CyberAlchemy_RelativisticContinuum_planck__floor = _init_lp_CyberAlchemy_RelativisticContinuum_planck__floor();
lean_mark_persistent(lp_CyberAlchemy_RelativisticContinuum_planck__floor);
lp_CyberAlchemy_RelativisticContinuum_hubble__ceiling = _init_lp_CyberAlchemy_RelativisticContinuum_hubble__ceiling();
lean_mark_persistent(lp_CyberAlchemy_RelativisticContinuum_hubble__ceiling);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
