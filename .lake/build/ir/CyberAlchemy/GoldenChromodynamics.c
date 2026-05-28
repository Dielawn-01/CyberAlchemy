// Lean compiler output
// Module: CyberAlchemy.GoldenChromodynamics
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
lean_object* lean_nat_mod(lean_object*, lean_object*);
static lean_once_cell_t lp_CyberAlchemy_GoldenChromodynamics_golden__color___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_GoldenChromodynamics_golden__color___closed__0;
LEAN_EXPORT lean_object* lp_CyberAlchemy_GoldenChromodynamics_golden__color;
static lean_object* _init_lp_CyberAlchemy_GoldenChromodynamics_golden__color___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lean_unsigned_to_nat(229u);
x_2 = lean_cstr_to_nat("10509215371264");
x_3 = lean_nat_mod(x_2, x_1);
return x_3;
}
}
static lean_object* _init_lp_CyberAlchemy_GoldenChromodynamics_golden__color(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_obj_once(&lp_CyberAlchemy_GoldenChromodynamics_golden__color___closed__0, &lp_CyberAlchemy_GoldenChromodynamics_golden__color___closed__0_once, _init_lp_CyberAlchemy_GoldenChromodynamics_golden__color___closed__0);
return x_1;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_GoldenChromodynamics(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_GoldenChromodynamics_golden__color = _init_lp_CyberAlchemy_GoldenChromodynamics_golden__color();
lean_mark_persistent(lp_CyberAlchemy_GoldenChromodynamics_golden__color);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
