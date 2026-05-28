// Lean compiler output
// Module: CyberAlchemy.PrimeGenerators
// Imports: public import Init public import Mathlib.Tactic.NormNum public import Mathlib.Tactic.Linarith public import Mathlib.Data.Nat.Prime.Basic public import CyberAlchemy.CyberBundle
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
static const lean_ctor_object lp_CyberAlchemy_prime__generators___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(41) << 1) | 1)),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_CyberAlchemy_prime__generators___closed__0 = (const lean_object*)&lp_CyberAlchemy_prime__generators___closed__0_value;
static const lean_ctor_object lp_CyberAlchemy_prime__generators___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(37) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_prime__generators___closed__0_value)}};
static const lean_object* lp_CyberAlchemy_prime__generators___closed__1 = (const lean_object*)&lp_CyberAlchemy_prime__generators___closed__1_value;
static const lean_ctor_object lp_CyberAlchemy_prime__generators___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(31) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_prime__generators___closed__1_value)}};
static const lean_object* lp_CyberAlchemy_prime__generators___closed__2 = (const lean_object*)&lp_CyberAlchemy_prime__generators___closed__2_value;
static const lean_ctor_object lp_CyberAlchemy_prime__generators___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(29) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_prime__generators___closed__2_value)}};
static const lean_object* lp_CyberAlchemy_prime__generators___closed__3 = (const lean_object*)&lp_CyberAlchemy_prime__generators___closed__3_value;
static const lean_ctor_object lp_CyberAlchemy_prime__generators___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(23) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_prime__generators___closed__3_value)}};
static const lean_object* lp_CyberAlchemy_prime__generators___closed__4 = (const lean_object*)&lp_CyberAlchemy_prime__generators___closed__4_value;
static const lean_ctor_object lp_CyberAlchemy_prime__generators___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(19) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_prime__generators___closed__4_value)}};
static const lean_object* lp_CyberAlchemy_prime__generators___closed__5 = (const lean_object*)&lp_CyberAlchemy_prime__generators___closed__5_value;
static const lean_ctor_object lp_CyberAlchemy_prime__generators___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(17) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_prime__generators___closed__5_value)}};
static const lean_object* lp_CyberAlchemy_prime__generators___closed__6 = (const lean_object*)&lp_CyberAlchemy_prime__generators___closed__6_value;
static const lean_ctor_object lp_CyberAlchemy_prime__generators___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(13) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_prime__generators___closed__6_value)}};
static const lean_object* lp_CyberAlchemy_prime__generators___closed__7 = (const lean_object*)&lp_CyberAlchemy_prime__generators___closed__7_value;
static const lean_ctor_object lp_CyberAlchemy_prime__generators___closed__8_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(11) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_prime__generators___closed__7_value)}};
static const lean_object* lp_CyberAlchemy_prime__generators___closed__8 = (const lean_object*)&lp_CyberAlchemy_prime__generators___closed__8_value;
static const lean_ctor_object lp_CyberAlchemy_prime__generators___closed__9_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_prime__generators___closed__8_value)}};
static const lean_object* lp_CyberAlchemy_prime__generators___closed__9 = (const lean_object*)&lp_CyberAlchemy_prime__generators___closed__9_value;
static const lean_ctor_object lp_CyberAlchemy_prime__generators___closed__10_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_prime__generators___closed__9_value)}};
static const lean_object* lp_CyberAlchemy_prime__generators___closed__10 = (const lean_object*)&lp_CyberAlchemy_prime__generators___closed__10_value;
static const lean_ctor_object lp_CyberAlchemy_prime__generators___closed__11_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_prime__generators___closed__10_value)}};
static const lean_object* lp_CyberAlchemy_prime__generators___closed__11 = (const lean_object*)&lp_CyberAlchemy_prime__generators___closed__11_value;
static const lean_ctor_object lp_CyberAlchemy_prime__generators___closed__12_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_prime__generators___closed__11_value)}};
static const lean_object* lp_CyberAlchemy_prime__generators___closed__12 = (const lean_object*)&lp_CyberAlchemy_prime__generators___closed__12_value;
LEAN_EXPORT const lean_object* lp_CyberAlchemy_prime__generators = (const lean_object*)&lp_CyberAlchemy_prime__generators___closed__12_value;
static const lean_ctor_object lp_CyberAlchemy_physical__primes___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(11) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_prime__generators___closed__2_value)}};
static const lean_object* lp_CyberAlchemy_physical__primes___closed__0 = (const lean_object*)&lp_CyberAlchemy_physical__primes___closed__0_value;
static const lean_ctor_object lp_CyberAlchemy_physical__primes___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_physical__primes___closed__0_value)}};
static const lean_object* lp_CyberAlchemy_physical__primes___closed__1 = (const lean_object*)&lp_CyberAlchemy_physical__primes___closed__1_value;
static const lean_ctor_object lp_CyberAlchemy_physical__primes___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_physical__primes___closed__1_value)}};
static const lean_object* lp_CyberAlchemy_physical__primes___closed__2 = (const lean_object*)&lp_CyberAlchemy_physical__primes___closed__2_value;
static const lean_ctor_object lp_CyberAlchemy_physical__primes___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_physical__primes___closed__2_value)}};
static const lean_object* lp_CyberAlchemy_physical__primes___closed__3 = (const lean_object*)&lp_CyberAlchemy_physical__primes___closed__3_value;
static const lean_ctor_object lp_CyberAlchemy_physical__primes___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_physical__primes___closed__3_value)}};
static const lean_object* lp_CyberAlchemy_physical__primes___closed__4 = (const lean_object*)&lp_CyberAlchemy_physical__primes___closed__4_value;
LEAN_EXPORT const lean_object* lp_CyberAlchemy_physical__primes = (const lean_object*)&lp_CyberAlchemy_physical__primes___closed__4_value;
static const lean_ctor_object lp_CyberAlchemy_consciousness__primes___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(29) << 1) | 1)),((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_CyberAlchemy_consciousness__primes___closed__0 = (const lean_object*)&lp_CyberAlchemy_consciousness__primes___closed__0_value;
static const lean_ctor_object lp_CyberAlchemy_consciousness__primes___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(23) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_consciousness__primes___closed__0_value)}};
static const lean_object* lp_CyberAlchemy_consciousness__primes___closed__1 = (const lean_object*)&lp_CyberAlchemy_consciousness__primes___closed__1_value;
static const lean_ctor_object lp_CyberAlchemy_consciousness__primes___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(19) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_consciousness__primes___closed__1_value)}};
static const lean_object* lp_CyberAlchemy_consciousness__primes___closed__2 = (const lean_object*)&lp_CyberAlchemy_consciousness__primes___closed__2_value;
static const lean_ctor_object lp_CyberAlchemy_consciousness__primes___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(17) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_consciousness__primes___closed__2_value)}};
static const lean_object* lp_CyberAlchemy_consciousness__primes___closed__3 = (const lean_object*)&lp_CyberAlchemy_consciousness__primes___closed__3_value;
static const lean_ctor_object lp_CyberAlchemy_consciousness__primes___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*2 + 0, .m_other = 2, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(13) << 1) | 1)),((lean_object*)&lp_CyberAlchemy_consciousness__primes___closed__3_value)}};
static const lean_object* lp_CyberAlchemy_consciousness__primes___closed__4 = (const lean_object*)&lp_CyberAlchemy_consciousness__primes___closed__4_value;
LEAN_EXPORT const lean_object* lp_CyberAlchemy_consciousness__primes = (const lean_object*)&lp_CyberAlchemy_consciousness__primes___closed__4_value;
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
lean_object* lean_nat_add(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_fib(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_fib___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_fib(lean_object* x_1) {
_start:
{
lean_object* x_2; uint8_t x_3; 
x_2 = lean_unsigned_to_nat(0u);
x_3 = lean_nat_dec_eq(x_1, x_2);
if (x_3 == 1)
{
return x_2;
}
else
{
lean_object* x_4; lean_object* x_5; uint8_t x_6; 
x_4 = lean_unsigned_to_nat(1u);
x_5 = lean_nat_sub(x_1, x_4);
x_6 = lean_nat_dec_eq(x_5, x_2);
if (x_6 == 1)
{
lean_dec(x_5);
return x_4;
}
else
{
lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; lean_object* x_11; 
x_7 = lean_nat_sub(x_5, x_4);
lean_dec(x_5);
x_8 = lean_nat_add(x_7, x_4);
x_9 = lp_CyberAlchemy_fib(x_8);
lean_dec(x_8);
x_10 = lp_CyberAlchemy_fib(x_7);
lean_dec(x_7);
x_11 = lean_nat_add(x_9, x_10);
lean_dec(x_10);
lean_dec(x_9);
return x_11;
}
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_fib___boxed(lean_object* x_1) {
_start:
{
lean_object* x_2; 
x_2 = lp_CyberAlchemy_fib(x_1);
lean_dec(x_1);
return x_2;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_NormNum(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Tactic_Linarith(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Nat_Prime_Basic(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_CyberBundle(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_PrimeGenerators(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Tactic_NormNum(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Tactic_Linarith(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Nat_Prime_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_CyberBundle(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
