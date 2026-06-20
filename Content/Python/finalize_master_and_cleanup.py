"""Professional finishing pass on M_Master_Toon_Universal + instance-library cleanup.

1. Replace the master's DefaultTexture (engine checkerboard) fallbacks on every
   TextureObjectParameter / TextureSampleParameter2D with sensible neutral defaults
   (white albedo, FLAT normal, neutral height, thematic masks). Normals on
   DefaultTexture is an actual bug — flat normal is the correct neutral.
2. Delete the legacy MI_Universal_* sprawl so the library is exactly the curated
   20 (Showcase 10 + Sakura 10). User-authorized ("delete them all").

Headless (editor closed, SCC disabled by caller):
  UnrealEditor-Cmd BS_GodFile.uproject -ExecutePythonScript=".../finalize_master_and_cleanup.py"
    -unattended -nullrhi -DisablePlugins=Monolith
"""
from __future__ import annotations

import unreal

MASTER = "/Game/EnvSandbox/Materials/Masters/M_Master_Toon_Universal"

WHITE = "/Engine/EngineResources/WhiteSquareTexture.WhiteSquareTexture"
FLAT_N = "/Engine/EngineMaterials/DefaultNormal.DefaultNormal"
HEART = "/Game/Magical/T_Magic_Heart.T_Magic_Heart"
STAR = "/Game/Magical/T_Magic_Star.T_Magic_Star"

# param-name -> sensible default texture (neutral, never the checkerboard)
DEFAULTS = {
    "Albedo": WHITE,
    "LayerB_Albedo": WHITE,
    "NormalMap": FLAT_N,
    "LayerB_NormalMap": FLAT_N,
    "DetailNormal": FLAT_N,
    "HeightMap": WHITE,
    "LayerB_HeightMap": WHITE,
    # ORM / LayerB_ORM intentionally NOT defaulted here: white would force
    # metallic=1 if the graph reads its B channel. Left for a traced review.
    "SparkleMask": STAR,
    "MotifMask": HEART,
    "FairyGlyphMask": STAR,
}

# Keep ONLY these instance folders; delete the rest of the sprawl.
KEEP_DIRS = {"Showcase", "Sakura"}
INST_ROOT = "/Game/EnvSandbox/Materials/Instances"
LEGACY_DIRS = [f"{INST_ROOT}/Environment", f"{INST_ROOT}/Stylized"]


def fix_master_textures():
    if not unreal.EditorAssetLibrary.does_asset_exist(MASTER):
        unreal.log_error("[Finalize] master missing")
        return 0
    m = unreal.load_asset(MASTER)
    resolved = {k: v for k, v in DEFAULTS.items()
                if unreal.EditorAssetLibrary.does_asset_exist(v.split(".")[0])}
    missing = set(DEFAULTS) - set(resolved)
    if missing:
        unreal.log_warning(f"[Finalize] default textures not found, skipped: {missing}")

    changed = 0
    for expr in unreal.MaterialEditingLibrary.get_material_expressions(m) or []:
        pname = None
        for prop in ("parameter_name", "ParameterName"):
            try:
                raw = expr.get_editor_property(prop)
                if raw:
                    pname = str(raw)
                    break
            except Exception:
                continue
        if not pname or pname not in resolved:
            continue
        tex = unreal.load_asset(resolved[pname].split(".")[0])
        if not tex:
            continue
        for tprop in ("texture", "Texture"):
            try:
                expr.set_editor_property(tprop, tex)
                changed += 1
                unreal.log(f"[Finalize] {pname} -> {resolved[pname].rsplit('/',1)[-1]}")
                break
            except Exception:
                continue
    unreal.MaterialEditingLibrary.recompile_material(m)
    unreal.EditorAssetLibrary.save_loaded_asset(m, only_if_is_dirty=False)
    return changed


def cleanup_legacy():
    removed = []
    for d in LEGACY_DIRS:
        if unreal.EditorAssetLibrary.does_directory_exist(d):
            if unreal.EditorAssetLibrary.delete_directory(d):
                removed.append(d)
            else:
                unreal.log_warning(f"[Finalize] failed to delete {d}")
    return removed


def main():
    try:
        unreal.AssetRegistryHelpers.get_asset_registry().search_all_assets(True)
    except Exception as e:
        unreal.log_warning(f"[Finalize] registry: {e}")

    changed = fix_master_textures()
    removed = cleanup_legacy()
    unreal.log(f"[Finalize] master tex defaults set={changed}; legacy dirs removed={removed}")
    print(f"FINALIZE_OK tex_defaults={changed} legacy_removed={len(removed)}")


if __name__ == "__main__":
    main()
