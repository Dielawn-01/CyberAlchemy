// Lean compiler output
// Module: CyberAlchemy.GoldenLattice
// Imports: public import Init public import CyberAlchemy.ProtorealManifold
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
LEAN_EXPORT lean_object* lp_CyberAlchemy_GoldenLattice_ord__71;
LEAN_EXPORT lean_object* lp_CyberAlchemy_GoldenLattice_ord__181;
LEAN_EXPORT lean_object* lp_CyberAlchemy_GoldenLattice_ord__229;
static lean_object* _init_lp_CyberAlchemy_GoldenLattice_ord__71(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(35u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_GoldenLattice_ord__181(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(45u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_GoldenLattice_ord__229(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(114u);
return x_1;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_GoldenLattice(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_GoldenLattice_ord__71 = _init_lp_CyberAlchemy_GoldenLattice_ord__71();
lean_mark_persistent(lp_CyberAlchemy_GoldenLattice_ord__71);
lp_CyberAlchemy_GoldenLattice_ord__181 = _init_lp_CyberAlchemy_GoldenLattice_ord__181();
lean_mark_persistent(lp_CyberAlchemy_GoldenLattice_ord__181);
lp_CyberAlchemy_GoldenLattice_ord__229 = _init_lp_CyberAlchemy_GoldenLattice_ord__229();
lean_mark_persistent(lp_CyberAlchemy_GoldenLattice_ord__229);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
