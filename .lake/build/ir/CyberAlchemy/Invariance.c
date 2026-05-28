// Lean compiler output
// Module: CyberAlchemy.Invariance
// Imports: public import Init public import CyberAlchemy.PentagonCoherence public import CyberAlchemy.Rigidity public import CyberAlchemy.FusionRing public import CyberAlchemy.Semisimple public import CyberAlchemy.EulerPerception public import CyberAlchemy.CommutatorGap public import CyberAlchemy.MassGap public import CyberAlchemy.StructuralHeterogeneity public import CyberAlchemy.HodgeConjecture public import CyberAlchemy.MayerVietoris
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
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_PentagonCoherence(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_Rigidity(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_FusionRing(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_Semisimple(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_EulerPerception(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_CommutatorGap(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_MassGap(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_StructuralHeterogeneity(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_HodgeConjecture(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_MayerVietoris(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_Invariance(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_PentagonCoherence(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_Rigidity(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_FusionRing(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_Semisimple(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_EulerPerception(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_CommutatorGap(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_MassGap(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_StructuralHeterogeneity(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_HodgeConjecture(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_MayerVietoris(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
