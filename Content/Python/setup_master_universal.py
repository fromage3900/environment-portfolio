"""Build M_Master_Toon_Universal — the 'reach for every scene' master.

Hybrid texture/procedural, triplanar, Nikki dreamy glow, constellation ramps,
curvature gold leaf, fairy-dust highlight motifs, dreamy shadow tinting,
shadow-garden flowers, and metallic ORM blend — all defaulting to neutral (0).

Run (editor open):
  py "G:/EnvironmentPortfolio/BS_GodFile/Content/Python/setup_master_universal.py"

Then instances:
  py "G:/EnvironmentPortfolio/BS_GodFile/Content/Python/setup_universal_instances.py"
"""
from __future__ import annotations

import unreal
import material_lib as lib

MASTER_NAME = "M_Master_Toon_Universal"
WAT = "/Engine/Functions/Engine_MaterialFunctions02/Texturing/WorldAlignedTexture"
WAN = "/Engine/Functions/Engine_MaterialFunctions02/Texturing/WorldAlignedNormal"

WIRES: dict[str, bool] = {}


def wire(tag, from_e, to_e, *pins) -> bool:
    for p in pins:
        if from_e is not None and lib.connect(from_e, "", to_e, p):
            WIRES[tag] = True
            return True
    WIRES[tag] = False
    return False


def const1(m, x, y, val: float = 1.0):
    c = lib.create_expression(m, unreal.MaterialExpressionConstant, x, y)
    c.set_editor_property("r", val)
    return c


def tex_object(m, name, x, y, group: str = "Textures"):
    e = lib.create_expression(m, unreal.MaterialExpressionTextureObjectParameter, x, y)
    e.set_editor_property("parameter_name", name)
    e.set_editor_property("group", group)
    return e


def mf_call(m, path, x, y):
    if not unreal.EditorAssetLibrary.does_asset_exist(path):
        return None
    c = lib.create_expression(m, unreal.MaterialExpressionMaterialFunctionCall, x, y)
    c.set_editor_property("material_function", unreal.load_asset(path))
    return c


def static_switch(m, name, group, x, y, default=False):
    sw = lib.create_expression(m, unreal.MaterialExpressionStaticSwitchParameter, x, y)
    sw.set_editor_property("parameter_name", name)
    sw.set_editor_property("group", group)
    sw.set_editor_property("default_value", default)
    return sw


def world_xy(m, x, y):
    wp = lib.create_expression(m, unreal.MaterialExpressionWorldPosition, x, y)
    mask = lib.create_expression(m, unreal.MaterialExpressionComponentMask, x + 160, y)
    mask.set_editor_property("r", True)
    mask.set_editor_property("g", True)
    mask.set_editor_property("b", False)
    mask.set_editor_property("a", False)
    wire("wxy_wp", wp, mask, "")
    return mask


def style_peak(m, style, target: float, tag: str, x, y):
    """Weight ~1 when style scalar equals target, ~0 elsewhere."""
    tgt = const1(m, x, y, target)
    sub = lib.create_expression(m, unreal.MaterialExpressionSubtract, x + 120, y)
    wire(f"{tag}_subA", style, sub, "A")
    wire(f"{tag}_subB", tgt, sub, "B")
    ab = lib.create_expression(m, unreal.MaterialExpressionAbs, x + 260, y)
    wire(f"{tag}_abs", sub, ab, "Input")
    scale = const1(m, x + 120, y + 80, 2.0)
    sc = lib.create_expression(m, unreal.MaterialExpressionMultiply, x + 400, y)
    wire(f"{tag}_scA", ab, sc, "A")
    wire(f"{tag}_scB", scale, sc, "B")
    inv = lib.create_expression(m, unreal.MaterialExpressionOneMinus, x + 540, y)
    wire(f"{tag}_inv", sc, inv, "Input")
    return inv


def build():
    lib.ensure_directory(lib.MASTER_DIR)
    path = lib.asset_path(lib.MASTER_DIR, MASTER_NAME)
    if unreal.EditorAssetLibrary.does_asset_exist(path):
        unreal.EditorAssetLibrary.delete_asset(path)

    at = unreal.AssetToolsHelpers.get_asset_tools()
    m = at.create_asset(MASTER_NAME, lib.MASTER_DIR, unreal.Material, unreal.MaterialFactoryNew())
    if not m:
        raise RuntimeError("create_asset failed")
    m.set_editor_property("material_domain", unreal.MaterialDomain.MD_SURFACE)
    m.set_editor_property("blend_mode", unreal.BlendMode.BLEND_OPAQUE)
    lib.try_set_editor_property(m, "bUsesSubstrate", True)

    # ---- core parameters ----
    base_tint = lib.vector_param(m, "BaseTint", "Palette", (0.60, 0.55, 0.50, 1.0), -2100, -220)
    tex_weight = lib.scalar_param(m, "TextureWeight", "Hybrid", 1.0, -2100, -100)
    uv_scale = lib.scalar_param(m, "UVScale", "UV", 1.0, -2100, 20)
    roughness_s = lib.scalar_param(m, "Roughness", "Surface", 0.70, -2100, 140)
    metallic_s = lib.scalar_param(m, "Metallic", "Surface", 0.0, -2100, 240)
    tri_tiling = lib.scalar_param(m, "TriplanarTiling", "Triplanar", 256.0, -2100, 340)
    albedo = tex_object(m, "Albedo", -2100, 480)
    normal = tex_object(m, "NormalMap", -2100, 640)
    orm = tex_object(m, "ORM", -2100, 800)

    # ---- UV ----
    tc = lib.create_expression(m, unreal.MaterialExpressionTextureCoordinate, -1800, 460)
    uv = lib.create_expression(m, unreal.MaterialExpressionMultiply, -1620, 460)
    wire("uv_tc", tc, uv, "A")
    wire("uv_scale", uv_scale, uv, "B")

    def uv_sample(tag, tobj, yy):
        s = lib.create_expression(m, unreal.MaterialExpressionTextureSample, -1420, yy)
        wire(f"{tag}_obj", tobj, s, "Tex", "TextureObject")
        wire(f"{tag}_uv", uv, s, "UVs", "Coordinates")
        return s

    alb_uv = uv_sample("alb", albedo, 480)
    nrm_uv = uv_sample("nrm", normal, 640)
    orm_uv = uv_sample("orm", orm, 800)

    waT = mf_call(m, WAT, -1240, 480)
    waN = mf_call(m, WAN, -1240, 640)
    waR = mf_call(m, WAT, -1240, 800)
    for tag, fn, tobj in (("triA", waT, albedo), ("triN", waN, normal), ("triR", waR, orm)):
        if fn:
            wire(f"{tag}_obj", tobj, fn, "TextureObject (T2d)", "TextureObject", "Tex")
            wire(f"{tag}_size", tri_tiling, fn, "Texture Size", "WorldSize", "Size")

    def tri_switch(tag, uv_e, tri_e, yy):
        sw = static_switch(m, "bTriplanar", "Triplanar", -1060, yy)
        wire(f"{tag}_true", tri_e or uv_e, sw, "A", "True")
        wire(f"{tag}_false", uv_e, sw, "B", "False")
        return sw

    alb = tri_switch("swA", alb_uv, waT, 480)
    nrm_s = tri_switch("swN", nrm_uv, waN, 640)
    orm_s = tri_switch("swR", orm_uv, waR, 800)

    # hybrid base color / roughness / normal / metallic
    color = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, -200, 120)
    wire("color_A", base_tint, color, "A")
    wire("color_B", alb, color, "B")
    wire("color_alpha", tex_weight, color, "Alpha")

    org = lib.create_expression(m, unreal.MaterialExpressionComponentMask, -200, 800)
    org.set_editor_property("r", False)
    org.set_editor_property("g", True)
    org.set_editor_property("b", False)
    org.set_editor_property("a", False)
    lib.connect_unary(orm_s, org)
    rough = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 20, 800)
    wire("rough_A", roughness_s, rough, "A")
    wire("rough_B", org, rough, "B")
    wire("rough_alpha", tex_weight, rough, "Alpha")

    orm_r = lib.create_expression(m, unreal.MaterialExpressionComponentMask, -200, 960)
    orm_r.set_editor_property("r", True)
    orm_r.set_editor_property("g", False)
    orm_r.set_editor_property("b", False)
    orm_r.set_editor_property("a", False)
    lib.connect_unary(orm_s, orm_r)
    metal = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 20, 960)
    wire("metal_A", metallic_s, metal, "A")
    wire("metal_B", orm_r, metal, "B")
    wire("metal_alpha", tex_weight, metal, "Alpha")

    flat_n = lib.create_expression(m, unreal.MaterialExpressionConstant3Vector, -200, 640)
    flat_n.set_editor_property("constant", unreal.LinearColor(0.0, 0.0, 1.0, 1.0))
    nrm = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 20, 640)
    wire("nrm_A", flat_n, nrm, "A")
    wire("nrm_B", nrm_s, nrm, "B")
    wire("nrm_alpha", tex_weight, nrm, "Alpha")

    # ---- Nikki dreamy layer ----
    rim_color = lib.vector_param(m, "RimColor", "Nikki", (0.70, 0.85, 1.00, 1.0), -2100, 1040)
    rim_power = lib.scalar_param(m, "RimPower", "Nikki", 3.0, -2100, 1140)
    rim_int = lib.scalar_param(m, "RimIntensity", "Nikki", 0.0, -2100, 1240)
    dream_tint = lib.vector_param(m, "DreamTint", "Nikki", (1.00, 0.85, 0.92, 1.0), -2100, 1340)
    pastel = lib.scalar_param(m, "PastelLift", "Nikki", 0.0, -2100, 1440)
    irid = lib.scalar_param(m, "Iridescence", "Nikki", 0.0, -2100, 1540)
    irid_tint = lib.vector_param(m, "IridescenceTint", "Nikki", (0.80, 0.60, 1.00, 1.0), -2100, 1640)
    spark_mask = lib.texture_param(m, "SparkleMask", "Nikki", -2100, 1740)
    spark_scale = lib.scalar_param(m, "SparkleScale", "Nikki", 8.0, -2100, 1840)
    spark_int = lib.scalar_param(m, "SparkleIntensity", "Nikki", 0.0, -2100, 1940)
    spark_color = lib.vector_param(m, "SparkleColor", "Nikki", (1.00, 0.95, 0.80, 1.0), -2100, 2040)
    glow_color = lib.vector_param(m, "GlowColor", "Nikki", (1.00, 0.90, 0.95, 1.0), -2100, 2140)
    glow_int = lib.scalar_param(m, "GlowIntensity", "Nikki", 0.0, -2100, 2240)
    rim_soft = lib.scalar_param(m, "RimSoftness", "Nikki", 0.35, -2100, 2340)
    inner_glow = lib.scalar_param(m, "InnerGlowIntensity", "Nikki", 0.0, -2100, 2440)
    inner_color = lib.vector_param(m, "InnerGlowColor", "Nikki", (1.00, 0.92, 0.98, 1.0), -2100, 2540)
    bloom = lib.scalar_param(m, "BloomBoost", "Nikki", 0.0, -2100, 2640)
    sheen = lib.scalar_param(m, "FabricSheen", "Nikki", 0.0, -2100, 2740)
    sheen_tint = lib.vector_param(m, "SheenTint", "Nikki", (1.00, 1.00, 1.00, 1.0), -2100, 2840)
    sheen_power = lib.scalar_param(m, "SheenPower", "Nikki", 6.0, -2100, 2940)

    # ---- Constellation ramps ----
    const_low = lib.vector_param(m, "ConstellationRampLow", "Constellation", (0.10, 0.12, 0.28, 1.0), -2100, 3060)
    const_mid = lib.vector_param(m, "ConstellationRampMid", "Constellation", (0.40, 0.62, 0.95, 1.0), -2100, 3160)
    const_high = lib.vector_param(m, "ConstellationRampHigh", "Constellation", (0.95, 0.88, 1.00, 1.0), -2100, 3260)
    const_str = lib.scalar_param(m, "ConstellationStrength", "Constellation", 0.0, -2100, 3360)
    const_scale = lib.scalar_param(m, "ConstellationScale", "Constellation", 1.8, -2100, 3460)
    const_phase = lib.scalar_param(m, "ConstellationPhase", "Constellation", 0.0, -2100, 3560)

    # ---- Gold leaf on curvature ----
    gild_str = lib.scalar_param(m, "GildingStrength", "Gilding", 0.0, -2100, 3680)
    gold_tint = lib.vector_param(m, "GoldTint", "Gilding", (0.92, 0.72, 0.28, 1.0), -2100, 3780)
    gold_rough = lib.scalar_param(m, "GoldRoughness", "Gilding", 0.18, -2100, 3880)
    gold_emis = lib.vector_param(m, "GoldEmissive", "Gilding", (0.35, 0.25, 0.05, 1.0), -2100, 3980)
    curve_sens = lib.scalar_param(m, "CurvatureSensitivity", "Gilding", 2.5, -2100, 4080)

    # ---- Dreamy shadows + shadow garden ----
    shadow_tint = lib.vector_param(m, "ShadowDreamTint", "ShadowDream", (0.48, 0.42, 0.62, 1.0), -2100, 4200)
    shadow_str = lib.scalar_param(m, "ShadowDreamStrength", "ShadowDream", 0.0, -2100, 4300)
    shadow_soft = lib.scalar_param(m, "ShadowSoftness", "ShadowDream", 0.5, -2100, 4400)
    flower_str = lib.scalar_param(m, "ShadowFlowerStrength", "ShadowGarden", 0.0, -2100, 4520)
    flower_scale = lib.scalar_param(m, "ShadowFlowerScale", "ShadowGarden", 5.0, -2100, 4620)
    flower_color = lib.vector_param(m, "ShadowFlowerColor", "ShadowGarden", (0.92, 0.45, 0.72, 1.0), -2100, 4720)

    # ---- Fairy dust motifs (0=off, 1=heart, 2=star, 3=flower, 4=moon) ----
    fairy_style = lib.scalar_param(m, "FairyMotifStyle", "FairyDust", 0.0, -2100, 4840)
    fairy_int = lib.scalar_param(m, "FairyDustIntensity", "FairyDust", 0.0, -2100, 4940)
    fairy_scale = lib.scalar_param(m, "FairyDustScale", "FairyDust", 14.0, -2100, 5040)
    fairy_color = lib.vector_param(m, "FairyDustColor", "FairyDust", (1.0, 0.92, 0.98, 1.0), -2100, 5140)
    fairy_thresh = lib.scalar_param(m, "FairyHighlightThreshold", "FairyDust", 0.35, -2100, 5240)
    fairy_glyph = lib.texture_param(m, "FairyGlyphMask", "FairyDust", -2100, 5340)

    color_nikki = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 220, 120)
    wire("nikki_base_A", color, color_nikki, "A")
    wire("nikki_base_B", dream_tint, color_nikki, "B")
    wire("nikki_base_alpha", pastel, color_nikki, "Alpha")

    # constellation star field
    wxy = world_xy(m, 220, 300)
    const_mul = lib.create_expression(m, unreal.MaterialExpressionMultiply, 400, 300)
    wire("const_mulA", wxy, const_mul, "A")
    wire("const_mulB", const_scale, const_mul, "B")
    phase_add = lib.create_expression(m, unreal.MaterialExpressionAdd, 560, 300)
    wire("phase_A", const_mul, phase_add, "A")
    wire("phase_B", const_phase, phase_add, "B")
    frac_n = lib.create_expression(m, unreal.MaterialExpressionFrac, 720, 300)
    wire("frac_in", phase_add, frac_n, "Input")
    star_dist = lib.create_expression(m, unreal.MaterialExpressionDistance, 900, 300)
    star_ctr = lib.create_expression(m, unreal.MaterialExpressionConstant2Vector, 720, 420)
    star_ctr.set_editor_property("r", 0.5)
    star_ctr.set_editor_property("g", 0.5)
    wire("dist_A", frac_n, star_dist, "A")
    wire("dist_B", star_ctr, star_dist, "B")
    star_inv = lib.create_expression(m, unreal.MaterialExpressionOneMinus, 1080, 300)
    wire("star_inv", star_dist, star_inv, "Input")
    star_pow = lib.create_expression(m, unreal.MaterialExpressionPower, 1240, 300)
    wire("star_powA", star_inv, star_pow, "Base")
    two = const1(m, 1080, 420, 2.0)
    wire("star_powB", two, star_pow, "Exp")
    ramp_a = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 1420, 260)
    wire("ramp_aA", const_low, ramp_a, "A")
    wire("ramp_aB", const_mid, ramp_a, "B")
    wire("ramp_a_alpha", star_pow, ramp_a, "Alpha")
    ramp_b = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 1600, 260)
    wire("ramp_bA", ramp_a, ramp_b, "A")
    wire("ramp_bB", const_high, ramp_b, "B")
    wire("ramp_b_alpha", star_pow, ramp_b, "Alpha")
    color_stars = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 1780, 120)
    wire("stars_A", color_nikki, color_stars, "A")
    wire("stars_B", ramp_b, color_stars, "B")
    wire("stars_alpha", const_str, color_stars, "Alpha")

    # curvature gold leaf
    pnormal = lib.create_expression(m, unreal.MaterialExpressionPixelNormalWS, 220, 520)
    ddx = lib.create_expression(m, unreal.MaterialExpressionDDX, 400, 460)
    ddy = lib.create_expression(m, unreal.MaterialExpressionDDY, 400, 580)
    wire("ddx_n", pnormal, ddx, "Input")
    wire("ddy_n", pnormal, ddy, "Input")
    curve_sum = lib.create_expression(m, unreal.MaterialExpressionAdd, 560, 520)
    wire("curve_A", ddx, curve_sum, "A")
    wire("curve_B", ddy, curve_sum, "B")
    curve_abs = lib.create_expression(m, unreal.MaterialExpressionAbs, 720, 520)
    wire("curve_abs", curve_sum, curve_abs, "Input")
    curve_mul = lib.create_expression(m, unreal.MaterialExpressionMultiply, 880, 520)
    wire("curve_mulA", curve_abs, curve_mul, "A")
    wire("curve_mulB", curve_sens, curve_mul, "B")
    gold_mask = lib.create_expression(m, unreal.MaterialExpressionMultiply, 1040, 520)
    wire("gold_maskA", curve_mul, gold_mask, "A")
    wire("gold_maskB", gild_str, gold_mask, "B")
    color_gold = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 1220, 120)
    wire("gold_cA", color_stars, color_gold, "A")
    wire("gold_cB", gold_tint, color_gold, "B")
    wire("gold_c_alpha", gold_mask, color_gold, "Alpha")
    rough_gold = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 1220, 800)
    wire("gold_rA", rough, rough_gold, "A")
    wire("gold_rB", gold_rough, rough_gold, "B")
    wire("gold_r_alpha", gold_mask, rough_gold, "Alpha")
    metal_gold = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 1220, 960)
    wire("gold_mA", metal, metal_gold, "A")
    one_m = const1(m, 1040, 1080, 1.0)
    wire("gold_mB", one_m, metal_gold, "B")
    wire("gold_m_alpha", gold_mask, metal_gold, "Alpha")
    gold_emis_m = lib.create_expression(m, unreal.MaterialExpressionMultiply, 1220, 640)
    wire("gold_eA", gold_mask, gold_emis_m, "A")
    wire("gold_eB", gold_emis, gold_emis_m, "B")

    # dreamy shadow tint (N·L proxy)
    light_dir = lib.create_expression(m, unreal.MaterialExpressionConstant3Vector, 220, 760)
    light_dir.set_editor_property("constant", unreal.LinearColor(0.35, 0.55, 0.85, 1.0))
    ndotl = lib.create_expression(m, unreal.MaterialExpressionDotProduct, 400, 760)
    wire("ndotl_A", pnormal, ndotl, "A")
    wire("ndotl_B", light_dir, ndotl, "B")
    shadow_raw = lib.create_expression(m, unreal.MaterialExpressionOneMinus, 560, 760)
    wire("shadow_raw", ndotl, shadow_raw, "Input")
    soft_exp = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 720, 860)
    wire("soft_A", const1(m, 560, 900, 1.0), soft_exp, "A")
    wire("soft_B", const1(m, 560, 980, 4.0), soft_exp, "B")
    wire("soft_alpha", shadow_soft, soft_exp, "Alpha")
    shadow_pow = lib.create_expression(m, unreal.MaterialExpressionPower, 880, 760)
    wire("shadow_powA", shadow_raw, shadow_pow, "Base")
    wire("shadow_powB", soft_exp, shadow_pow, "Exp")
    shadow_amt = lib.create_expression(m, unreal.MaterialExpressionMultiply, 1040, 760)
    wire("shadow_amtA", shadow_pow, shadow_amt, "A")
    wire("shadow_amtB", shadow_str, shadow_amt, "B")
    final_color = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 1420, 120)
    wire("dream_A", color_gold, final_color, "A")
    wire("dream_B", shadow_tint, final_color, "B")
    wire("dream_alpha", shadow_amt, final_color, "Alpha")

    # shadow garden flowers (world clover in shadow)
    flower_uv = lib.create_expression(m, unreal.MaterialExpressionMultiply, 1220, 900)
    wire("fl_uvA", wxy, flower_uv, "A")
    wire("fl_uvB", flower_scale, flower_uv, "B")
    petal_x = lib.create_expression(m, unreal.MaterialExpressionSine, 1400, 860)
    petal_x.set_editor_property("period", 1.0)
    wire("petal_x", flower_uv, petal_x, "Input")
    petal_y = lib.create_expression(m, unreal.MaterialExpressionSine, 1400, 980)
    petal_y.set_editor_property("period", 1.0)
    flower_uv2 = lib.create_expression(m, unreal.MaterialExpressionMultiply, 1400, 920)
    wire("fl2A", flower_uv, flower_uv2, "A")
    const_swap = const1(m, 1220, 1040, 0.7)
    wire("fl2B", const_swap, flower_uv2, "B")
    wire("petal_y_in", flower_uv2, petal_y, "Input")
    petal = lib.create_expression(m, unreal.MaterialExpressionMultiply, 1580, 920)
    wire("petalA", petal_x, petal, "A")
    wire("petalB", petal_y, petal, "B")
    petal_abs = lib.create_expression(m, unreal.MaterialExpressionAbs, 1740, 920)
    wire("petal_abs", petal, petal_abs, "Input")
    flower_mask = lib.create_expression(m, unreal.MaterialExpressionMultiply, 1900, 900)
    wire("fl_maskA", shadow_amt, flower_mask, "A")
    wire("fl_maskB", petal_abs, flower_mask, "B")
    flower_w = lib.create_expression(m, unreal.MaterialExpressionMultiply, 2060, 900)
    wire("fl_wA", flower_mask, flower_w, "A")
    wire("fl_wB", flower_str, flower_w, "B")
    flower_e = lib.create_expression(m, unreal.MaterialExpressionMultiply, 2220, 900)
    wire("fl_eA", flower_w, flower_e, "A")
    wire("fl_eB", flower_color, flower_e, "B")

    # fresnel + Nikki emissive stack
    fres = lib.create_expression(m, unreal.MaterialExpressionFresnel, 220, 1100)
    wire("fresnel_exp", rim_power, fres, "ExponentIn")
    rim_soft_m = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 220, 1180)
    wire("rim_soft_A", fres, rim_soft_m, "A")
    rim_inv = lib.create_expression(m, unreal.MaterialExpressionOneMinus, 60, 1240)
    wire("rim_soft_inv", rim_soft, rim_inv, "Input")
    rim_soft_b = lib.create_expression(m, unreal.MaterialExpressionMultiply, 60, 1300)
    wire("rim_soft_bA", fres, rim_soft_b, "A")
    wire("rim_soft_bB", rim_inv, rim_soft_b, "B")
    wire("rim_soft_alpha", rim_soft, rim_soft_m, "Alpha")
    wire("rim_soft_B", rim_soft_b, rim_soft_m, "B")
    rim_m = lib.create_expression(m, unreal.MaterialExpressionMultiply, 400, 1100)
    wire("rim_mA", rim_soft_m, rim_m, "A")
    wire("rim_mB", rim_int, rim_m, "B")
    rim_e = lib.create_expression(m, unreal.MaterialExpressionMultiply, 580, 1100)
    wire("rim_eA", rim_m, rim_e, "A")
    wire("rim_eB", rim_color, rim_e, "B")
    irid_m = lib.create_expression(m, unreal.MaterialExpressionMultiply, 400, 1280)
    wire("irid_mA", rim_soft_m, irid_m, "A")
    wire("irid_mB", irid, irid_m, "B")
    irid_e = lib.create_expression(m, unreal.MaterialExpressionMultiply, 580, 1280)
    wire("irid_eA", irid_m, irid_e, "A")
    wire("irid_eB", irid_tint, irid_e, "B")

    spark_uv = lib.create_expression(m, unreal.MaterialExpressionMultiply, 220, 1420)
    wire("spark_uvA", uv, spark_uv, "A")
    wire("spark_uvB", spark_scale, spark_uv, "B")
    wire("spark_mask_uv", spark_uv, spark_mask, "UVs", "Coordinates")
    spark_m = lib.create_expression(m, unreal.MaterialExpressionMultiply, 400, 1420)
    wire("spark_mA", spark_mask, spark_m, "A")
    wire("spark_mB", spark_int, spark_m, "B")
    spark_e = lib.create_expression(m, unreal.MaterialExpressionMultiply, 580, 1420)
    wire("spark_eA", spark_m, spark_e, "A")
    wire("spark_eB", spark_color, spark_e, "B")

    glow_e = lib.create_expression(m, unreal.MaterialExpressionMultiply, 400, 1580)
    wire("glow_eA", glow_color, glow_e, "A")
    wire("glow_eB", glow_int, glow_e, "B")

    inner_inv = lib.create_expression(m, unreal.MaterialExpressionOneMinus, 220, 1280)
    wire("inner_inv", rim_soft_m, inner_inv, "Input")
    inner_m = lib.create_expression(m, unreal.MaterialExpressionMultiply, 400, 1360)
    wire("inner_mA", inner_inv, inner_m, "A")
    wire("inner_mB", inner_glow, inner_m, "B")
    inner_e = lib.create_expression(m, unreal.MaterialExpressionMultiply, 580, 1360)
    wire("inner_eA", inner_m, inner_e, "A")
    wire("inner_eB", inner_color, inner_e, "B")

    sheen_f = lib.create_expression(m, unreal.MaterialExpressionFresnel, 220, 1520)
    wire("sheen_exp", sheen_power, sheen_f, "ExponentIn")
    sheen_m = lib.create_expression(m, unreal.MaterialExpressionMultiply, 400, 1520)
    wire("sheen_mA", sheen_f, sheen_m, "A")
    wire("sheen_mB", sheen, sheen_m, "B")
    sheen_e = lib.create_expression(m, unreal.MaterialExpressionMultiply, 580, 1520)
    wire("sheen_eA", sheen_m, sheen_e, "A")
    wire("sheen_eB", sheen_tint, sheen_e, "B")

    # fairy dust procedural motifs on world UV
    fairy_uv = lib.create_expression(m, unreal.MaterialExpressionMultiply, 220, 1680)
    wire("fairy_uvA", wxy, fairy_uv, "A")
    wire("fairy_uvB", fairy_scale, fairy_uv, "B")
    # heart: pinched radial
    heart_r = lib.create_expression(m, unreal.MaterialExpressionDistance, 400, 1640)
    heart_c = lib.create_expression(m, unreal.MaterialExpressionConstant2Vector, 220, 1780)
    heart_c.set_editor_property("r", 0.5)
    heart_c.set_editor_property("g", 0.42)
    wire("heart_distA", fairy_uv, heart_r, "A")
    wire("heart_distB", heart_c, heart_r, "B")
    heart_inv = lib.create_expression(m, unreal.MaterialExpressionOneMinus, 560, 1640)
    wire("heart_inv", heart_r, heart_inv, "Input")
    # star: high-frequency sine grid
    star_sx = lib.create_expression(m, unreal.MaterialExpressionSine, 400, 1760)
    star_sx.set_editor_property("period", 5.0)
    wire("star_sx", fairy_uv, star_sx, "Input")
    star_sy = lib.create_expression(m, unreal.MaterialExpressionSine, 400, 1880)
    star_sy.set_editor_property("period", 5.0)
    fairy_uv_y = lib.create_expression(m, unreal.MaterialExpressionComponentMask, 220, 1880)
    fairy_uv_y.set_editor_property("r", False)
    fairy_uv_y.set_editor_property("g", True)
    fairy_uv_y.set_editor_property("b", False)
    fairy_uv_y.set_editor_property("a", False)
    wire("fuv_y", fairy_uv, fairy_uv_y, "")
    wire("star_sy", fairy_uv_y, star_sy, "Input")
    star_m = lib.create_expression(m, unreal.MaterialExpressionMultiply, 560, 1820)
    wire("star_mA", star_sx, star_m, "A")
    wire("star_mB", star_sy, star_m, "B")
    star_abs = lib.create_expression(m, unreal.MaterialExpressionAbs, 720, 1820)
    wire("star_abs", star_m, star_abs, "Input")
    # flower motif for fairy dust (separate from shadow-garden petals)
    fairy_px = lib.create_expression(m, unreal.MaterialExpressionSine, 400, 1960)
    fairy_px.set_editor_property("period", 1.0)
    wire("fairy_px", fairy_uv, fairy_px, "Input")
    fairy_py = lib.create_expression(m, unreal.MaterialExpressionSine, 400, 2080)
    fairy_py.set_editor_property("period", 1.0)
    fairy_uv_y2 = lib.create_expression(m, unreal.MaterialExpressionComponentMask, 220, 2080)
    fairy_uv_y2.set_editor_property("r", False)
    fairy_uv_y2.set_editor_property("g", True)
    fairy_uv_y2.set_editor_property("b", False)
    fairy_uv_y2.set_editor_property("a", False)
    wire("fuv_y2", fairy_uv, fairy_uv_y2, "")
    wire("fairy_py", fairy_uv_y2, fairy_py, "Input")
    flower_motif = lib.create_expression(m, unreal.MaterialExpressionMultiply, 560, 2020)
    wire("fl_mA", fairy_px, flower_motif, "A")
    wire("fl_mB", fairy_py, flower_motif, "B")
    flower_m_abs = lib.create_expression(m, unreal.MaterialExpressionAbs, 720, 1960)
    wire("fl_m_abs", flower_motif, flower_m_abs, "Input")
    # moon: crescent from two radii
    moon_r = lib.create_expression(m, unreal.MaterialExpressionDistance, 400, 2080)
    moon_c = lib.create_expression(m, unreal.MaterialExpressionConstant2Vector, 220, 2180)
    moon_c.set_editor_property("r", 0.45)
    moon_c.set_editor_property("g", 0.5)
    wire("moon_distA", fairy_uv, moon_r, "A")
    wire("moon_distB", moon_c, moon_r, "B")
    moon_sub = lib.create_expression(m, unreal.MaterialExpressionSubtract, 560, 2080)
    wire("moon_subA", const1(m, 400, 2180, 0.35), moon_sub, "A")
    wire("moon_subB", moon_r, moon_sub, "B")
    moon_clamp = lib.create_expression(m, unreal.MaterialExpressionSaturate, 720, 2080)
    wire("moon_sat", moon_sub, moon_clamp, "Input")

    w_heart = style_peak(m, fairy_style, 1.0, "wh", 860, 1640)
    w_star = style_peak(m, fairy_style, 2.0, "ws", 860, 1760)
    w_flower = style_peak(m, fairy_style, 3.0, "wf", 860, 1880)
    w_moon = style_peak(m, fairy_style, 4.0, "wm", 860, 2000)
    m_h = lib.create_expression(m, unreal.MaterialExpressionMultiply, 1040, 1640)
    wire("m_hA", heart_inv, m_h, "A")
    wire("m_hB", w_heart, m_h, "B")
    m_s = lib.create_expression(m, unreal.MaterialExpressionMultiply, 1040, 1760)
    wire("m_sA", star_abs, m_s, "A")
    wire("m_sB", w_star, m_s, "B")
    m_f = lib.create_expression(m, unreal.MaterialExpressionMultiply, 1040, 1880)
    wire("m_fA", flower_m_abs, m_f, "A")
    wire("m_fB", w_flower, m_f, "B")
    m_m = lib.create_expression(m, unreal.MaterialExpressionMultiply, 1040, 2000)
    wire("m_mA", moon_clamp, m_m, "A")
    wire("m_mB", w_moon, m_m, "B")
    motif_a = lib.create_expression(m, unreal.MaterialExpressionAdd, 1220, 1720)
    wire("motif_aA", m_h, motif_a, "A")
    wire("motif_aB", m_s, motif_a, "B")
    motif_b = lib.create_expression(m, unreal.MaterialExpressionAdd, 1380, 1780)
    wire("motif_bA", motif_a, motif_b, "A")
    wire("motif_bB", m_f, motif_b, "B")
    motif = lib.create_expression(m, unreal.MaterialExpressionAdd, 1540, 1820)
    wire("motif_cA", motif_b, motif, "A")
    wire("motif_cB", m_m, motif, "B")
    # optional glyph texture overlay
    wire("glyph_uv", fairy_uv, fairy_glyph, "UVs", "Coordinates")
    motif_tex = lib.create_expression(m, unreal.MaterialExpressionAdd, 1700, 1820)
    wire("motif_texA", motif, motif_tex, "A")
    wire("motif_texB", fairy_glyph, motif_tex, "B")
    highlight = lib.create_expression(m, unreal.MaterialExpressionSubtract, 1220, 1580)
    wire("hl_A", rim_soft_m, highlight, "A")
    wire("hl_B", fairy_thresh, highlight, "B")
    highlight_sat = lib.create_expression(m, unreal.MaterialExpressionSaturate, 1380, 1580)
    wire("hl_sat", highlight, highlight_sat, "Input")
    fairy_m = lib.create_expression(m, unreal.MaterialExpressionMultiply, 1860, 1700)
    wire("fairy_mA", motif_tex, fairy_m, "A")
    wire("fairy_mB", highlight_sat, fairy_m, "B")
    fairy_w = lib.create_expression(m, unreal.MaterialExpressionMultiply, 2020, 1700)
    wire("fairy_wA", fairy_m, fairy_w, "A")
    wire("fairy_wB", fairy_int, fairy_w, "B")
    fairy_e = lib.create_expression(m, unreal.MaterialExpressionMultiply, 2180, 1700)
    wire("fairy_eA", fairy_w, fairy_e, "A")
    wire("fairy_eB", fairy_color, fairy_e, "B")

    # emissive sum + bloom
    a1 = lib.create_expression(m, unreal.MaterialExpressionAdd, 2400, 1200)
    wire("emi1A", rim_e, a1, "A")
    wire("emi1B", irid_e, a1, "B")
    a2 = lib.create_expression(m, unreal.MaterialExpressionAdd, 2560, 1280)
    wire("emi2A", a1, a2, "A")
    wire("emi2B", spark_e, a2, "B")
    a3 = lib.create_expression(m, unreal.MaterialExpressionAdd, 2720, 1360)
    wire("emi3A", a2, a3, "A")
    wire("emi3B", glow_e, a3, "B")
    a4 = lib.create_expression(m, unreal.MaterialExpressionAdd, 2880, 1440)
    wire("emi4A", a3, a4, "A")
    wire("emi4B", inner_e, a4, "B")
    a5 = lib.create_expression(m, unreal.MaterialExpressionAdd, 3040, 1520)
    wire("emi5A", a4, a5, "A")
    wire("emi5B", sheen_e, a5, "B")
    a6 = lib.create_expression(m, unreal.MaterialExpressionAdd, 3200, 1600)
    wire("emi6A", a5, a6, "A")
    wire("emi6B", gold_emis_m, a6, "B")
    a7 = lib.create_expression(m, unreal.MaterialExpressionAdd, 3360, 1680)
    wire("emi7A", a6, a7, "A")
    wire("emi7B", fairy_e, a7, "B")
    emissive_raw = lib.create_expression(m, unreal.MaterialExpressionAdd, 3520, 1760)
    wire("emi8A", a7, emissive_raw, "A")
    wire("emi8B", flower_e, emissive_raw, "B")
    bloom_m = lib.create_expression(m, unreal.MaterialExpressionAdd, 3680, 1760)
    wire("bloom_add_A", const1(m, 3520, 1860, 1.0), bloom_m, "A")
    wire("bloom_add_B", bloom, bloom_m, "B")
    emissive = lib.create_expression(m, unreal.MaterialExpressionMultiply, 3840, 1760)
    wire("bloom_mul_A", emissive_raw, emissive, "A")
    wire("bloom_mul_B", bloom_m, emissive, "B")

    profiles = lib.create_toon_profiles(["TP_Default", "TP_Gold"])
    toon = lib.create_expression(m, unreal.MaterialExpressionSubstrateToonBSDF, 4040, 480)
    lib.try_set_editor_property(toon, "toon_profile", profiles.get("TP_Default"))
    WIRES["toon_basecolor"] = lib.connect_toon_pin(toon, final_color, ("BaseColor", "DiffuseColor"))
    WIRES["toon_roughness"] = lib.connect_toon_pin(toon, rough_gold, ("Roughness",))
    WIRES["toon_normal"] = lib.connect_toon_pin(toon, nrm, ("Normal", "TangentNormal", "NormalMap"))
    WIRES["toon_metallic"] = lib.connect_toon_pin(toon, metal_gold, ("Metallic", "Metalness"))
    WIRES["toon_emissive"] = lib.connect_toon_pin(toon, emissive, ("Emissive Color", "EmissiveColor", "Emissive"))
    lib.connect_front_material(m, toon)

    unreal.MaterialEditingLibrary.recompile_material(m)
    lib.save_package(m)

    failed = sorted(k for k, v in WIRES.items() if not v)
    unreal.log(f"[Universal] built {path}")
    unreal.log(f"[Universal] wires ok={sum(WIRES.values())}/{len(WIRES)} | failed={failed}")
    print(f"UNIVERSAL_RESULT path={path} ok={sum(WIRES.values())}/{len(WIRES)} failed={failed}")

    try:
        import setup_universal_instances as inst
        inst.build_instances()
    except Exception as exc:
        unreal.log_warning(f"[Universal] instances: {exc}")

    return path


if __name__ == "__main__":
    build()
