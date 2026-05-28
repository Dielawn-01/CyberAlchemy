// Lean compiler output
// Module: CyberAlchemy.OptimalCompute
// Imports: public import Init public import CyberAlchemy.NonstandardBridge public import CyberAlchemy.MonsterLattice
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
LEAN_EXPORT lean_object* lp_CyberAlchemy_OptimalCompute_leech__key;
LEAN_EXPORT lean_object* lp_CyberAlchemy_OptimalCompute_harmonic__buffer;
LEAN_EXPORT lean_object* lp_CyberAlchemy_OptimalCompute_topological__buffer;
LEAN_EXPORT lean_object* lp_CyberAlchemy_OptimalCompute_saeptation;
LEAN_EXPORT lean_object* lp_CyberAlchemy_OptimalCompute_hexation__degree;
static lean_object* _init_lp_CyberAlchemy_OptimalCompute_leech__key(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(24u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_OptimalCompute_harmonic__buffer(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(6u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_OptimalCompute_topological__buffer(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(42u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_OptimalCompute_saeptation(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(7u);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_OptimalCompute_hexation__degree(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_unsigned_to_nat(6u);
return x_1;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_NonstandardBridge(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_MonsterLattice(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_OptimalCompute(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_NonstandardBridge(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_MonsterLattice(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_OptimalCompute_leech__key = _init_lp_CyberAlchemy_OptimalCompute_leech__key();
lean_mark_persistent(lp_CyberAlchemy_OptimalCompute_leech__key);
lp_CyberAlchemy_OptimalCompute_harmonic__buffer = _init_lp_CyberAlchemy_OptimalCompute_harmonic__buffer();
lean_mark_persistent(lp_CyberAlchemy_OptimalCompute_harmonic__buffer);
lp_CyberAlchemy_OptimalCompute_topological__buffer = _init_lp_CyberAlchemy_OptimalCompute_topological__buffer();
lean_mark_persistent(lp_CyberAlchemy_OptimalCompute_topological__buffer);
lp_CyberAlchemy_OptimalCompute_saeptation = _init_lp_CyberAlchemy_OptimalCompute_saeptation();
lean_mark_persistent(lp_CyberAlchemy_OptimalCompute_saeptation);
lp_CyberAlchemy_OptimalCompute_hexation__degree = _init_lp_CyberAlchemy_OptimalCompute_hexation__degree();
lean_mark_persistent(lp_CyberAlchemy_OptimalCompute_hexation__degree);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
