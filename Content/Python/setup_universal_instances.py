"""Create themed MI_* instances for M_Master_Toon_Universal.

Run after setup_master_universal.py:
  py "G:/EnvironmentPortfolio/BS_GodFile/Content/Python/setup_universal_instances.py"
"""
from __future__ import annotations

import json
from pathlib import Path

import material_lib as lib

MASTER = f"{lib.MASTER_DIR}/M_Master_Toon_Universal.M_Master_Toon_Universal"
REPORT = Path(__file__).resolve().parents[2] / "Saved" / "Audit" / "universal_instances.json"

INSTANCES: list[dict] = [
    {
        "name": "MI_Universal_Default",
        "profile": "TP_Default",
        "vectors": {"BaseTint": (0.62, 0.58, 0.55, 1.0)},
        "scalars": {"TextureWeight": 1.0, "UVScale": 1.0, "Roughness": 0.65, "Metallic": 0.0},
    },
    {
        "name": "MI_Universal_DreamyPastel",
        "profile": "TP_Default",
        "vectors": {
            "BaseTint": (0.78, 0.72, 0.82, 1.0),
            "DreamTint": (1.0, 0.88, 0.96, 1.0),
            "ShadowDreamTint": (0.55, 0.48, 0.72, 1.0),
            "GlowColor": (1.0, 0.92, 0.98, 1.0),
        },
        "scalars": {
            "PastelLift": 0.42,
            "InnerGlowIntensity": 0.25,
            "GlowIntensity": 0.12,
            "ShadowDreamStrength": 0.55,
            "ShadowSoftness": 0.7,
            "BloomBoost": 0.15,
        },
    },
    {
        "name": "MI_Universal_Constellation",
        "profile": "TP_Default",
        "vectors": {
            "BaseTint": (0.12, 0.14, 0.28, 1.0),
            "ConstellationRampLow": (0.08, 0.10, 0.22, 1.0),
            "ConstellationRampMid": (0.35, 0.55, 0.95, 1.0),
            "ConstellationRampHigh": (0.95, 0.88, 1.0, 1.0),
            "RimColor": (0.55, 0.75, 1.0, 1.0),
        },
        "scalars": {
            "ConstellationStrength": 0.85,
            "ConstellationScale": 2.4,
            "ConstellationPhase": 0.0,
            "RimIntensity": 0.35,
            "RimPower": 4.5,
            "Metallic": 0.15,
        },
    },
    {
        "name": "MI_Universal_GoldLeaf",
        "profile": "TP_Gold",
        "vectors": {
            "BaseTint": (0.48, 0.40, 0.34, 1.0),
            "GoldTint": (0.92, 0.72, 0.28, 1.0),
            "GoldEmissive": (0.45, 0.32, 0.08, 1.0),
        },
        "scalars": {
            "GildingStrength": 0.72,
            "CurvatureSensitivity": 3.2,
            "GoldRoughness": 0.22,
            "Metallic": 0.85,
            "Roughness": 0.38,
        },
    },
    {
        "name": "MI_Universal_FairyHearts",
        "profile": "TP_Default",
        "vectors": {
            "BaseTint": (0.82, 0.62, 0.72, 1.0),
            "FairyDustColor": (1.0, 0.55, 0.72, 1.0),
            "DreamTint": (1.0, 0.86, 0.92, 1.0),
        },
        "scalars": {
            "FairyMotifStyle": 1.0,
            "FairyDustIntensity": 0.65,
            "FairyDustScale": 12.0,
            "FairyHighlightThreshold": 0.42,
            "PastelLift": 0.2,
            "BloomBoost": 0.35,
        },
    },
    {
        "name": "MI_Universal_FairyStars",
        "profile": "TP_Default",
        "vectors": {
            "BaseTint": (0.22, 0.28, 0.42, 1.0),
            "FairyDustColor": (0.95, 0.92, 1.0, 1.0),
            "RimColor": (0.65, 0.82, 1.0, 1.0),
        },
        "scalars": {
            "FairyMotifStyle": 2.0,
            "FairyDustIntensity": 0.8,
            "FairyDustScale": 18.0,
            "RimIntensity": 0.28,
            "ConstellationStrength": 0.35,
            "Metallic": 0.25,
        },
    },
    {
        "name": "MI_Universal_FairyGarden",
        "profile": "TP_Default",
        "vectors": {
            "BaseTint": (0.58, 0.72, 0.52, 1.0),
            "FairyDustColor": (1.0, 0.78, 0.92, 1.0),
            "ShadowFlowerColor": (0.95, 0.55, 0.78, 1.0),
            "ShadowDreamTint": (0.42, 0.58, 0.48, 1.0),
        },
        "scalars": {
            "FairyMotifStyle": 3.0,
            "FairyDustIntensity": 0.5,
            "ShadowFlowerStrength": 0.62,
            "ShadowFlowerScale": 6.0,
            "ShadowDreamStrength": 0.4,
            "GildingStrength": 0.15,
        },
    },
    {
        "name": "MI_Universal_MoonlitMetal",
        "profile": "TP_Gold",
        "vectors": {
            "BaseTint": (0.18, 0.20, 0.32, 1.0),
            "FairyDustColor": (0.88, 0.92, 1.0, 1.0),
            "GoldTint": (0.85, 0.78, 0.55, 1.0),
        },
        "scalars": {
            "FairyMotifStyle": 4.0,
            "FairyDustIntensity": 0.45,
            "Metallic": 0.92,
            "Roughness": 0.28,
            "RimIntensity": 0.22,
            "ConstellationStrength": 0.25,
        },
    },
]


def build_instances() -> list[dict]:
    import unreal

    if not unreal.EditorAssetLibrary.does_asset_exist(MASTER):
        raise RuntimeError(f"Missing master: {MASTER} — run setup_master_universal.py first")

    profiles = lib.create_toon_profiles(["TP_Default", "TP_Gold"])
    results: list[dict] = []

    for spec in INSTANCES:
        inst = lib.create_material_instance(spec["name"], lib.ENV_INST_DIR, MASTER)
        profile = profiles.get(spec.get("profile", "TP_Default"))
        if profile:
            lib.set_instance_toon_profile(inst, profile)
        for name, rgba in spec.get("vectors", {}).items():
            lib.set_instance_vector(inst, name, rgba)
        for name, value in spec.get("scalars", {}).items():
            lib.set_instance_scalar(inst, name, value)
        lib.save_package(inst)
        results.append({"instance": spec["name"], "status": "created_or_updated"})

    return results


def main() -> int:
    try:
        import unreal  # noqa: F401
    except ImportError:
        print("Requires Unreal Editor Python")
        return 1

    results = build_instances()
    report = {"instances": results, "count": len(results)}
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
