// Lean compiler output
// Module: CyberAlchemy.SharedLatentSpace
// Imports: public import Init public import CyberAlchemy.LittleDelta public import CyberAlchemy.AgenticFrame public import CyberAlchemy.ErrorCorrection public import CyberAlchemy.SchwarzianTruth public import CyberAlchemy.TopologicalImaginary public import CyberAlchemy.LieAlgebra
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
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
static lean_once_cell_t lp_CyberAlchemy_SharedLatentSpace_hodge__attractor___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_SharedLatentSpace_hodge__attractor___closed__0;
LEAN_EXPORT lean_object* lp_CyberAlchemy_SharedLatentSpace_hodge__attractor;
static lean_object* _init_lp_CyberAlchemy_SharedLatentSpace_hodge__attractor___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
x_2 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1279875089____hygCtx___hyg_8_;
x_3 = lean_alloc_ctor(0, 5, 0);
lean_ctor_set(x_3, 0, x_2);
lean_ctor_set(x_3, 1, x_2);
lean_ctor_set(x_3, 2, x_2);
lean_ctor_set(x_3, 3, x_1);
lean_ctor_set(x_3, 4, x_1);
return x_3;
}
}
static lean_object* _init_lp_CyberAlchemy_SharedLatentSpace_hodge__attractor(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_obj_once(&lp_CyberAlchemy_SharedLatentSpace_hodge__attractor___closed__0, &lp_CyberAlchemy_SharedLatentSpace_hodge__attractor___closed__0_once, _init_lp_CyberAlchemy_SharedLatentSpace_hodge__attractor___closed__0);
return x_1;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_LittleDelta(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_AgenticFrame(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ErrorCorrection(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_SchwarzianTruth(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_TopologicalImaginary(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_LieAlgebra(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_SharedLatentSpace(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_LittleDelta(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_AgenticFrame(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ErrorCorrection(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_SchwarzianTruth(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_TopologicalImaginary(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_LieAlgebra(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_SharedLatentSpace_hodge__attractor = _init_lp_CyberAlchemy_SharedLatentSpace_hodge__attractor();
lean_mark_persistent(lp_CyberAlchemy_SharedLatentSpace_hodge__attractor);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
