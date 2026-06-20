"""Expand M_Water_Master_Grand_v6 — canonical portfolio grand water shader.

Does NOT create a separate water master. Wires compositing caustics where applicable,
creates starter instances, and writes audit JSON.

Run (editor):
  py "G:/EnvironmentPortfolio/BS_GodFile/Content/Python/setup_master_water.py"

Headless:
  python Content/Python/setup_master_water.py
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

MASTER_NAME = "M_Water_Master_Grand_v6"
MASTER_PATH = f"/Game/EnvSandbox/Materials/Masters/{MASTER_NAME}"
INST_DIR = "/Game/EnvSandbox/Materials/Instances/Water"
REPORT = Path(__file__).resolve().parents[2] / "Saved" / "Audit" / "grand_water_expand.json"

# Params detected on M_Water_Master_Grand_v6 (disk + editor audit)
GRAND_WATER_SCALARS = (
    "CausticIntensity",
    "GerstnerScale",
    "WaveSpeed",
    "WaterRoughness",
    "MagicalIntensity",
)

INSTANCES = [
    {
        "name": "MI_GrandWater_OceanDeep",
        "scalars": {
            "CausticIntensity": 0.45,
            "GerstnerScale": 0.06,
            "WaveSpeed": 0.35,
            "WaterRoughness": 0.05,
            "MagicalIntensity": 0.0,
        },
    },
    {
        "name": "MI_GrandWater_RiverClear",
        "scalars": {
            "CausticIntensity": 0.65,
            "GerstnerScale": 0.12,
            "WaveSpeed": 0.55,
            "WaterRoughness": 0.08,
            "MagicalIntensity": 0.15,
        },
    },
    {
        "name": "MI_GrandWater_PondStylized",
        "scalars": {
            "CausticIntensity": 0.75,
            "GerstnerScale": 0.18,
            "WaveSpeed": 0.18,
            "WaterRoughness": 0.10,
            "MagicalIntensity": 0.35,
        },
    },
]


def _audit_grand_water(material) -> dict:
    import unreal

    params: list[dict] = []
    for expr in unreal.MaterialEditingLibrary.get_material_expressions(material) or []:
        if not expr:
            continue
        tname = type(expr).__name__
        if "Parameter" not in tname or "Function" in tname:
            continue
        pname = None
        for prop in ("parameter_name", "ParameterName"):
            try:
                raw = expr.get_editor_property(prop)
                if raw:
                    pname = str(raw)
                    break
            except Exception:
                pass
        if not pname:
            continue
        group = ""
        try:
            group = str(expr.get_editor_property("group") or "")
        except Exception:
            pass
        kind = "texture" if "Texture" in tname else ("vector" if "Vector" in tname else "scalar")
        params.append({"name": pname, "kind": kind, "group": group})

    names = {p["name"] for p in params}
    return {
        "param_count": len(params),
        "params": params,
        "expected_scalars_present": {s: s in names for s in GRAND_WATER_SCALARS},
    }


def build() -> str:
    import unreal
    import material_lib as lib

    asset_path = f"{MASTER_PATH}.{MASTER_NAME}"
    if not unreal.EditorAssetLibrary.does_asset_exist(MASTER_PATH):
        raise RuntimeError(f"{MASTER_PATH} missing — grand water is the canonical shader")

    mat = unreal.load_asset(asset_path)
    if not mat:
        raise RuntimeError(f"Failed to load {asset_path}")

    audit_before = _audit_grand_water(mat)

    # Wire compositing caustics/sparkle on any unwired texture param named *Caustic*
    import portfolio_texture_catalog as catalog

    caustic_chain = catalog._chain(
        catalog.COMPOSITING["noise_fine"],
        "/Game/Alphas_Sparkles/T_Spark_Twinkle8.T_Spark_Twinkle8",
        catalog.MASK["voronoi_swirl"],
    )
    wired_textures: list[str] = []
    for expr, _owner in lib.iter_texture_parameter_expressions(mat):
        pname = None
        for prop in ("parameter_name", "ParameterName"):
            try:
                raw = expr.get_editor_property(prop)
                if raw:
                    pname = str(raw)
                    break
            except Exception:
                pass
        if not pname or "caustic" not in pname.lower():
            continue
        tex = None
        for prop in ("texture", "Texture"):
            try:
                tex = expr.get_editor_property(prop)
                if tex:
                    break
            except Exception:
                pass
        if lib.is_placeholder_texture(tex) or lib.is_banned_texture(tex):
            path = lib.resolve_texture_path(caustic_chain)
            if path and lib.set_expression_texture(expr, path):
                wired_textures.append(pname)

    try:
        unreal.MaterialEditingLibrary.recompile_material(mat)
    except Exception as exc:
        unreal.log_warning(f"[GrandWater] compile: {exc}")
    lib.save_package(mat)

    lib.ensure_directory(INST_DIR)
    parent = asset_path
    created: list[str] = []
    for spec in INSTANCES:
        mi = lib.create_material_instance(spec["name"], INST_DIR, parent)
        for n, v in spec.get("scalars", {}).items():
            try:
                lib.set_instance_scalar(mi, n, v)
            except Exception as exc:
                unreal.log_warning(f"[GrandWater] {spec['name']} {n}: {exc}")
        lib.save_package(mi)
        created.append(spec["name"])

    audit_after = _audit_grand_water(mat)
    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "master": MASTER_PATH,
        "canonical": True,
        "note": "M_Master_Toon_Water is deprecated — use M_Water_Master_Grand_v6 only",
        "wired_textures": wired_textures,
        "instances": created,
        "audit_before": audit_before,
        "audit_after": audit_after,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    unreal.log(f"[GrandWater] expanded {MASTER_PATH} instances={len(created)} -> {REPORT}")
    print(f"GRAND_WATER_OK {MASTER_PATH} instances={created}")
    return MASTER_PATH


def main():
    try:
        import unreal  # noqa: F401
        build()
        return 0
    except ImportError:
        import subprocess

        root = Path(__file__).resolve().parents[2]
        ue = Path(r"C:\Program Files\Epic Games\UE_5.8\Engine\Binaries\Win64\UnrealEditor-Cmd.exe")
        if not ue.exists():
            print(f"ERROR: {ue}")
            return 1
        cmd = [
            str(ue),
            str(root / "BS_GodFile.uproject"),
            f"-ExecutePythonScript={(root / 'Content/Python/setup_master_water.py').as_posix()}",
            "-stdout",
            "-unattended",
            "-nullrhi",
            f"-log={root / 'Saved/Logs/setup_grand_water.log'}",
        ]
        return subprocess.run(cmd, cwd=str(root)).returncode


if __name__ == "__main__":
    raise SystemExit(main())
