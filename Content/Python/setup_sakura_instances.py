"""Build the MI_Sakura_* material set for the SakuraPath scene, on M_Master_Toon_Universal.

Run AFTER rebuilding the master (so the new MacroDetail/Magical params exist):
  py "G:/EnvironmentPortfolio/BS_GodFile/Content/Python/setup_master_universal.py"
  py "G:/EnvironmentPortfolio/BS_GodFile/Content/Python/setup_sakura_instances.py"
"""
from __future__ import annotations

import unreal
import material_lib as lib

PARENT = f"{lib.MASTER_DIR}/M_Master_Toon_Universal"
FOLDER = f"{lib.MATERIALS_ROOT}/Instances/Sakura"

SAKURA = [
    {"name": "MI_Sakura_Blossom", "profile": "TP_Default",
     "vectors": {"BaseTint": (1.0, 0.74, 0.84, 1.0), "RimColor": (1.0, 0.60, 0.78, 1.0), "DreamTint": (1.0, 0.80, 0.90, 1.0)},
     "scalars": {"TextureWeight": 0.30, "PastelLift": 0.55, "RimIntensity": 1.2, "RimPower": 3.0,
                 "SparkleIntensity": 1.6, "SparkleScale": 10.0, "GlowIntensity": 0.15, "Roughness": 0.75}},
    {"name": "MI_Sakura_Bark", "profile": "TP_Stone",
     "vectors": {"BaseTint": (0.30, 0.22, 0.17, 1.0)},
     "scalars": {"TextureWeight": 0.90, "Roughness": 0.82, "MacroVariationStrength": 0.30, "MacroScale": 0.0012,
                 "DetailStrength": 0.50, "DetailTiling": 10.0}},
    {"name": "MI_Sakura_StonePath", "profile": "TP_Stone",
     "vectors": {"BaseTint": (0.52, 0.50, 0.47, 1.0)},
     "scalars": {"TextureWeight": 0.90, "Roughness": 0.85, "MacroVariationStrength": 0.40,
                 "DetailStrength": 0.60, "DetailTiling": 6.0}},
    {"name": "MI_Sakura_Moss", "profile": "TP_Default",
     "vectors": {"BaseTint": (0.20, 0.34, 0.17, 1.0)},
     "scalars": {"TextureWeight": 0.85, "Roughness": 0.90, "MacroVariationStrength": 0.30}},
    {"name": "MI_Sakura_Water", "profile": "TP_Glass",
     "vectors": {"BaseTint": (0.42, 0.55, 0.68, 1.0), "IridescenceTint": (0.80, 0.70, 0.95, 1.0)},
     "scalars": {"TextureWeight": 0.20, "Roughness": 0.12, "Iridescence": 0.35, "GlowIntensity": 0.05, "RimIntensity": 0.40}},
    {"name": "MI_Sakura_ToriiRed", "profile": "TP_Default",
     "vectors": {"BaseTint": (0.66, 0.14, 0.11, 1.0)},
     "scalars": {"TextureWeight": 0.55, "Roughness": 0.38, "MacroVariationStrength": 0.20, "DetailStrength": 0.30}},
    {"name": "MI_Sakura_Lantern", "profile": "TP_Stone",
     "vectors": {"BaseTint": (0.55, 0.53, 0.48, 1.0), "GlowColor": (1.0, 0.78, 0.45, 1.0)},
     "scalars": {"TextureWeight": 0.85, "Roughness": 0.80, "GlowIntensity": 0.60, "MacroVariationStrength": 0.30, "DetailStrength": 0.40}},
    {"name": "MI_Sakura_Grass", "profile": "TP_Foliage",
     "vectors": {"BaseTint": (0.24, 0.40, 0.20, 1.0)},
     "scalars": {"TextureWeight": 0.80, "Roughness": 0.88}},
]


def build():
    if not unreal.EditorAssetLibrary.does_asset_exist(PARENT):
        unreal.log_error("[Sakura] master missing — run setup_master_universal.py first")
        return
    lib.ensure_directory(FOLDER)
    profiles = lib.create_toon_profiles(["TP_Default", "TP_Stone", "TP_Glass", "TP_Foliage", "TP_Gold"])
    made = []
    for spec in SAKURA:
        mi = lib.create_material_instance(spec["name"], FOLDER, PARENT)
        if spec.get("profile") in profiles:
            lib.set_instance_toon_profile(mi, profiles[spec["profile"]])
        for n, v in spec.get("vectors", {}).items():
            try: lib.set_instance_vector(mi, n, v)
            except Exception as e: unreal.log_warning(f"[Sakura] {spec['name']} vec {n}: {e}")
        for n, v in spec.get("scalars", {}).items():
            try: lib.set_instance_scalar(mi, n, v)
            except Exception as e: unreal.log_warning(f"[Sakura] {spec['name']} scl {n}: {e}")
        lib.save_package(mi)
        made.append(spec["name"])
    unreal.log(f"[Sakura] built {len(made)} instances in {FOLDER}")
    print(f"SAKURA_INSTANCES {made}")


if __name__ == "__main__":
    build()
