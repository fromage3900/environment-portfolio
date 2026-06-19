"""Validate Ultra Dynamic Sky time-of-day sync and wire M_Master_Toon_Universal.

UDS already drives `/Game/UltraDynamicSky/Materials/Weather/UltraDynamicWeather_Parameters`
via `Update Active Variables` / `Update Material Effect Parameters` on the
Ultra_Dynamic_Sky (and Ultra_Dynamic_Weather) blueprint. No separate
MPC_Portfolio_TimeOfDay is created — that would be a stale duplicate.

Portfolio materials read UDS live through:
  - Material function `Day_to_Night_Color` (Sun Vector from UDS MPC)
  - Static switch `UseUDSTimeOfDay` + scalar `TimeOfDayMPCStrength` on the universal master

Run (editor open):
  py "G:/EnvironmentPortfolio/BS_GodFile/Content/Python/setup_time_of_day_mpc.py"
  py ".../setup_time_of_day_mpc.py" --rebuild-master

Also see: setup_portfolio_mpc.py (manual scene palette — MPC_Portfolio_Palette)
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import unreal

import material_lib as lib

REPORT = Path(__file__).resolve().parents[2] / "Saved" / "Audit" / "uds_time_of_day_sync.json"

UDS_ROOT = "/Game/UltraDynamicSky"
UDS_BP = f"{UDS_ROOT}/Blueprints/Ultra_Dynamic_Sky"
UDS_WEATHER_BP = f"{UDS_ROOT}/Blueprints/Ultra_Dynamic_Weather"
UDS_MPC = f"{UDS_ROOT}/Materials/Weather/UltraDynamicWeather_Parameters"
MF_DTN_FLOAT = f"{UDS_ROOT}/Materials/Material_Functions/Sky_Utilities/Day_to_Night_Float"
MF_DTN_COLOR = f"{UDS_ROOT}/Materials/Material_Functions/Sky_Utilities/Day_to_Night_Color"
MASTER = f"{lib.MASTER_DIR}/M_Master_Toon_Universal"

UDS_MPC_SCALARS = [
    "Time of Day",  # 0–2400, updated by UDS each tick
    "DLWE_Base Wetness",
    "DLWE_Snow Depth",
    "Wind Intensity",
    "Wind Force",
    "Wind Angle",
]

UDS_MPC_VECTORS = [
    "Sun Vector",  # drives Day_to_Night_* material functions
    "Moon Vector",
    "Ambient Fog Color",
    "Snow Color",
    "Dust Color",
]

UDS_BP_PROPERTIES = [
    "Time of Day",  # float 0–2400
    "Sun Angle",
    "Sun Inclination",
    "Animate Time of Day",
    "Day Length",
    "Night Length",
]

UDS_BP_FUNCTIONS = [
    "Update Active Variables",
    "Get Time of Day in Real Time Format",
    "Set Time of Day Using Time Code",
    "Bind to Sunrise",
    "Bind to Sunset",
]


def _asset_ok(path: str) -> bool:
    leaf = path.rsplit("/", 1)[-1]
    return unreal.EditorAssetLibrary.does_asset_exist(f"{path}.{leaf}")


def audit_uds() -> dict:
    mpc_path = f"{UDS_MPC}.UltraDynamicWeather_Parameters"
    return {
        "feasible": _asset_ok(UDS_MPC) and _asset_ok(MF_DTN_COLOR),
        "uds_mpc": mpc_path if _asset_ok(UDS_MPC) else None,
        "uds_blueprint": UDS_BP if _asset_ok(UDS_BP) else None,
        "uds_weather_blueprint": UDS_WEATHER_BP if _asset_ok(UDS_WEATHER_BP) else None,
        "material_functions": {
            "Day_to_Night_Float": MF_DTN_FLOAT if _asset_ok(MF_DTN_FLOAT) else None,
            "Day_to_Night_Color": MF_DTN_COLOR if _asset_ok(MF_DTN_COLOR) else None,
        },
        "mpc_scalars": UDS_MPC_SCALARS,
        "mpc_vectors": UDS_MPC_VECTORS,
        "uds_properties": UDS_BP_PROPERTIES,
        "uds_functions": UDS_BP_FUNCTIONS,
        "sync_mechanism": (
            "UDS actor runs Update Active Variables each frame (or on interval), "
            "writing Time of Day and Sun Vector into UltraDynamicWeather_Parameters. "
            "Materials sample that MPC directly or via Day_to_Night_Float/Color."
        ),
        "portfolio_mpc_decision": (
            "MPC_Portfolio_TimeOfDay NOT created — UDS MPC is the live source of truth. "
            "MPC_Portfolio_Palette.TimeOfDayWarmth remains a manual scene-grade overlay."
        ),
    }


def rebuild_master_if_requested() -> str | None:
    if not any("rebuild" in str(a).lower() for a in sys.argv):
        return None
    import setup_master_universal as master

    sys.argv = [a for a in sys.argv if "rebuild" not in a.lower()] + ["--force"]
    return master.build()


def main() -> int:
    audit = audit_uds()
    master_path = None
    if audit["feasible"]:
        master_path = rebuild_master_if_requested()
        if not master_path and _asset_ok(MASTER):
            master_path = f"{MASTER}.M_Master_Toon_Universal"
    else:
        unreal.log_error(
            "[UDS ToD] UltraDynamicWeather_Parameters or Day_to_Night_Color missing. "
            "Install/sync Content/UltraDynamicSky before enabling UseUDSTimeOfDay."
        )

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        **audit,
        "master_material": master_path,
        "material_switches": {
            "UseUDSTimeOfDay": "Static switch on M_Master_Toon_Universal (default off)",
            "TimeOfDayMPCStrength": "Scalar 0–1 blend toward UDS day/night tint",
            "TimeOfDayWarmth": "Manual fallback when UseUDSTimeOfDay is off",
        },
        "level_setup": [
            "1. Drag Ultra_Dynamic_Sky into the level (Content/UltraDynamicSky/Blueprints).",
            "2. Optional: add Ultra_Dynamic_Weather for wetness/snow MPC scalars.",
            "3. Set Basic Controls → Time of Day (0–2400, e.g. 1200 = noon).",
            "4. Enable Animate Time of Day for runtime cycle, or drive Time of Day from Sequencer/Blueprint.",
            "5. On material instances using M_Master_Toon_Universal: enable UseUDSTimeOfDay.",
            "6. Tune TimeOfDayMPCStrength (default 1) for grade intensity.",
        ],
        "external_control": (
            "Get Actor of Class → Ultra_Dynamic_Sky, set Time of Day variable. "
            "Disable Animate Time of Day on UDS to avoid conflicts. "
            "Utility functions: Set Time of Day Using Time Code, Bind to Sunrise/Sunset."
        ),
        "rebuild_command": (
            'py "G:/EnvironmentPortfolio/BS_GodFile/Content/Python/setup_time_of_day_mpc.py" --rebuild-master'
        ),
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if audit["feasible"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
