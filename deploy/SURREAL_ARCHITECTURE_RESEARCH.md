# Surreal Architecture — Research & Overhaul Notes

**Version:** 2.66.11  
**Deploy:** `deploy/surreal_architecture_gen.py` + `deploy/surreal_arch/` + `deploy/surreal_greybox/`  
**Live:** copy all three to Blender 5.1 `scripts/addons/`

## v2.66 — UE trim pipeline + kit registration

| Feature | Module | Notes |
|---------|--------|-------|
| Trim vertex bake | `surreal_arch/trim_bake.py` | `trim_id` vertex color + face attribute for UE material assignment |
| Kit registration API | `surreal_arch/kit_registration.py` | `register_kit(monolith, arch_id, builder, snap_fn=...)` |
| Greybox extract | `surreal_greybox/primitives.py` | `_gb_box`, `_gb_join`, `_gb_bool_diff` bound at register |
| Workflow polls | `surreal_arch/workflow_polls.py` | BLOCKOUT hides experimental integration panels |

### New arch type
| Type | Research basis |
|------|----------------|
| `GB_ROMANESQUE_APSE` | Cistercian choir termination — semicircular recess shell, barrel vault cap, `apse_open` MUST_CONNECT snap |

### New room graphs
| Graph | Composition |
|-------|-------------|
| `ROMANESQUE_APSE` | Arcade → offset corridor → arcade → apse cap |
| `VENETIAN_CANAL` | Loggia → offset corridor → loggia → corridor (sottoportego rhythm) |
| `SCI_FI_DECK_EXPANSION` | Long corridor → T → airlock → command room → offset return |

## v2.65 — Research presets + style kits

### Research quick-launch (`surreal_arch/research_presets.py`)
| Preset | arch_type | Research basis |
|--------|-----------|----------------|
| Romanesque Cloister Arcade | `GB_ROMANESQUE_ARCADE` | Cistercian cloister — colonettes, round arch, barrel vault |
| Brutalist Pilotis Hall | `GREYBOX_PILLAR_HALL` | Le Corbusier pilotis + béton brut recess panels |
| Venetian Loggia Bay | `GB_VENETIAN_LOGGIA` | Venetian bifora rhythm + cornice shelf |
| Sci-Fi Pressure Door Airlock | `GB_SCIFI_PRESSURE_DOOR` | Gasket recess, frame offset, MUST_CONNECT door snap |

### Greybox kit types
| Type | Module |
|------|--------|
| `GB_CORRIDOR_OFFSET` | `greybox_offset.py` |
| `GB_ROMANESQUE_ARCADE` | `romanesque_kit.py` |
| `GB_BRUTALIST_PANEL_WALL` | `brutalist_kit.py` |
| `GB_VENETIAN_LOGGIA` | `venetian_kit.py` |
| `GB_SCIFI_PRESSURE_DOOR` | `scifi_kit.py` |
| `GB_GOTHIC_*` | `gothic_kit.py` |

## Trim group convention (UE)

Trim metadata on `obj['surreal_trim_groups']` maps to vertex color `trim_id` layer on bake:

| trim_id | Group | UE slot hint |
|---------|-------|--------------|
| 1 | wall_panel_recess | M_Trim_Panel_Recess |
| 15 | gasket_ring | M_Trim_Gasket |
| 8 | apse_shell | M_Trim_Apse_Shell |

Export sidecar JSON via **Export Snap JSON** or automatically on **Bake & Export UE5** (`<fbx>.snap.json`) includes snaps + trim_groups + `ue_export_hints` + optional **`gn_trim_zone_faces`** (evaluated mesh trim-zone count).

### GN trim face attrs (v2.66.9+)

- `trim:group_id` labels on `_gb_box` resolve to `surreal_trim_zone` (1-based) + `surreal_trim_id` face attributes before join
- `integration._wire_trim_box_wrapper` re-patches after `surreal_greybox.attach_all` so hot-reload keeps trim stamping
- **`gb_bake_trim_colors`**: bakes evaluated GN zones to CORNER layer `SURREAL_TRIM`; sidecar reports `trim_color_layer` + `trim_bake_mode: per_face_zones`

## Verify

```text
blender --background --python deploy/_mcp_verify_overhaul.py
```

Or MCP `execute_blender_code` with the same script.
