// Lean compiler output
// Module: CyberAlchemy.ProtorealAlgebra
// Imports: public import Init public import CyberAlchemy.ProtorealManifold public import CyberAlchemy.ProtorealMesh
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
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_instAddKleinMesh___lam__0(lean_object*, lean_object*);
static const lean_closure_object lp_CyberAlchemy_instAddKleinMesh___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_CyberAlchemy_instAddKleinMesh___lam__0, .m_arity = 2, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_CyberAlchemy_instAddKleinMesh___closed__0 = (const lean_object*)&lp_CyberAlchemy_instAddKleinMesh___closed__0_value;
LEAN_EXPORT const lean_object* lp_CyberAlchemy_instAddKleinMesh = (const lean_object*)&lp_CyberAlchemy_instAddKleinMesh___closed__0_value;
lean_object* lp_CyberAlchemy_ProtorealManifold_mul(lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_(lean_object*, lean_object*, lean_object*);
lean_object* lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_CyberAlchemy_instMulKleinMesh___lam__0(lean_object*, lean_object*);
static const lean_closure_object lp_CyberAlchemy_instMulKleinMesh___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_CyberAlchemy_instMulKleinMesh___lam__0, .m_arity = 2, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_CyberAlchemy_instMulKleinMesh___closed__0 = (const lean_object*)&lp_CyberAlchemy_instMulKleinMesh___closed__0_value;
LEAN_EXPORT const lean_object* lp_CyberAlchemy_instMulKleinMesh = (const lean_object*)&lp_CyberAlchemy_instMulKleinMesh___closed__0_value;
extern lean_object* lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
static lean_once_cell_t lp_CyberAlchemy_instZeroKleinMesh___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_instZeroKleinMesh___closed__0;
lean_object* lp_mathlib_Complex_ofReal(lean_object*);
static lean_once_cell_t lp_CyberAlchemy_instZeroKleinMesh___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_instZeroKleinMesh___closed__1;
static lean_once_cell_t lp_CyberAlchemy_instZeroKleinMesh___closed__2_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_instZeroKleinMesh___closed__2;
LEAN_EXPORT lean_object* lp_CyberAlchemy_instZeroKleinMesh;
static lean_once_cell_t lp_CyberAlchemy_instProtorealAlgebraKleinMesh___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_CyberAlchemy_instProtorealAlgebraKleinMesh___closed__0;
LEAN_EXPORT lean_object* lp_CyberAlchemy_instProtorealAlgebraKleinMesh;
LEAN_EXPORT lean_object* lp_CyberAlchemy_instAddKleinMesh___lam__0(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; lean_object* x_4; lean_object* x_5; uint8_t x_6; 
x_3 = lean_ctor_get(x_1, 0);
lean_inc_ref(x_3);
x_4 = lean_ctor_get(x_2, 0);
lean_inc_ref(x_4);
x_5 = lean_ctor_get(x_1, 1);
lean_inc_ref(x_5);
lean_dec_ref(x_1);
x_6 = !lean_is_exclusive(x_2);
if (x_6 == 0)
{
lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; lean_object* x_11; lean_object* x_12; lean_object* x_13; uint8_t x_14; 
x_7 = lean_ctor_get(x_2, 1);
x_8 = lean_ctor_get(x_2, 0);
lean_dec(x_8);
x_9 = lean_ctor_get(x_3, 0);
lean_inc(x_9);
x_10 = lean_ctor_get(x_3, 1);
lean_inc(x_10);
x_11 = lean_ctor_get(x_3, 2);
lean_inc(x_11);
x_12 = lean_ctor_get(x_3, 3);
lean_inc(x_12);
x_13 = lean_ctor_get(x_3, 4);
lean_inc(x_13);
lean_dec_ref(x_3);
x_14 = !lean_is_exclusive(x_4);
if (x_14 == 0)
{
lean_object* x_15; lean_object* x_16; lean_object* x_17; lean_object* x_18; lean_object* x_19; lean_object* x_20; lean_object* x_21; uint8_t x_22; 
x_15 = lean_ctor_get(x_4, 0);
x_16 = lean_ctor_get(x_4, 1);
x_17 = lean_ctor_get(x_4, 2);
x_18 = lean_ctor_get(x_4, 3);
x_19 = lean_ctor_get(x_4, 4);
x_20 = lean_ctor_get(x_5, 0);
lean_inc(x_20);
x_21 = lean_ctor_get(x_5, 1);
lean_inc(x_21);
lean_dec_ref(x_5);
x_22 = !lean_is_exclusive(x_7);
if (x_22 == 0)
{
lean_object* x_23; lean_object* x_24; lean_object* x_25; lean_object* x_26; lean_object* x_27; lean_object* x_28; lean_object* x_29; lean_object* x_30; lean_object* x_31; 
x_23 = lean_ctor_get(x_7, 0);
x_24 = lean_ctor_get(x_7, 1);
x_25 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_25, 0, x_9);
lean_closure_set(x_25, 1, x_15);
x_26 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_26, 0, x_10);
lean_closure_set(x_26, 1, x_16);
x_27 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_27, 0, x_11);
lean_closure_set(x_27, 1, x_17);
x_28 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_28, 0, x_12);
lean_closure_set(x_28, 1, x_18);
x_29 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_29, 0, x_13);
lean_closure_set(x_29, 1, x_19);
lean_ctor_set(x_4, 4, x_29);
lean_ctor_set(x_4, 3, x_28);
lean_ctor_set(x_4, 2, x_27);
lean_ctor_set(x_4, 1, x_26);
lean_ctor_set(x_4, 0, x_25);
x_30 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_30, 0, x_20);
lean_closure_set(x_30, 1, x_23);
x_31 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_31, 0, x_21);
lean_closure_set(x_31, 1, x_24);
lean_ctor_set(x_7, 1, x_31);
lean_ctor_set(x_7, 0, x_30);
return x_2;
}
else
{
lean_object* x_32; lean_object* x_33; lean_object* x_34; lean_object* x_35; lean_object* x_36; lean_object* x_37; lean_object* x_38; lean_object* x_39; lean_object* x_40; lean_object* x_41; 
x_32 = lean_ctor_get(x_7, 0);
x_33 = lean_ctor_get(x_7, 1);
lean_inc(x_33);
lean_inc(x_32);
lean_dec(x_7);
x_34 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_34, 0, x_9);
lean_closure_set(x_34, 1, x_15);
x_35 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_35, 0, x_10);
lean_closure_set(x_35, 1, x_16);
x_36 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_36, 0, x_11);
lean_closure_set(x_36, 1, x_17);
x_37 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_37, 0, x_12);
lean_closure_set(x_37, 1, x_18);
x_38 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_38, 0, x_13);
lean_closure_set(x_38, 1, x_19);
lean_ctor_set(x_4, 4, x_38);
lean_ctor_set(x_4, 3, x_37);
lean_ctor_set(x_4, 2, x_36);
lean_ctor_set(x_4, 1, x_35);
lean_ctor_set(x_4, 0, x_34);
x_39 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_39, 0, x_20);
lean_closure_set(x_39, 1, x_32);
x_40 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_40, 0, x_21);
lean_closure_set(x_40, 1, x_33);
x_41 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_41, 0, x_39);
lean_ctor_set(x_41, 1, x_40);
lean_ctor_set(x_2, 1, x_41);
return x_2;
}
}
else
{
lean_object* x_42; lean_object* x_43; lean_object* x_44; lean_object* x_45; lean_object* x_46; lean_object* x_47; lean_object* x_48; lean_object* x_49; lean_object* x_50; lean_object* x_51; lean_object* x_52; lean_object* x_53; lean_object* x_54; lean_object* x_55; lean_object* x_56; lean_object* x_57; lean_object* x_58; lean_object* x_59; lean_object* x_60; 
x_42 = lean_ctor_get(x_4, 0);
x_43 = lean_ctor_get(x_4, 1);
x_44 = lean_ctor_get(x_4, 2);
x_45 = lean_ctor_get(x_4, 3);
x_46 = lean_ctor_get(x_4, 4);
lean_inc(x_46);
lean_inc(x_45);
lean_inc(x_44);
lean_inc(x_43);
lean_inc(x_42);
lean_dec(x_4);
x_47 = lean_ctor_get(x_5, 0);
lean_inc(x_47);
x_48 = lean_ctor_get(x_5, 1);
lean_inc(x_48);
lean_dec_ref(x_5);
x_49 = lean_ctor_get(x_7, 0);
lean_inc(x_49);
x_50 = lean_ctor_get(x_7, 1);
lean_inc(x_50);
if (lean_is_exclusive(x_7)) {
 lean_ctor_release(x_7, 0);
 lean_ctor_release(x_7, 1);
 x_51 = x_7;
} else {
 lean_dec_ref(x_7);
 x_51 = lean_box(0);
}
x_52 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_52, 0, x_9);
lean_closure_set(x_52, 1, x_42);
x_53 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_53, 0, x_10);
lean_closure_set(x_53, 1, x_43);
x_54 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_54, 0, x_11);
lean_closure_set(x_54, 1, x_44);
x_55 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_55, 0, x_12);
lean_closure_set(x_55, 1, x_45);
x_56 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_56, 0, x_13);
lean_closure_set(x_56, 1, x_46);
x_57 = lean_alloc_ctor(0, 5, 0);
lean_ctor_set(x_57, 0, x_52);
lean_ctor_set(x_57, 1, x_53);
lean_ctor_set(x_57, 2, x_54);
lean_ctor_set(x_57, 3, x_55);
lean_ctor_set(x_57, 4, x_56);
x_58 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_58, 0, x_47);
lean_closure_set(x_58, 1, x_49);
x_59 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_59, 0, x_48);
lean_closure_set(x_59, 1, x_50);
if (lean_is_scalar(x_51)) {
 x_60 = lean_alloc_ctor(0, 2, 0);
} else {
 x_60 = x_51;
}
lean_ctor_set(x_60, 0, x_58);
lean_ctor_set(x_60, 1, x_59);
lean_ctor_set(x_2, 1, x_60);
lean_ctor_set(x_2, 0, x_57);
return x_2;
}
}
else
{
lean_object* x_61; lean_object* x_62; lean_object* x_63; lean_object* x_64; lean_object* x_65; lean_object* x_66; lean_object* x_67; lean_object* x_68; lean_object* x_69; lean_object* x_70; lean_object* x_71; lean_object* x_72; lean_object* x_73; lean_object* x_74; lean_object* x_75; lean_object* x_76; lean_object* x_77; lean_object* x_78; lean_object* x_79; lean_object* x_80; lean_object* x_81; lean_object* x_82; lean_object* x_83; lean_object* x_84; lean_object* x_85; lean_object* x_86; lean_object* x_87; 
x_61 = lean_ctor_get(x_2, 1);
lean_inc(x_61);
lean_dec(x_2);
x_62 = lean_ctor_get(x_3, 0);
lean_inc(x_62);
x_63 = lean_ctor_get(x_3, 1);
lean_inc(x_63);
x_64 = lean_ctor_get(x_3, 2);
lean_inc(x_64);
x_65 = lean_ctor_get(x_3, 3);
lean_inc(x_65);
x_66 = lean_ctor_get(x_3, 4);
lean_inc(x_66);
lean_dec_ref(x_3);
x_67 = lean_ctor_get(x_4, 0);
lean_inc(x_67);
x_68 = lean_ctor_get(x_4, 1);
lean_inc(x_68);
x_69 = lean_ctor_get(x_4, 2);
lean_inc(x_69);
x_70 = lean_ctor_get(x_4, 3);
lean_inc(x_70);
x_71 = lean_ctor_get(x_4, 4);
lean_inc(x_71);
if (lean_is_exclusive(x_4)) {
 lean_ctor_release(x_4, 0);
 lean_ctor_release(x_4, 1);
 lean_ctor_release(x_4, 2);
 lean_ctor_release(x_4, 3);
 lean_ctor_release(x_4, 4);
 x_72 = x_4;
} else {
 lean_dec_ref(x_4);
 x_72 = lean_box(0);
}
x_73 = lean_ctor_get(x_5, 0);
lean_inc(x_73);
x_74 = lean_ctor_get(x_5, 1);
lean_inc(x_74);
lean_dec_ref(x_5);
x_75 = lean_ctor_get(x_61, 0);
lean_inc(x_75);
x_76 = lean_ctor_get(x_61, 1);
lean_inc(x_76);
if (lean_is_exclusive(x_61)) {
 lean_ctor_release(x_61, 0);
 lean_ctor_release(x_61, 1);
 x_77 = x_61;
} else {
 lean_dec_ref(x_61);
 x_77 = lean_box(0);
}
x_78 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_78, 0, x_62);
lean_closure_set(x_78, 1, x_67);
x_79 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_79, 0, x_63);
lean_closure_set(x_79, 1, x_68);
x_80 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_80, 0, x_64);
lean_closure_set(x_80, 1, x_69);
x_81 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_81, 0, x_65);
lean_closure_set(x_81, 1, x_70);
x_82 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_82, 0, x_66);
lean_closure_set(x_82, 1, x_71);
if (lean_is_scalar(x_72)) {
 x_83 = lean_alloc_ctor(0, 5, 0);
} else {
 x_83 = x_72;
}
lean_ctor_set(x_83, 0, x_78);
lean_ctor_set(x_83, 1, x_79);
lean_ctor_set(x_83, 2, x_80);
lean_ctor_set(x_83, 3, x_81);
lean_ctor_set(x_83, 4, x_82);
x_84 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_84, 0, x_73);
lean_closure_set(x_84, 1, x_75);
x_85 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_85, 0, x_74);
lean_closure_set(x_85, 1, x_76);
if (lean_is_scalar(x_77)) {
 x_86 = lean_alloc_ctor(0, 2, 0);
} else {
 x_86 = x_77;
}
lean_ctor_set(x_86, 0, x_84);
lean_ctor_set(x_86, 1, x_85);
x_87 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_87, 0, x_83);
lean_ctor_set(x_87, 1, x_86);
return x_87;
}
}
}
LEAN_EXPORT lean_object* lp_CyberAlchemy_instMulKleinMesh___lam__0(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; lean_object* x_4; lean_object* x_5; uint8_t x_6; 
x_3 = lean_ctor_get(x_1, 1);
lean_inc_ref(x_3);
x_4 = lean_ctor_get(x_2, 1);
lean_inc_ref(x_4);
x_5 = lean_ctor_get(x_1, 0);
lean_inc_ref(x_5);
lean_dec_ref(x_1);
x_6 = !lean_is_exclusive(x_2);
if (x_6 == 0)
{
lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; uint8_t x_11; 
x_7 = lean_ctor_get(x_2, 0);
x_8 = lean_ctor_get(x_2, 1);
lean_dec(x_8);
x_9 = lean_ctor_get(x_3, 0);
lean_inc(x_9);
x_10 = lean_ctor_get(x_3, 1);
lean_inc(x_10);
lean_dec_ref(x_3);
x_11 = !lean_is_exclusive(x_4);
if (x_11 == 0)
{
lean_object* x_12; lean_object* x_13; lean_object* x_14; lean_object* x_15; lean_object* x_16; lean_object* x_17; lean_object* x_18; lean_object* x_19; lean_object* x_20; lean_object* x_21; 
x_12 = lean_ctor_get(x_4, 0);
x_13 = lean_ctor_get(x_4, 1);
x_14 = lp_CyberAlchemy_ProtorealManifold_mul(x_5, x_7);
lean_inc(x_12);
lean_inc(x_9);
x_15 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_15, 0, x_9);
lean_closure_set(x_15, 1, x_12);
lean_inc(x_13);
lean_inc(x_10);
x_16 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_16, 0, x_10);
lean_closure_set(x_16, 1, x_13);
x_17 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_17, 0, x_16);
x_18 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_18, 0, x_15);
lean_closure_set(x_18, 1, x_17);
x_19 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_19, 0, x_9);
lean_closure_set(x_19, 1, x_13);
x_20 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_20, 0, x_10);
lean_closure_set(x_20, 1, x_12);
x_21 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_21, 0, x_19);
lean_closure_set(x_21, 1, x_20);
lean_ctor_set(x_4, 1, x_21);
lean_ctor_set(x_4, 0, x_18);
lean_ctor_set(x_2, 0, x_14);
return x_2;
}
else
{
lean_object* x_22; lean_object* x_23; lean_object* x_24; lean_object* x_25; lean_object* x_26; lean_object* x_27; lean_object* x_28; lean_object* x_29; lean_object* x_30; lean_object* x_31; lean_object* x_32; 
x_22 = lean_ctor_get(x_4, 0);
x_23 = lean_ctor_get(x_4, 1);
lean_inc(x_23);
lean_inc(x_22);
lean_dec(x_4);
x_24 = lp_CyberAlchemy_ProtorealManifold_mul(x_5, x_7);
lean_inc(x_22);
lean_inc(x_9);
x_25 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_25, 0, x_9);
lean_closure_set(x_25, 1, x_22);
lean_inc(x_23);
lean_inc(x_10);
x_26 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_26, 0, x_10);
lean_closure_set(x_26, 1, x_23);
x_27 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_27, 0, x_26);
x_28 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_28, 0, x_25);
lean_closure_set(x_28, 1, x_27);
x_29 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_29, 0, x_9);
lean_closure_set(x_29, 1, x_23);
x_30 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_30, 0, x_10);
lean_closure_set(x_30, 1, x_22);
x_31 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_31, 0, x_29);
lean_closure_set(x_31, 1, x_30);
x_32 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_32, 0, x_28);
lean_ctor_set(x_32, 1, x_31);
lean_ctor_set(x_2, 1, x_32);
lean_ctor_set(x_2, 0, x_24);
return x_2;
}
}
else
{
lean_object* x_33; lean_object* x_34; lean_object* x_35; lean_object* x_36; lean_object* x_37; lean_object* x_38; lean_object* x_39; lean_object* x_40; lean_object* x_41; lean_object* x_42; lean_object* x_43; lean_object* x_44; lean_object* x_45; lean_object* x_46; lean_object* x_47; lean_object* x_48; 
x_33 = lean_ctor_get(x_2, 0);
lean_inc(x_33);
lean_dec(x_2);
x_34 = lean_ctor_get(x_3, 0);
lean_inc(x_34);
x_35 = lean_ctor_get(x_3, 1);
lean_inc(x_35);
lean_dec_ref(x_3);
x_36 = lean_ctor_get(x_4, 0);
lean_inc(x_36);
x_37 = lean_ctor_get(x_4, 1);
lean_inc(x_37);
if (lean_is_exclusive(x_4)) {
 lean_ctor_release(x_4, 0);
 lean_ctor_release(x_4, 1);
 x_38 = x_4;
} else {
 lean_dec_ref(x_4);
 x_38 = lean_box(0);
}
x_39 = lp_CyberAlchemy_ProtorealManifold_mul(x_5, x_33);
lean_inc(x_36);
lean_inc(x_34);
x_40 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_40, 0, x_34);
lean_closure_set(x_40, 1, x_36);
lean_inc(x_37);
lean_inc(x_35);
x_41 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_41, 0, x_35);
lean_closure_set(x_41, 1, x_37);
x_42 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_2451848184____hygCtx___hyg_8_), 2, 1);
lean_closure_set(x_42, 0, x_41);
x_43 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_43, 0, x_40);
lean_closure_set(x_43, 1, x_42);
x_44 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_44, 0, x_34);
lean_closure_set(x_44, 1, x_37);
x_45 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_4214226450____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_45, 0, x_35);
lean_closure_set(x_45, 1, x_36);
x_46 = lean_alloc_closure((void*)(lp_mathlib_Real_definition___lam__0_00___x40_Mathlib_Data_Real_Basic_1138242547____hygCtx___hyg_8_), 3, 2);
lean_closure_set(x_46, 0, x_44);
lean_closure_set(x_46, 1, x_45);
if (lean_is_scalar(x_38)) {
 x_47 = lean_alloc_ctor(0, 2, 0);
} else {
 x_47 = x_38;
}
lean_ctor_set(x_47, 0, x_43);
lean_ctor_set(x_47, 1, x_46);
x_48 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_48, 0, x_39);
lean_ctor_set(x_48, 1, x_47);
return x_48;
}
}
}
static lean_object* _init_lp_CyberAlchemy_instZeroKleinMesh___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; 
x_1 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
x_2 = lean_alloc_ctor(0, 5, 0);
lean_ctor_set(x_2, 0, x_1);
lean_ctor_set(x_2, 1, x_1);
lean_ctor_set(x_2, 2, x_1);
lean_ctor_set(x_2, 3, x_1);
lean_ctor_set(x_2, 4, x_1);
return x_2;
}
}
static lean_object* _init_lp_CyberAlchemy_instZeroKleinMesh___closed__1(void) {
_start:
{
lean_object* x_1; lean_object* x_2; 
x_1 = lp_mathlib_Real_definition_00___x40_Mathlib_Data_Real_Basic_1850581184____hygCtx___hyg_8_;
x_2 = lp_mathlib_Complex_ofReal(x_1);
return x_2;
}
}
static lean_object* _init_lp_CyberAlchemy_instZeroKleinMesh___closed__2(void) {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lean_obj_once(&lp_CyberAlchemy_instZeroKleinMesh___closed__1, &lp_CyberAlchemy_instZeroKleinMesh___closed__1_once, _init_lp_CyberAlchemy_instZeroKleinMesh___closed__1);
x_2 = lean_obj_once(&lp_CyberAlchemy_instZeroKleinMesh___closed__0, &lp_CyberAlchemy_instZeroKleinMesh___closed__0_once, _init_lp_CyberAlchemy_instZeroKleinMesh___closed__0);
x_3 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_3, 0, x_2);
lean_ctor_set(x_3, 1, x_1);
return x_3;
}
}
static lean_object* _init_lp_CyberAlchemy_instZeroKleinMesh(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_obj_once(&lp_CyberAlchemy_instZeroKleinMesh___closed__2, &lp_CyberAlchemy_instZeroKleinMesh___closed__2_once, _init_lp_CyberAlchemy_instZeroKleinMesh___closed__2);
return x_1;
}
}
static lean_object* _init_lp_CyberAlchemy_instProtorealAlgebraKleinMesh___closed__0(void) {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; lean_object* x_4; 
x_1 = lp_CyberAlchemy_instZeroKleinMesh;
x_2 = ((lean_object*)(lp_CyberAlchemy_instMulKleinMesh___closed__0));
x_3 = ((lean_object*)(lp_CyberAlchemy_instAddKleinMesh___closed__0));
x_4 = lean_alloc_ctor(0, 3, 0);
lean_ctor_set(x_4, 0, x_3);
lean_ctor_set(x_4, 1, x_2);
lean_ctor_set(x_4, 2, x_1);
return x_4;
}
}
static lean_object* _init_lp_CyberAlchemy_instProtorealAlgebraKleinMesh(void) {
_start:
{
lean_object* x_1; 
x_1 = lean_obj_once(&lp_CyberAlchemy_instProtorealAlgebraKleinMesh___closed__0, &lp_CyberAlchemy_instProtorealAlgebraKleinMesh___closed__0_once, _init_lp_CyberAlchemy_instProtorealAlgebraKleinMesh___closed__0);
return x_1;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(uint8_t builtin);
lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealMesh(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_CyberAlchemy_CyberAlchemy_ProtorealAlgebra(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealManifold(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_CyberAlchemy_CyberAlchemy_ProtorealMesh(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_CyberAlchemy_instZeroKleinMesh = _init_lp_CyberAlchemy_instZeroKleinMesh();
lean_mark_persistent(lp_CyberAlchemy_instZeroKleinMesh);
lp_CyberAlchemy_instProtorealAlgebraKleinMesh = _init_lp_CyberAlchemy_instProtorealAlgebraKleinMesh();
lean_mark_persistent(lp_CyberAlchemy_instProtorealAlgebraKleinMesh);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
