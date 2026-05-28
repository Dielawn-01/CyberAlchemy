// Lean compiler output
// Module: CyberAlchemy.MetalloOrganicSemantics
// Imports: public import Init public import Mathlib.Data.Real.Basic public import Mathlib.Data.Complex.Basic public import CyberAlchemy.TopologicalUncertainty public import CyberAlchemy.Bitcollapse
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
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_rna__dimension;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_dna__dimension;
LEAN_EXPORT lean_object* lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_mof__semantic__dimension;
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_rna__dimension(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(6u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_dna__dimension(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(7u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_mof__semantic__dimension(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(42u);
return x_1;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Real_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Complex_Basic(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_TopologicalUncertainty(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_Bitcollapse(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Real_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Complex_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_TopologicalUncertainty(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_Bitcollapse(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_rna__dimension = _init_lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_rna__dimension();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_rna__dimension);
lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_dna__dimension = _init_lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_dna__dimension();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_dna__dimension);
lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_mof__semantic__dimension = _init_lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_mof__semantic__dimension();
lean_mark_persistent(lp_CyberAlchemy_CyberAlchemy_MetalloOrganicSemantics_mof__semantic__dimension);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
