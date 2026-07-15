# Melodia ΓÇö Live Collaborative Environment Art Platform

UE 5.8 + Blender 5.1 production platform for stylized portfolio work: real-time BlenderΓåöUnreal level design bridge, procedural geometry generation, automatic material crosswalk, voice-driven NPCs, rhythm combat, and autonomous agent loops.

**≡ƒÜÇ New here? Start with [QUICKSTART.md](QUICKSTART.md) - Get running in 5 minutes!**

---

## ≡ƒÜÇ Quick Start: Choose Your Path

**≡ƒæï Welcome!** First, let's check your setup:

```powershell
≡ƒöº Run: .\deploy\validate_setup.ps1
```

This will check if you have the required tools installed. Then pick your onboarding path:

| Path | Time | What You'll Do | For |
|------|------|----------------|-----|
| ≡ƒöì **Viewer** | 5 min | Open & explore levels | Reviewers, new team members |
| ≡ƒÅù∩╕Å **Geometry** | 10 min | Build & send assets to UE | Level designers, environment artists |
| ≡ƒÄ¿ **Materials** | 15 min | Create & preview materials | Technical artists, shader folks |
| ≡ƒñ¥ **Full Collaborator** | 30 min | Complete live workflow | Active contributors |

---

## ≡ƒöì Path 1: Viewer Mode (5 min)

**Perfect for:** Exploring the project, reviewing levels, understanding the structure

### Step 1: Install Unreal Engine 5.8
```
Γ£à Download UE 5.8 from Epic Games Launcher
Γ£à Install to: C:\Program Files\Epic Games\UE_5.8\
```

### Step 2: Clone & Open Project
```bash
≡ƒôü Clone repo: git clone https://github.com/fromage3900/environment-portfolio.git
≡ƒôü Run: git lfs pull (for large assets)
≡ƒôé Open: BS_GodFile.uproject
ΓÅ│ Wait for shader compilation (first run takes 5-10 min)
```

### Step 3: Explore Levels
```
≡ƒÄ« Open these levels to explore:
Γö£ΓöÇΓöÇ /Game/Melodia/Levels/L_ZenForestTest (gameplay demo)
Γö£ΓöÇΓöÇ /Game/EnvSandbox/Levels/L_Template (neutral testing)
ΓööΓöÇΓöÇ /Game/EnvSandbox/Levels/WP/SakuraDream (World Partition demo)
```

### Step 4: Play the Demo
```
≡ƒÄ» In L_ZenForestTest:
Γö£ΓöÇΓöÇ Press Alt+P to Play
Γö£ΓöÇΓöÇ Use WASD to move
Γö£ΓöÇΓöÇ Walk into the trigger ΓåÆ rhythm battle!
ΓööΓöÇΓöÇ Complete 3 stages ΓåÆ win the demo
```

**≡ƒÄë Done!** You're now ready to explore the project.

---

## ≡ƒÅù∩╕Å Path 2: Geometry Designer (10 min)

**Perfect for:** Building levels, creating environments, blocking out spaces

### Step 1: Install Required Tools
```
Γ£à Unreal Engine 5.8 (from Viewer mode)
Γ£à Blender 5.1+ from: https://www.blender.org/download/
Γ£à Install to: C:\Program Files\Blender Foundation\Blender 5.1\
```

> **ΓÜí Lightweight clone (50 MB, not 300 GB):** You don't need the full UE project to design levels. Use sparse checkout to get just the Blender addon + scripts:
> ```powershell
> git clone --filter=blob:none --no-checkout https://github.com/fromage3900/environment-portfolio.git MelodiaCollab
> cd MelodiaCollab
> git sparse-checkout init --cone
> git sparse-checkout set deploy/surreal_arch deploy/surreal_world deploy/surreal_os Content/Python/gmm Content/Python/material_lib.py Content/Python/create_zunzun_bps.py Content/Python/import_zundamon.py Content/Python/resolve_material_crosswalk.py Tools Docs README.md
> git checkout
> ```
> Then copy `deploy/surreal_arch/` ΓåÆ Blender's addons folder. **[Full setup guide ΓåÆ](Docs/SETUP_COLLAB.md)**

### Step 2: Open Both Applications
```
≡ƒôé Open: BS_GodFile.uproject (Unreal)
≡ƒôé Open: WorkingMelusinaScene5.blend (Blender - or any .blend file)
```

### Step 3: Start the Live Bridge
```
≡ƒöº In Blender N-panel:
Γö£ΓöÇΓöÇ Press N to open side panel
Γö£ΓöÇΓöÇ Click "Melodia Studio" tab
Γö£ΓöÇΓöÇ Find "Live Bridge" section
ΓööΓöÇΓöÇ Click "Refresh Status"
```

You should see: `[Γ£ô] LiveLink   [ ] BL MCP   [Γ£ô] UE MCP`

### Step 4: Connect Blender Γåö Unreal
```
≡ƒöù In Blender Live Bridge:
Γö£ΓöÇΓöÇ Expand "LiveLink :9876"
Γö£ΓöÇΓöÇ Click "Start Server"
ΓööΓöÇΓöÇ Status changes to: CONNECTED Γ£à
```

### Step 5: Generate Your First Asset
```
≡ƒÄ¿ In Blender Melodia Studio:
Γö£ΓöÇΓöÇ Go to "Genome Carousel"
Γö£ΓöÇΓöÇ Pick a style (try "ZEN_SHRINE")
Γö£ΓöÇΓöÇ Click "Apply"
ΓööΓöÇΓöÇ Watch geometry appear! ≡ƒÄë
```

### Step 6: Send to Unreal
```
≡ƒôñ In Blender Live Bridge:
Γö£ΓöÇΓöÇ Click "Send + Materials"
ΓööΓöÇΓöÇ Check Unreal /Game/LiveLink/ folder
```

**Γ£¿ Success!** Your asset now appears in Unreal with correct materials!

### Step 7: Place in Level
```
≡ƒÄ« In Unreal:
Γö£ΓöÇΓöÇ Open /Game/EnvSandbox/Levels/L_Template
Γö£ΓöÇΓöÇ Find your asset in /Game/LiveLink/
Γö£ΓöÇΓöÇ Drag it into the viewport
ΓööΓöÇΓöÇ Position it where you want
```

**≡ƒÄë Done!** You can now build and stream geometry live to Unreal!

---

## ≡ƒÄ¿ Path 3: Material Designer (15 min)

**Perfect for:** Creating materials, testing shaders, look development

### Step 1: Complete Viewer Mode
```
Γ£à Finish Path 1 (Viewer Mode) first
```

### Step 2: Open Material Test Level
```
≡ƒÄ« Open: /Game/EnvSandbox/Levels/L_Template
```

### Step 3: Explore Master Materials
```
≡ƒÄ¿ In Content Browser, find:
Γö£ΓöÇΓöÇ /Game/EnvSandbox/Materials/Masters/M_Master_Toon_Universal
Γö£ΓöÇΓöÇ /Game/EnvSandbox/Materials/Masters/M_Master_Toon_Landscape_HeightBlend
ΓööΓöÇΓöÇ /Game/EnvSandbox/Materials/Masters/M_Water_Master_Grand_v6
```

### Step 4: Create Material Instance
```
≡ƒöº Right-click any master material:
Γö£ΓöÇΓöÇ Select "Create Material Instance"
Γö£ΓöÇΓöÇ Name it: MI_Test_MyMaterial
ΓööΓöÇΓöÇ Double-click to edit parameters
```

### Step 5: Test Your Material
```
≡ƒÄ« In the level:
Γö£ΓöÇΓöÇ Create a cube or sphere
Γö£ΓöÇΓöÇ Apply your material instance
Γö£ΓöÇΓöÇ Adjust parameters in real-time
ΓööΓöÇΓöÇ See changes instantly! Γ£¿
```

### Step 6: Use Material Preview Script
```python
≡ƒô£ In Unreal Python console (Window ΓåÆ Developer Tools ΓåÆ Python Editor):
import capture_material_grid
capture_material_grid.capture_material("/Game/EnvSandbox/Materials/Instances/MI_Test_MyMaterial")
```

**≡ƒÄë Done!** You can now create and test materials efficiently!

---

## ≡ƒñ¥ Path 4: Full Collaborator (30 min)

**Perfect for:** Active contributors, team members, production work

### Step 1: Complete Previous Paths
```
Γ£à Finish Paths 1, 2, and 3 first
```

### Step 2: Install VOICEVOX (for NPCs)
```
≡ƒÄñ Download VOICEVOX: https://voicevox.hiroshiba.jp/
≡ƒôü Install to: G:\programs\VOICEVOX\
≡ƒÜÇ Launch VOICEVOX.exe
Γ£à Verify: curl http://127.0.0.1:50021/version
```

### Step 3: Generate NPC Voices
```powershell
≡ƒô£ In terminal:
cd G:\EnvironmentPortfolio\BS_GodFile\Tools
$env:PYTHONIOENCODING = "utf-8"
python generate_all_voices.py
```

This creates **102 voice files** for 7 characters! ≡ƒÄÖ∩╕Å

### Step 4: Create NPC Blueprints
```python
≡ƒô£ In Unreal Python console:
import create_zunzun_bps
create_zunzun_bps.run()
```

This creates 7 NPC Blueprints + quest data! ≡ƒñû

### Step 5: Enable Live Sync (Optional)
```
≡ƒöä In Blender Live Bridge:
Γö£ΓöÇΓöÇ Toggle "Live Sync ON"
ΓööΓöÇΓöÇ Every change streams to Unreal automatically!
```

### Step 6: Test Full Workflow
```
≡ƒÄ« Open: /Game/Melodia/Levels/L_ZenForestTest
≡ƒÄ» Press Alt+P to Play
ΓÜö∩╕Å Walk into trigger ΓåÆ rhythm battle with voiced NPCs!
≡ƒÅå Complete the dungeon ΓåÆ full demo experience!
```

**≡ƒÄë Done!** You're now a full collaborator!

---

## ≡ƒåÿ Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| ≡ƒö┤ Port 9876 "in use" | Close extra Blender instances (Task Manager) |
| ≡ƒö┤ Materials look gray | Run: `import resolve_material_crosswalk; resolve_material_crosswalk.resolve_all()` |
| ≡ƒö┤ VOICEVOX speaker missing | Open VOICEVOX ΓåÆ Settings ΓåÆ Manage Voice Libraries ΓåÆ download |
| ≡ƒö┤ Unreal crashes on play | Rebuild MelodiaCore plugin (Tools ΓåÆ Refresh Visual Studio Project) |
| ≡ƒö┤ Can't find Melodia Studio tab | Reload SurrealArch addon in Blender |

---

## ≡ƒôÜ Next Steps

**≡ƒôû For Level Designers:**
- [Docs/LEVEL_DESIGNER_ONBOARDING.md](Docs/LEVEL_DESIGNER_ONBOARDING.md) - Deep dive into level design workflow
- [Docs/COLLABORATION_WORKFLOW.md](Docs/COLLABORATION_WORKFLOW.md) - Git handoff rules

**≡ƒôû For Technical Artists:**
- [MATERIAL_LOOKDEV_PIPELINE.md](MATERIAL_LOOKDEV_PIPELINE.md) - Material creation workflow
- [Docs/MATERIAL_INTEGRATION.md](Docs/MATERIAL_INTEGRATION.md) - Material integration guide

**≡ƒôû For Programmers:**
- [AGENT_OPERATING_MODEL.md](AGENT_OPERATING_MODEL.md) - Agent system overview
- [AGENTS.md](AGENTS.md) - Multi-agent framework details

**≡ƒôû Full Documentation:**
- [DOC_INDEX.md](DOC_INDEX.md) - Complete documentation map

---

### Step 1 ΓÇö Verify the bridge ports

<table>
<tr><td><b>UE MCP</b></td><td><code>curl http://127.0.0.1:9316/health</code></td><td>ΓåÆ <code>{"status":"ok","tools_registered":1325}</code></td></tr>
<tr><td><b>LiveLink</b></td><td colspan="2">Blender N-panel ΓåÆ Melodia Studio ΓåÆ <b>Live Bridge</b> ΓåÆ <b>Refresh Status</b></td></tr>
<tr><td><b>VOICEVOX</b></td><td><code>curl http://127.0.0.1:50021/version</code></td><td>ΓåÆ <code>"0.25.2"</code></td></tr>
</table>

---

### Step 2 ΓÇö Start the LiveLink server

```
Blender N-panel ΓåÆ Melodia Studio ΓåÆ Live Bridge ΓåÆ LiveLink :9876 ΓåÆ [Start Server]
```

Status changes to **CONNECTED**. The server now accepts FBX streams from Blender and pushes to UE.

---

### Step 3 ΓÇö Generate & send your first asset

```
ΓöîΓöÇ Blender ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÉ
Γöé                                                    Γöé
Γöé  1. Genome Carousel ΓåÆ pick ZEN_SHRINE ΓåÆ [Apply]    Γöé
Γöé  2. Material Bridge ΓåÆ [Scan Slots] ΓåÆ [Auto-Match]  Γöé
Γöé  3. Live Bridge ΓåÆ [Send + Materials]                Γöé
Γöé                                                    Γöé
Γöé  (toggle Live Sync ON for continuous streaming)     Γöé
ΓööΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÿ
                          Γöé
                          Γû╝  FBX + textures + material paths
ΓöîΓöÇ Unreal ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÉ
Γöé                                                    Γöé
Γöé  Assets appear at  /Game/LiveLink/                 Γöé
Γöé  Material slots auto-resolved via .material_map.jsonΓöé
Γöé  Drag into viewport ΓåÆ geometry is in-level          Γöé
ΓööΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÿ
```

---

### Step 4 ΓÇö Generate NPC voices

```powershell
cd Tools
$env:PYTHONIOENCODING = "utf-8"
python generate_all_voices.py
```

**102 WAV files** across 7 characters (Zundamon, Zunko, Kiritan, Itako, Metan, Sora, Tsurugi). Speaker IDs: `3, 14, 5, 6, 2, 16, 17`.

---

### Step 5 ΓÇö Create NPC Blueprints (Unreal Python console)

```python
import create_zunzun_bps; create_zunzun_bps.run()
```

Creates: 7 `BP_*_NPC` Blueprints, 4 shop DataAssets, 4 quest DataTables, 7 party member DataAssets.

---

### Step 6 ΓÇö Playtest the vertical slice

```
Open: /Game/Melodia/Levels/L_ZenForestTest
Hit:  Alt+P

  Walk ΓåÆ encounter trigger ΓåÆ rhythm battle ΓåÆ reward choice
  ΓåÆ room exit ΓåÆ next stage ΓåÆ 3-stage dungeon ΓåÆ Sir Melodious reunion
```

| Key | Action |
|-----|--------|
| WASD | Move |
| 1/2/3/4 | Elemental lanes |
| Q | Basic attack |
| Space | Dodge |

---

### Step 7 ΓÇö Material post-import fix (if needed)

```python
# UE Python ΓÇö auto-applies .material_map.json crosswalk to all imported meshes
import resolve_material_crosswalk; resolve_material_crosswalk.resolve_all()
```

---

### Two-designer workflow

| Role | Tool | Responsibility |
|------|------|---------------|
| **Geometry Designer** | Blender | Procedural gen, mesh editing, materials, live sync |
| **Level Scripter** | Unreal | Blueprints, encounters, lighting, PCG scatter, NPCs |

Live sync ON ΓåÆ Geometry Designer tweaks ΓåÆ UE updates automatically ΓåÆ Scripter places gameplay.

---

### Port map

| Port | Service | Direction |
|------|---------|-----------|
| `9876` | LiveLink ΓÇö FBX/texture/animation stream | Blender ΓåÆ UE |
| `9316` | UE Monolith MCP ΓÇö Python execution (1,325 tools) | Any ΓåÆ UE |
| `9317` | Blender MCP ΓÇö genome/agent control | Any ΓåÆ Blender |
| `50021` | VOICEVOX ΓÇö TTS (7 characters) | Any ΓåÆ VOICEVOX |
| `50022` | Melusina Voice ΓÇö custom SBV2 | Any ΓåÆ Melusina |

---

### Troubleshooting quick-fix

| Problem | Fix |
|---------|-----|
| Port 9876 "in use" | Close extra Blender instances (Task Manager) |
| Materials gray in UE | `resolve_material_crosswalk.resolve_all()` |
| Speaker not found in VOICEVOX | Settings ΓåÆ Manage Voice Libraries ΓåÆ download |
| PIE crash on encounter | Rebuild MelodiaCore (.dll) |

---

### Key scripts

| Script | Does | Where |
|--------|------|-------|
| `Tools/setup_zunzun_studio.py` | Import all ZunZun models + studio layout | Blender |
| `Tools/generate_all_voices.py` | Batch-generate 102 NPC voice WAVs | Terminal |
| `Content/Python/import_zundamon.py` | Import Zundamon FBX + materials | UE |
| `Content/Python/create_zunzun_bps.py` | Auto-create 7 NPC BPs + quests/shop/party | UE |
| `Content/Python/resolve_material_crosswalk.py` | Post-import material auto-resolver | UE |
| `deploy/deploy_all.ps1` | Launch all 11 agent loops | Terminal |

---

Full guide with voice server setup, UE MCP commands, and Material Maker pipeline: **[Docs/ONBOARDING_LIVE_COLLAB.md](Docs/ONBOARDING_LIVE_COLLAB.md)**

---

## Current Focus

- Universal material/look-dev workflow centered on `M_Master_Toon_Universal`, `M_Master_Toon_Landscape_HeightBlend`, and `M_Water_Master_Grand_v6`.
- **SDF Material Factory**: 32 Substrate Toon SDF instances across cathedral, cosmo, and landscape families. 24/7 Ollama-powered autonomous generation loop. [Docs/SDF_FACTORY.md](Docs/SDF_FACTORY.md)
- **WP Pillar Levels**: 4 World Partition environments (SakuraDream, SpaceCathedral, BaroqueGrotto, CosmicOrrery) ΓÇö production-ready as of 2026-07-09: WP verified, distinct per-pillar displaced terrain, live-verified PCG scatter (2015/642/1085/6171 instances). Rebuild/verify via `setup_wp_pillar_levels.py` (kick + `--verify` in separate calls).
- **24/7 Agent Grid**: 11 autonomous deployable loops with start/stop dashboard. `deploy_all.ps1` launches everything.
- Generic `L_Template` look-dev stage for material, landscape, water, trimsheet, and PCG proof.
- Portfolio package generation from existing manifests and captures.

## Start Here

**≡ƒÜÇ New Users:**
- [QUICKSTART.md](QUICKSTART.md) - **Start here!** Get running in 5 minutes
- [README.md](README.md) - **This file** - Choose your onboarding path

**≡ƒôû Documentation:**
- [DOC_INDEX.md](DOC_INDEX.md) ΓÇö documentation map and source-of-truth list.
- [CURRENT_STATE.md](CURRENT_STATE.md) - implemented, partial, broken, planned, and research systems.

**≡ƒöº Workflows:**
- [UNIVERSAL_ENVIRONMENT_PIPELINE.md](UNIVERSAL_ENVIRONMENT_PIPELINE.md) - generic production flow.
- [MATERIAL_LOOKDEV_PIPELINE.md](MATERIAL_LOOKDEV_PIPELINE.md) - material and look-dev workflow.
- [AGENT_OPERATING_MODEL.md](AGENT_OPERATING_MODEL.md) - recursive agent roles and safety lanes.

**≡ƒæÑ Collaboration:**
- [Docs/LEVEL_DESIGNER_ONBOARDING.md](Docs/LEVEL_DESIGNER_ONBOARDING.md) - five-minute level-design workflow and validation.
- [Docs/COLLABORATION_WORKFLOW.md](Docs/COLLABORATION_WORKFLOW.md) - Git/LFS lanes and editor handoff rules.

**≡ƒôè Status:**
- [PORTFOLIO_READINESS.md](PORTFOLIO_READINESS.md) - readiness checklist, excluding Sakura art-pass ownership.
- [Docs/REPORTS/MELODIA_CONSOLIDATION_2026-07-13.md](Docs/REPORTS/MELODIA_CONSOLIDATION_2026-07-13.md) - current verified/partial/not-started handoff.

## Key Systems

- Material architecture: [MATERIAL_PIPELINE.md](MATERIAL_PIPELINE.md)
- Material review: [MATERIAL_SYSTEM_REVIEW.md](MATERIAL_SYSTEM_REVIEW.md)
- Node tree review: [Docs/MATERIAL_NODE_TREE_REVIEW.md](Docs/MATERIAL_NODE_TREE_REVIEW.md)
- Material integration runbook: [Docs/MATERIAL_INTEGRATION.md](Docs/MATERIAL_INTEGRATION.md)
- Portfolio deep review (current truth): [Docs/PROJECT_DEEP_REVIEW_2026-07-08.md](Docs/PROJECT_DEEP_REVIEW_2026-07-08.md)
- Ecosystem unification (PCG + materials, long-term): [Docs/ECOSYSTEM_UNIFICATION_PLAN.md](Docs/ECOSYSTEM_UNIFICATION_PLAN.md)
- Agent ownership: [AGENTS.md](AGENTS.md), [AGENT_BOUNDARIES.md](AGENT_BOUNDARIES.md), [AGENT_OWNERSHIP.md](AGENT_OWNERSHIP.md)

## Generic Package Flow

```text
Material/PCG/world systems
  -> L_Template or neutral test map validation
  -> Saved/Portfolio render and metadata fragments
  -> renders_manifest.json
  -> portfolio_package.json
  -> website / Figma / ArtStation handoff metadata
```

## 24/7 Agent Grid

11 autonomous loops managed by a unified deploy system:

```powershell
.\deploy\deploy_all.ps1     # Launch all 11 loops
.\deploy\stop_all.ps1       # Graceful shutdown
.\deploy\loop_status.ps1    # Live dashboard (PID/state per loop)
```

**Blender-side (4):** surreal_micro10, surreal_micro2, surreal_tierb, world_micro10
**UE Python (6):** material_aaa, master_texture, portfolio_orch, specialist_pcg, specialist_terrain, sdf_factory
**Meta (1):** recursive_learner

## SDF Material Catalog

32 Substrate Toon instances parented to `M_Toon_SDF` + `M_Master_SDF_Toon`:

| Family | Count | Examples |
|--------|-------|----------|
| Cathedral/Gothic | 8 | RoseWindow_Radial, GildedTracery_Arched, Altar_GoldFiligree |
| Cosmo/Atmospheric | 6 | Starfield_Dust, Nebula_Veil, Aurora_Band |
| Landscape | 6 | Terrain_Crystal, Grass_Weave, Sand_Leafcool |
| Stylized | 6 | RosyQuartz, CelestialVinyl, TealCeramic, VoidStarlight |
| Base | 5 | Wall, Floor, Accent, Rim, Ornamental |

Nikki-reviewed: 6 drop-in ready, 16 adaptable with parameter tuning.
See [NEXT_HIGHEST_LEVERAGE_TASK.md](NEXT_HIGHEST_LEVERAGE_TASK.md) for the Nikki scorecard.

Do not automate final Sakura level art direction. `L_SakuraPath` is a human-owned art pass. The platform may provide capture tools, material manifests, PCG standards, and generic look-dev support, but it should not replace the human composition pass.
