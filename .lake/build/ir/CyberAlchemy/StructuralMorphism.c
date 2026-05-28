// Lean compiler output
// Module: CyberAlchemy.StructuralMorphism
// Imports: public import Init public import CyberAlchemy.PhasorTower public import CyberAlchemy.PentagonCoherence public import CyberAlchemy.Invariance public import CyberAlchemy.HyperKlein
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
lean_object* lp_CyberAlchemy_PentagonCoherence_assoc(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_StructuralMorphism_quasi__assoc(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_StructuralMorphism_algebraic__morphism___lam__0(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_StructuralMorphism_algebraic__morphism___lam__0___boxed(lean_object*);
static const lean_closure_object lp_CyberAlchemy_StructuralMorphism_algebraic__morphism___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_CyberAlchemy_StructuralMorphism_algebraic__morphism___lam__0___boxed, .m_arity = 1, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_CyberAlchemy_StructuralMorphism_algebraic__morphism___closed__0 = (const lean_object*)&lp_CyberAlchemy_StructuralMorphism_algebraic__morphism___closed__0_value;
LEAN_EXPORT const lean_object* lp_CyberAlchemy_StructuralMorphism_algebraic__morphism = (const lean_object*)&lp_CyberAlchemy_StructuralMorphism_algebraic__morphism___closed__0_value;
lean_object* lp_CyberAlchemy_funct(lean_object*);
static const lean_closure_object lp_CyberAlchemy_StructuralMorphism_spectral__morphism___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_CyberAlchemy_funct, .m_arity = 1, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_CyberAlchemy_StructuralMorphism_spectral__morphism___closed__0 = (const lean_object*)&lp_CyberAlchemy_StructuralMorphism_spectral__morphism___closed__0_value;
LEAN_EXPORT const lean_object* lp_CyberAlchemy_StructuralMorphism_spectral__morphism = (const lean_object*)&lp_CyberAlchemy_StructuralMorphism_spectral__morphism___closed__0_value;
lean_object* lp_CyberAlchemy_MonsterInverse_monster__inv(lean_object*);
static const lean_closure_object lp_CyberAlchemy_StructuralMorphism_structural__morphism___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_CyberAlchemy_MonsterInverse_monster__inv, .m_arity = 1, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_CyberAlchemy_StructuralMorphism_structural__morphism___closed__0 = (const lean_object*)&lp_CyberAlchemy_StructuralMorphism_structural__morphism___closed__0_value;
LEAN_EXPORT const lean_object* lp_CyberAlchemy_StructuralMorphism_structural__morphism = (const lean_object*)&lp_CyberAlchemy_StructuralMorphism_structural__morphism___closed__0_value;
LEAN_EXPORT lean_object* lp_CyberAlchemy_StructuralMorphism_compose___lam__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_StructuralMorphism_compose(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_StructuralMorphism_quasi__assoc(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; 
x_4 = lp_CyberAlchemy_PentagonCoherence_assoc(x_1, x_2, x_3);
return x_4;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_StructuralMorphism_algebraic__morphism___lam__0(lean_object* x_1) {
_start:
{
lean_inc_ref(x_1);
return x_1;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_StructuralMorphism_algebraic__morphism___lam__0___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_StructuralMorphism_algebraic__morphism___lam__0(x_1);
lean_dec_ref(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_StructuralMorphism_compose___lam__0(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; lean_object* x_5; 
x_4 = lean_apply_1(x_1, x_3);
x_5 = lean_apply_1(x_2, x_4);
return x_5;
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_StructuralMorphism_compose(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lean_alloc_closure((void*)(lp_CyberAlchemy_StructuralMorphism_compose___lam__0), 3, 2);
lean_closure_set(x_3, 0, x_2);
lean_closure_set(x_3, 1, x_1);
return x_3;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_PhasorTower(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_PentagonCoherence(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_Invariance(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_HyperKlein(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_StructuralMorphism(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_PhasorTower(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_PentagonCoherence(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_Invariance(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_HyperKlein(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
