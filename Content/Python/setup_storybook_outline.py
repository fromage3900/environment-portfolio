"""Storybook post-process: cel outline + vine/branch growth along detected edges.

Stack after M_PP_ToonOutline on the portfolio PostProcessVolume:
  1. M_PP_ToonOutline — depth/normal edge ink
  2. M_PP_StorybookVines — organic growth from edges (this material)

Assign VineBranchMask to a branching noise / ivy alpha (e.g. from Stylization/).

Run:
  py "G:/EnvironmentPortfolio/BS_GodFile/Content/Python/setup_storybook_outline.py"
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import unreal

import material_lib as lib

REPORT_PATH = Path(__file__).resolve().parents[2] / "Saved" / "Audit" / "storybook_outline_build.json"
PP_NAME = "M_PP_StorybookVines"


def build_storybook_pp() -> str:
    lib.ensure_directory(lib.POST_DIR)
    path = lib.asset_path(lib.POST_DIR, PP_NAME)
    if unreal.EditorAssetLibrary.does_asset_exist(path):
        unreal.EditorAssetLibrary.delete_asset(path)

    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    material = asset_tools.create_asset(
        PP_NAME, lib.POST_DIR, unreal.Material, unreal.MaterialFactoryNew()
    )
    if not material:
        raise RuntimeError(f"Failed to create {PP_NAME}")

    material.set_editor_property("material_domain", unreal.MaterialDomain.MD_POST_PROCESS)
    try:
        material.set_editor_property(
            "blendable_location", unreal.BlendableLocation.BL_SCENE_COLOR_AFTER_TONEMAP
        )
    except AttributeError:
        material.set_editor_property(
            "blendable_location", unreal.BlendableLocation.BL_REPLACING_TONEMAPPER
        )

    scene = lib.create_expression(material, unreal.MaterialExpressionSceneTexture, -1000, 0)
    scene.set_editor_property("scene_texture_id", unreal.SceneTextureId.PPI_SCENE_COLOR)

    depth = lib.create_expression(material, unreal.MaterialExpressionSceneTexture, -1000, 200)
    depth.set_editor_property("scene_texture_id", unreal.SceneTextureId.PPI_SCENE_DEPTH)

    normals = lib.create_expression(material, unreal.MaterialExpressionSceneTexture, -1000, 400)
    normals.set_editor_property("scene_texture_id", unreal.SceneTextureId.PPI_WORLD_NORMAL)

    # outline edge mask (depth + normal discontinuity)
    ddx_d = lib.create_expression(material, unreal.MaterialExpressionDDX, -760, 200)
    lib.connect_unary(depth, ddx_d)
    ddy_d = lib.create_expression(material, unreal.MaterialExpressionDDY, -760, 280)
    lib.connect_unary(depth, ddy_d)
    edge_d = lib.create_expression(material, unreal.MaterialExpressionAdd, -560, 240)
    lib.connect(ddx_d, "", edge_d, "A")
    lib.connect(ddy_d, "", edge_d, "B")

    ddx_n = lib.create_expression(material, unreal.MaterialExpressionDDX, -760, 400)
    lib.connect_unary(normals, ddx_n)
    ddy_n = lib.create_expression(material, unreal.MaterialExpressionDDY, -760, 480)
    lib.connect_unary(normals, ddy_n)
    edge_n = lib.create_expression(material, unreal.MaterialExpressionAdd, -560, 440)
    lib.connect(ddx_n, "", edge_n, "A")
    lib.connect(ddy_n, "", edge_n, "B")

    edge_raw = lib.create_expression(material, unreal.MaterialExpressionAdd, -360, 320)
    lib.connect(edge_d, "", edge_raw, "A")
    lib.connect(edge_n, "", edge_raw, "B")
    edge_abs = lib.create_expression(material, unreal.MaterialExpressionAbs, -200, 320)
    lib.connect_unary(edge_raw, edge_abs)

    edge_width = lib.scalar_param(material, "OutlineWidth", "Storybook", 2.0, -1000, 600)
    edge_str = lib.scalar_param(material, "EdgeStrength", "Storybook", 1.0, -1000, 700)
    edge_mask = lib.create_expression(material, unreal.MaterialExpressionMultiply, 0, 320)
    lib.connect(edge_abs, "", edge_mask, "A")
    lib.connect(edge_width, "", edge_mask, "B")
    edge_sat = lib.create_expression(material, unreal.MaterialExpressionMultiply, 160, 320)
    lib.connect(edge_mask, "", edge_sat, "A")
    lib.connect(edge_str, "", edge_sat, "B")
    edge_clamp = lib.create_expression(material, unreal.MaterialExpressionSaturate, 320, 320)
    lib.connect_unary(edge_sat, edge_clamp)

    # vine growth: branch mask scrolled along screen-space diagonal + edge seed
    vine_len = lib.scalar_param(material, "VineGrowthLength", "Storybook", 0.35, -1000, 820)
    vine_scale = lib.scalar_param(material, "VineBranchScale", "Storybook", 6.0, -1000, 920)
    vine_str = lib.scalar_param(material, "VineBranchStrength", "Storybook", 0.75, -1000, 1020)
    vine_speed = lib.scalar_param(material, "VineGrowthSpeed", "Storybook", 0.08, -1000, 1120)
    vine_ink = lib.vector_param(material, "VineInkColor", "Storybook", (0.04, 0.12, 0.06, 1.0), -1000, 1220)
    leaf_tint = lib.vector_param(material, "LeafHighlightColor", "Storybook", (0.35, 0.62, 0.28, 1.0), -1000, 1340)
    branch_tex = lib.texture_param(material, "VineBranchMask", "Storybook", -1000, 1460)

    screen_uv = lib.create_expression(material, unreal.MaterialExpressionTextureCoordinate, -760, 900)
    time_n = lib.create_expression(material, unreal.MaterialExpressionTime, -760, 1040)
    scroll = lib.create_expression(material, unreal.MaterialExpressionMultiply, -560, 1040)
    lib.connect(time_n, "", scroll, "A")
    lib.connect(vine_speed, "", scroll, "B")
    uv_scroll = lib.create_expression(material, unreal.MaterialExpressionAdd, -560, 900)
    lib.connect(screen_uv, "", uv_scroll, "A")
    lib.connect(scroll, "", uv_scroll, "B")
    uv_scale = lib.create_expression(material, unreal.MaterialExpressionMultiply, -360, 900)
    lib.connect(uv_scroll, "", uv_scale, "A")
    lib.connect(vine_scale, "", uv_scale, "B")
    lib.connect(uv_scale, "", branch_tex, "Coordinates")

    branch_seed = lib.create_expression(material, unreal.MaterialExpressionMultiply, 480, 520)
    lib.connect(edge_clamp, "", branch_seed, "A")
    lib.connect(branch_tex, "", branch_seed, "B")
    vine_grow = lib.create_expression(material, unreal.MaterialExpressionMultiply, 640, 520)
    lib.connect(branch_seed, "", vine_grow, "A")
    lib.connect(vine_len, "", vine_grow, "B")
    vine_w = lib.create_expression(material, unreal.MaterialExpressionMultiply, 800, 520)
    lib.connect(vine_grow, "", vine_w, "A")
    lib.connect(vine_str, "", vine_w, "B")

    ink_line = lib.create_expression(material, unreal.MaterialExpressionLinearInterpolate, 480, 200)
    lib.connect(scene, "", ink_line, "A")
    lib.connect(vine_ink, "", ink_line, "B")
    lib.connect(edge_clamp, "", ink_line, "Alpha")

    vine_line = lib.create_expression(material, unreal.MaterialExpressionLinearInterpolate, 960, 360)
    lib.connect(ink_line, "", vine_line, "A")
    lib.connect(leaf_tint, "", vine_line, "B")
    lib.connect(vine_w, "", vine_line, "Alpha")

    unreal.MaterialEditingLibrary.connect_material_property(
        vine_line, "", unreal.MaterialProperty.MP_EMISSIVE_COLOR
    )

    try:
        unreal.MaterialEditingLibrary.recompile_material(material)
    except Exception as exc:
        unreal.log_warning(f"[StorybookPP] compile warning: {exc}")

    lib.save_package(material)
    unreal.log(f"[StorybookPP] built {path}")
    return path


def build_all() -> int:
    path = build_storybook_pp()
    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "post_process": path,
        "stack_note": "Add to PPV blendables after M_PP_ToonOutline",
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(build_all())
