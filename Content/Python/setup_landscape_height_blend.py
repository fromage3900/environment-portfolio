"""Build M_Master_Toon_Landscape_HeightBlend — toon landscape with height-map layer competition.

Run (editor):
  py "G:/EnvironmentPortfolio/BS_GodFile/Content/Python/setup_landscape_height_blend.py"

Headless:
  python Content/Python/setup_landscape_height_blend.py
"""
from __future__ import annotations

import os
import sys

MASTER_NAME = "M_Master_Toon_Landscape_HeightBlend"
INST_DIR = "/Game/EnvSandbox/Materials/Instances/Landscape"
WAT = "/Engine/Functions/Engine_MaterialFunctions02/Texturing/WorldAlignedTexture"
WAN = "/Engine/Functions/Engine_MaterialFunctions02/Texturing/WorldAlignedNormal"

INSTANCES = [
    {
        "name": "MI_Landscape_CliffGrass",
        "profile": "TP_Stone",
        "vectors": {"RockTint": (0.42, 0.40, 0.38, 1.0), "GrassTint": (0.32, 0.48, 0.22, 1.0), "MudTint": (0.28, 0.22, 0.16, 1.0)},
        "scalars": {"SlopeSharpness": 4.0, "HeightBlendStrength": 2.5, "GrassAmount": 0.65, "MudAmount": 0.25, "MacroStrength": 0.45, "TriplanarTiling": 280.0},
    },
    {
        "name": "MI_Landscape_Meadow",
        "profile": "TP_Foliage",
        "vectors": {"RockTint": (0.50, 0.46, 0.40, 1.0), "GrassTint": (0.38, 0.58, 0.24, 1.0), "MudTint": (0.34, 0.26, 0.18, 1.0)},
        "scalars": {"SlopeSharpness": 2.2, "HeightBlendStrength": 1.8, "GrassAmount": 0.85, "MudAmount": 0.15, "MacroStrength": 0.35, "TriplanarTiling": 220.0},
    },
    {
        "name": "MI_Landscape_SnowAlpine",
        "profile": "TP_Default",
        "vectors": {"RockTint": (0.38, 0.40, 0.44, 1.0), "GrassTint": (0.55, 0.58, 0.52, 1.0), "MudTint": (0.30, 0.28, 0.26, 1.0), "SnowTint": (0.92, 0.95, 0.98, 1.0)},
        "scalars": {"SlopeSharpness": 5.0, "HeightBlendStrength": 3.0, "GrassAmount": 0.35, "MudAmount": 0.10, "SnowStrength": 0.75, "SnowUpBias": 2.4, "TriplanarTiling": 320.0},
    },
]


def _layer_tex():
    import portfolio_texture_catalog as catalog

    return {
        "Rock": {
            "Albedo": catalog._chain(catalog.MARBLE["cool_stone"], catalog.MARBLE["dark"]),
            "Normal": catalog._normal_chain(),
            "Height": catalog._chain(catalog.HEIGHT["perlin"], catalog.COMPOSITING["crack_heavy"]),
        },
        "Grass": {
            "Albedo": catalog._chain(catalog.COMPOSITING["abstract_a"], catalog.MARBLE["warm_stone"]),
            "Normal": catalog._normal_chain(),
            "Height": catalog._chain(catalog.HEIGHT["perlin"], catalog.COMPOSITING["noise_fine"]),
        },
        "Mud": {
            "Albedo": catalog._chain(catalog.MARBLE["worn"], catalog.COMPOSITING["crack_overlay"]),
            "Normal": catalog._normal_chain(),
            "Height": catalog._chain(catalog.COMPOSITING["crack_overlay"], catalog.HEIGHT["perlin"]),
        },
    }


def build(*, force: bool = False) -> str:
    import unreal
    import material_lib as lib

    layer_tex = _layer_tex()

    def wire_tex(expr, candidates):
        path = lib.resolve_texture_path(candidates)
        if path:
            lib.set_expression_texture(expr, path)

    def mf_call(m, path, x, y):
        if not unreal.EditorAssetLibrary.does_asset_exist(path):
            return None
        c = lib.create_expression(m, unreal.MaterialExpressionMaterialFunctionCall, x, y)
        c.set_editor_property("material_function", unreal.load_asset(path))
        return c

    def sample_triplanar(m, tex_expr, tiling, tag, x, y):
        fn = WAN if "Nrm" in tag else WAT
        call = mf_call(m, fn, x, y)
        if not call:
            const = lib.create_expression(m, unreal.MaterialExpressionConstant3Vector, x + 200, y)
            const.set_editor_property("constant", unreal.LinearColor(0.5, 0.5, 0.5, 1.0))
            return const
        lib.connect(tex_expr, "Texture", call, "TextureObject")
        lib.connect(tiling, "", call, "TextureSize")
        return call

    lib.ensure_directory(lib.MASTER_DIR)
    lib.ensure_directory(INST_DIR)
    path = lib.asset_path(lib.MASTER_DIR, MASTER_NAME)
    exists = unreal.EditorAssetLibrary.does_asset_exist(path)
    force = force or os.environ.get("BS_MASTER_FORCE", "").lower() in ("1", "true", "yes")
    force = force or any("force" in str(a).lower() for a in sys.argv)
    if exists and not force:
        unreal.log_warning(f"[LandscapeHB] {path} exists — use --force")
        return path

    m = unreal.load_asset(path) if exists and force else None
    if m:
        lib.clear_material_graph(m)
    else:
        m = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            MASTER_NAME, lib.MASTER_DIR, unreal.Material, unreal.MaterialFactoryNew()
        )
    if not m:
        raise RuntimeError("create_asset failed")

    m.set_editor_property("material_domain", unreal.MaterialDomain.MD_SURFACE)
    m.set_editor_property("blend_mode", unreal.BlendMode.BLEND_OPAQUE)
    lib.try_set_editor_property(m, "bUsesSubstrate", True)
    lib.try_set_editor_property(m, "bUsedWithLandscape", True)
    lib.try_set_editor_property(m, "bUsedWithLandscapeGrass", True)

    profiles = lib.create_toon_profiles(["TP_Default", "TP_Stone", "TP_Foliage"])
    rock_tint = lib.vector_param(m, "RockTint", "Palette", (0.44, 0.41, 0.38, 1.0), -2200, -200)
    grass_tint = lib.vector_param(m, "GrassTint", "Palette", (0.30, 0.48, 0.20, 1.0), -2200, -80)
    mud_tint = lib.vector_param(m, "MudTint", "Palette", (0.28, 0.22, 0.16, 1.0), -2200, 40)
    snow_tint = lib.vector_param(m, "SnowTint", "Snow", (0.92, 0.95, 0.98, 1.0), -2200, 160)
    tri_tiling = lib.scalar_param(m, "TriplanarTiling", "Triplanar", 256.0, -2200, 300)
    slope_sharp = lib.scalar_param(m, "SlopeSharpness", "Blend", 3.0, -2200, 420)
    height_blend = lib.scalar_param(m, "HeightBlendStrength", "Blend", 2.0, -2200, 540)
    grass_amt = lib.scalar_param(m, "GrassAmount", "Blend", 0.6, -2200, 660)
    mud_amt = lib.scalar_param(m, "MudAmount", "Blend", 0.25, -2200, 780)
    macro_str = lib.scalar_param(m, "MacroStrength", "Macro", 0.4, -2200, 900)
    macro_scale = lib.scalar_param(m, "MacroScale", "Macro", 0.0004, -2200, 1020)
    snow_str = lib.scalar_param(m, "SnowStrength", "Snow", 0.0, -2200, 1140)
    snow_bias = lib.scalar_param(m, "SnowUpBias", "Snow", 2.2, -2200, 1260)
    roughness_s = lib.scalar_param(m, "Roughness", "Surface", 0.82, -2200, 1380)

    layer_samples: dict[str, dict] = {}
    for i, (layer, tex) in enumerate(layer_tex.items()):
        yy = 400 + i * 420
        alb = lib.texture_param(m, f"{layer}_Albedo", "Textures", -2000, yy)
        wire_tex(alb, tex["Albedo"])
        nrm = lib.texture_param(m, f"{layer}_Normal", "Textures", -2000, yy + 80)
        wire_tex(nrm, tex["Normal"])
        hgt = lib.texture_param(m, f"{layer}_Height", "Textures", -2000, yy + 160)
        wire_tex(hgt, tex["Height"])
        alb_s = sample_triplanar(m, alb, tri_tiling, f"{layer}_Alb", -1600, yy)
        nrm_s = sample_triplanar(m, nrm, tri_tiling, f"{layer}_Nrm", -1600, yy + 120)
        hgt_s = sample_triplanar(m, hgt, tri_tiling, f"{layer}_Hgt", -1600, yy + 240)
        tint_map = {"Rock": rock_tint, "Grass": grass_tint, "Mud": mud_tint}
        tinted = lib.create_expression(m, unreal.MaterialExpressionMultiply, -1200, yy)
        lib.connect(alb_s, "", tinted, "A")
        lib.connect(tint_map[layer], "", tinted, "B")
        weights = lib.create_expression(m, unreal.MaterialExpressionConstant3Vector, -1200, yy + 200)
        weights.set_editor_property("constant", unreal.LinearColor(0.30, 0.59, 0.11, 1.0))
        h_dot = lib.create_expression(m, unreal.MaterialExpressionDotProduct, -1040, yy + 200)
        lib.connect(hgt_s, "", h_dot, "A")
        lib.connect(weights, "", h_dot, "B")
        layer_samples[layer] = {"color": tinted, "normal": nrm_s, "height": h_dot}

    diff_gr = lib.create_expression(m, unreal.MaterialExpressionSubtract, -900, 500)
    lib.connect(layer_samples["Grass"]["height"], "", diff_gr, "A")
    lib.connect(layer_samples["Rock"]["height"], "", diff_gr, "B")
    diff_gm = lib.create_expression(m, unreal.MaterialExpressionSubtract, -900, 640)
    lib.connect(layer_samples["Grass"]["height"], "", diff_gm, "A")
    lib.connect(layer_samples["Mud"]["height"], "", diff_gm, "B")
    mod_gr = lib.create_expression(m, unreal.MaterialExpressionMultiply, -700, 500)
    lib.connect(diff_gr, "", mod_gr, "A")
    lib.connect(height_blend, "", mod_gr, "B")
    mod_gm = lib.create_expression(m, unreal.MaterialExpressionMultiply, -700, 640)
    lib.connect(diff_gm, "", mod_gm, "A")
    lib.connect(height_blend, "", mod_gm, "B")
    alpha_grass = lib.create_expression(m, unreal.MaterialExpressionClamp, -500, 500)
    lib.connect(mod_gr, "", alpha_grass, "Input")
    alpha_mud = lib.create_expression(m, unreal.MaterialExpressionClamp, -500, 640)
    lib.connect(mod_gm, "", alpha_mud, "Input")
    grass_gate = lib.create_expression(m, unreal.MaterialExpressionMultiply, -300, 500)
    lib.connect(alpha_grass, "", grass_gate, "A")
    lib.connect(grass_amt, "", grass_gate, "B")
    mud_gate = lib.create_expression(m, unreal.MaterialExpressionMultiply, -300, 640)
    lib.connect(alpha_mud, "", mud_gate, "A")
    lib.connect(mud_amt, "", mud_gate, "B")

    col_rg = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, -100, 520)
    lib.connect(layer_samples["Rock"]["color"], "", col_rg, "A")
    lib.connect(layer_samples["Grass"]["color"], "", col_rg, "B")
    lib.connect(grass_gate, "", col_rg, "Alpha")
    col_final = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 100, 560)
    lib.connect(col_rg, "", col_final, "A")
    lib.connect(layer_samples["Mud"]["color"], "", col_final, "B")
    lib.connect(mud_gate, "", col_final, "Alpha")
    nrm_rg = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, -100, 760)
    lib.connect(layer_samples["Rock"]["normal"], "", nrm_rg, "A")
    lib.connect(layer_samples["Grass"]["normal"], "", nrm_rg, "B")
    lib.connect(grass_gate, "", nrm_rg, "Alpha")
    nrm_final = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 100, 800)
    lib.connect(nrm_rg, "", nrm_final, "A")
    lib.connect(layer_samples["Mud"]["normal"], "", nrm_final, "B")
    lib.connect(mud_gate, "", nrm_final, "Alpha")

    pnorm = lib.create_expression(m, unreal.MaterialExpressionPixelNormalWS, 300, 340)
    up = lib.create_expression(m, unreal.MaterialExpressionConstant3Vector, 300, 480)
    up.set_editor_property("constant", unreal.LinearColor(0, 0, 1, 1))
    slope_dot = lib.create_expression(m, unreal.MaterialExpressionDotProduct, 500, 400)
    lib.connect(pnorm, "", slope_dot, "A")
    lib.connect(up, "", slope_dot, "B")
    slope_inv = lib.create_expression(m, unreal.MaterialExpressionOneMinus, 680, 400)
    lib.connect(slope_dot, "", slope_inv, "Input")
    slope_pow = lib.create_expression(m, unreal.MaterialExpressionPower, 860, 400)
    lib.connect(slope_inv, "", slope_pow, "Base")
    lib.connect(slope_sharp, "", slope_pow, "Exp")
    cliff_col = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 1040, 560)
    lib.connect(col_final, "", cliff_col, "A")
    lib.connect(layer_samples["Rock"]["color"], "", cliff_col, "B")
    lib.connect(slope_pow, "", cliff_col, "Alpha")

    wp = lib.create_expression(m, unreal.MaterialExpressionWorldPosition, 300, 900)
    macro_mul = lib.create_expression(m, unreal.MaterialExpressionMultiply, 500, 900)
    lib.connect(wp, "", macro_mul, "A")
    ms = lib.create_expression(m, unreal.MaterialExpressionConstant, 300, 1000)
    ms.set_editor_property("r", 0.002)
    lib.connect(ms, "", macro_mul, "B")
    macro_mul2 = lib.create_expression(m, unreal.MaterialExpressionMultiply, 700, 900)
    lib.connect(macro_mul, "", macro_mul2, "A")
    lib.connect(macro_scale, "", macro_mul2, "B")
    macro_noise = lib.create_expression(m, unreal.MaterialExpressionNoise, 900, 900)
    lib.connect(macro_mul2, "", macro_noise, "Position")
    macro_g = lib.create_expression(m, unreal.MaterialExpressionMultiply, 1100, 900)
    lib.connect(macro_noise, "", macro_g, "A")
    lib.connect(macro_str, "", macro_g, "B")
    macro_col = lib.create_expression(m, unreal.MaterialExpressionAdd, 1300, 860)
    lib.connect(cliff_col, "", macro_col, "A")
    lib.connect(macro_g, "", macro_col, "B")

    snow_dot = lib.create_expression(m, unreal.MaterialExpressionDotProduct, 1100, 1040)
    lib.connect(pnorm, "", snow_dot, "A")
    lib.connect(up, "", snow_dot, "B")
    snow_sat = lib.create_expression(m, unreal.MaterialExpressionSaturate, 1280, 1040)
    lib.connect(snow_dot, "", snow_sat, "Input")
    snow_pow = lib.create_expression(m, unreal.MaterialExpressionPower, 1460, 1040)
    lib.connect(snow_sat, "", snow_pow, "Base")
    lib.connect(snow_bias, "", snow_pow, "Exp")
    snow_amt = lib.create_expression(m, unreal.MaterialExpressionMultiply, 1640, 1040)
    lib.connect(snow_pow, "", snow_amt, "A")
    lib.connect(snow_str, "", snow_amt, "B")
    final_col = lib.create_expression(m, unreal.MaterialExpressionLinearInterpolate, 1820, 900)
    lib.connect(macro_col, "", final_col, "A")
    lib.connect(snow_tint, "", final_col, "B")
    lib.connect(snow_amt, "", final_col, "Alpha")

    toon = lib.create_expression(m, unreal.MaterialExpressionSubstrateToonBSDF, 2100, 700)
    lib.try_set_editor_property(toon, "toon_profile", profiles["TP_Default"])
    lib.connect_toon_pin(toon, final_col, ("BaseColor", "DiffuseColor"))
    lib.connect_toon_pin(toon, roughness_s, ("Roughness",))
    lib.connect_toon_pin(toon, nrm_final, ("Normal",))
    lib.connect_front_material(m, toon)
    unreal.MaterialEditingLibrary.recompile_material(m)
    lib.save_package(m)

    for spec in INSTANCES:
        mi = lib.create_material_instance(spec["name"], INST_DIR, path)
        if spec.get("profile") in profiles:
            lib.set_instance_toon_profile(mi, profiles[spec["profile"]])
        for n, v in spec.get("vectors", {}).items():
            lib.set_instance_vector(mi, n, v)
        for n, v in spec.get("scalars", {}).items():
            lib.set_instance_scalar(mi, n, v)
        lib.save_package(mi)

    print(f"LANDSCAPE_HB_OK {path} instances={len(INSTANCES)}")
    return path


def main():
    try:
        import unreal  # noqa: F401
        build()
        return 0
    except ImportError:
        import subprocess
        from pathlib import Path

        root = Path(__file__).resolve().parents[2]
        ue = Path(r"C:\Program Files\Epic Games\UE_5.8\Engine\Binaries\Win64\UnrealEditor-Cmd.exe")
        if not ue.exists():
            print(f"ERROR: {ue}")
            return 1
        os.environ.setdefault("BS_MASTER_FORCE", "1")
        cmd = [
            str(ue), str(root / "BS_GodFile.uproject"),
            f"-ExecutePythonScript={(root / 'Content/Python/setup_landscape_height_blend.py').as_posix()}",
            "-stdout", "-unattended", "-nullrhi", "-DisablePlugins=Monolith",
            f"-log={root / 'Saved/Logs/setup_landscape_height_blend.log'}",
        ]
        return subprocess.run(cmd, cwd=str(root)).returncode


if __name__ == "__main__":
    raise SystemExit(main())
