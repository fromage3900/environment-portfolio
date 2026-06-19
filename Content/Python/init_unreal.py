"""UE editor startup: load Blender Live Link client and register menus."""
import importlib.util
import os
import sys

import unreal

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_OWNER = "BSGodFile_LiveLink"


def _py_path_prefix():
    project_python = _SCRIPT_DIR.replace("\\", "/")
    return (
        f"import sys; p=r'{project_python}'; "
        f"sys.path.insert(0,p) if p not in sys.path else None; "
        f"import livelink_unreal; "
    )


def register_livelink_menus():
    menus = unreal.ToolMenus.get()
    main = menus.find_menu("LevelEditor.MainMenu")
    if not main:
        unreal.log_warning("[LiveLink] LevelEditor.MainMenu not found")
        return

    for stale in (
        "LevelEditor.MainMenu.LiveLink.BlenderLiveLink",
        "LevelEditor.MainMenu.LiveLink",
    ):
        if menus.find_menu(stale):
            menus.remove_menu(stale)

    main.add_sub_menu(_OWNER, "LiveLink", "LiveLink", "LiveLink", "Live Link")
    live = menus.extend_menu("LevelEditor.MainMenu.LiveLink")
    live.add_sub_menu(
        _OWNER, "BlenderLiveLink", "BlenderLiveLink", "LiveLink", "Blender Live Link"
    )
    bl = menus.extend_menu("LevelEditor.MainMenu.LiveLink.BlenderLiveLink")

    prefix = _py_path_prefix()

    def add_entry(section, name, label, py_suffix):
        entry = unreal.ToolMenuEntry(name=name, type=unreal.MultiBlockType.MENU_ENTRY)
        entry.set_label(label)
        entry.set_string_command(
            type=unreal.ToolMenuStringCommandType.PYTHON,
            custom_type_name="",
            string=prefix + py_suffix,
        )
        bl.add_menu_entry(section, entry)

    add_entry("Connection", "StartLL", "Start Live Link", "livelink_unreal.start_connection()")
    add_entry("Connection", "StopLL", "Stop Live Link", "livelink_unreal.stop_connection()")
    add_entry(
        "Connection",
        "StatusLL",
        "Show Status",
        "unreal.log('[LiveLink] ' + livelink_unreal.get_status())",
    )

    dev = unreal.ToolMenuEntry(name="DeveloperLL", type=unreal.MultiBlockType.MENU_ENTRY)
    dev.set_label("Developer: Milad Kambari (3DRedbox Studio)")
    dev.set_string_command(
        type=unreal.ToolMenuStringCommandType.PYTHON,
        custom_type_name="",
        string="import webbrowser; webbrowser.open('https://www.artstation.com/milad_kambari')",
    )
    bl.add_menu_entry("Info", dev)

    menus.refresh_all_widgets()
    unreal.log("[LiveLink] Menu registered — LiveLink > Blender Live Link")


if _SCRIPT_DIR not in sys.path:
    sys.path.insert(0, _SCRIPT_DIR)

_pyc = os.path.join(_SCRIPT_DIR, "livelink_unreal.pyc")
_spec = importlib.util.spec_from_file_location("livelink_unreal", _pyc)
m = importlib.util.module_from_spec(_spec)
sys.modules["livelink_unreal"] = m
_spec.loader.exec_module(m)
m.register_menus = register_livelink_menus


def startup():
    if hasattr(m, "startup"):
        m.startup()
    else:
        register_livelink_menus()
    unreal.log(
        "[LiveLink] v3.1 loaded — no floating window; use "
        "LiveLink > Blender Live Link > Start Live Link (Blender server must run first)"
    )


def shutdown():
    if hasattr(m, "shutdown"):
        m.shutdown()
