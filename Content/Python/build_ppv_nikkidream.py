"""Build BP_PPV_NikkiDream - a droppable, level-agnostic dreamy post-process volume.

Stacks the project's existing PP materials as blendables + UDS-aware native settings.
Does NOT touch any level; you drop BP_PPV_NikkiDream into zenforesttest (or any level)
when ready. Unbound = affects the whole level.

Run inside the editor (Monolith run_python) after relaunch:
  import build_ppv_nikkidream as b; b.build()

Blendable stack (order matters - grade LAST):
  1. M_PP_ToonOutline        - crisp toon silhouette lines
  2. M_PP_StorybookVines_Inst- animated storybook vine border frame
  3. M_PP_MeluColorGrade     - Melusina palette tint + emissive boost

Native settings tuned for the Nikki-dream look. NOTE on UDS: Ultra Dynamic Sky
drives its own exposure/fog. Keep this volume's exposure OVERRIDES OFF (below) so
UDS stays in control; this volume only adds bloom/vignette/CA/grain/grade on top.
Tune bloom vs UDS in-editor.
"""
from __future__ import annotations

DIR = "/Game/EnvSandbox/PostProcess"
BLENDABLES = [
    "/Game/EnvSandbox/Materials/PostProcess/M_PP_ToonOutline",
    "/Game/EnvSandbox/Materials/PostProcess/M_PP_StorybookVines_Inst",
    "/Game/_PROJECT/04_Materials/PostProcess/M_PP_MeluColorGrade",
]


def build() -> str:
    import unreal
    atools = unreal.AssetToolsHelpers.get_asset_tools()
    fac = unreal.BlueprintFactory()
    fac.set_editor_property("parent_class", unreal.PostProcessVolume)
    path = f"{DIR}/BP_PPV_NikkiDream"
    if unreal.EditorAssetLibrary.does_asset_exist(path):
        bp = unreal.EditorAssetLibrary.load_asset(path)
    else:
        bp = atools.create_asset("BP_PPV_NikkiDream", DIR, unreal.Blueprint, fac)
    cdo = unreal.get_default_object(bp.generated_class())
    cdo.set_editor_property("unbound", True)
    cdo.set_editor_property("priority", 1.0)
    s = cdo.get_editor_property("settings")

    def ov(name, val):
        s.set_editor_property(f"override_{name}", True)
        s.set_editor_property(name, val)

    # --- bloom (your Dream Rim/Bloom/Halo emissive will bloom beautifully) ---
    ov("bloom_intensity", 0.7)
    # --- lens dreaminess ---
    ov("vignette_intensity", 0.35)
    ov("scene_fringe_intensity", 1.2)      # chromatic aberration
    ov("film_grain_intensity", 0.12)
    # --- gentle grade (leave exposure to UDS) ---
    ov("color_saturation", unreal.Vector4(1.05, 1.05, 1.08, 1.0))
    ov("color_contrast", unreal.Vector4(1.04, 1.04, 1.06, 1.0))
    # Shadows toward lavender/teal, highlights toward warm rose (Melusina):
    ov("color_gain_shadows", unreal.Vector4(0.96, 0.97, 1.04, 1.0))
    ov("color_gain_highlights", unreal.Vector4(1.04, 1.00, 0.98, 1.0))

    # --- blendables ---
    arr = []
    for mp in BLENDABLES:
        mm = unreal.EditorAssetLibrary.load_asset(mp)
        if mm:
            arr.append(unreal.WeightedBlendable(1.0, mm))
    s.set_editor_property("weighted_blendables", unreal.WeightedBlendables(arr))

    cdo.set_editor_property("settings", s)
    unreal.EditorAssetLibrary.save_asset(path, only_if_is_dirty=False)
    msg = f"BP_PPV_NikkiDream built | blendables={len(arr)} | unbound"
    print(msg)
    return msg


if __name__ == "__main__":
    build()
