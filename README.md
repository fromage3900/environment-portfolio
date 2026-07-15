# Melodia -- Live Collaborative Environment Art Platform

```
✧ ┊ ⋆ ┊ . ┊ ┊┊ ┊⋆ ┊ .┊ ┊ ⋆˚  ✧  ┊ ┊ ⋆ ┊ . ┊ ┊┊ ┊⋆ ┊ .┊ ┊ ⋆˚  ✧
```

UE 5.8 + Blender 5.1 production platform for real-time Blender <-> Unreal level design, procedural geometry generation, automatic material crosswalk, voice-driven NPCs, rhythm combat, and autonomous agent pipelines.

```
 ◇─◇──◇──◇─◇
```

> **New here?** [QUICKSTART.md](QUICKSTART.md) -- 5 minutes to first demo.
>
> **Level designer?** [Sparse checkout guide](Docs/SETUP_COLLAB.md) -- 50 MB clone, not 300 GB.
>
> **Architecture overview?** [PIPELINE.md](PIPELINE.md) -- full system map.

```
 ◇─◇──◇──◇─◇
```

---

## Onboarding Paths

```
┊ ⋆ ┊ . ┊ ┊┊ ┊⋆ ┊ .┊ ┊
```

| Path | Time | What You'll Do | For |
|------|------|----------------|-----|
| **Viewer** | 5 min | Open & explore levels | Reviewers, new team members |
| **Geometry** | 10 min | Build & send assets to UE | Level designers, environment artists |
| **Materials** | 15 min | Create & preview materials | Technical artists, shader folks |
| **Full Collaborator** | 30 min | Complete live workflow | Active contributors |

```
┊ ⋆ ┊ . ┊ ┊┊ ┊⋆ ┊ .┊ ┊
```

Run setup check: `.\deploy\validate_setup.ps1`

---

## Path 1: Viewer Mode (5 min)

```
◇─── Viewer ───◇
```

**Step 1** -- Install Unreal Engine 5.8 from Epic Games Launcher.

**Step 2** -- Clone & Open:

```bash
git clone https://github.com/fromage3900/environment-portfolio.git
git lfs pull
# Open BS_GodFile.uproject -- wait for shader compilation (5-10 min first run)
```

**Step 3** -- Explore:

```
/Game/Melodia/Levels/L_ZenForestTest        (gameplay demo)
/Game/EnvSandbox/Levels/L_Template          (neutral testing)
/Game/EnvSandbox/Environments/WP/L_WP_SakuraDream  (World Partition)
```

**Step 4** -- Play: Open `L_ZenForestTest` -> `Alt+P` -> walk into trigger -> rhythm battle -> 3 stages -> win.

```
◇──◇──◇──◇─◇
```

---

## Path 2: Geometry Designer (10 min)

```
◇─── Geometry ───◇
```

**Step 1** -- Install Blender 5.1+ from [blender.org](https://www.blender.org/).

> **Lightweight clone (50 MB):** You don't need the full UE project.
> ```powershell
> git clone --filter=blob:none --no-checkout https://github.com/fromage3900/environment-portfolio.git MelodiaCollab
> cd MelodiaCollab
> git sparse-checkout init --cone
> git sparse-checkout set deploy/surreal_arch deploy/surreal_world deploy/surreal_os Content/Python/gmm Content/Python/material_lib.py Content/Python/create_zunzun_bps.py Content/Python/import_zundamon.py Content/Python/resolve_material_crosswalk.py Tools Docs README.md
> git checkout
> ```
> Copy `deploy/surreal_arch/` to Blender's addons folder. [Full guide](Docs/SETUP_COLLAB.md)

**Step 2** -- Open both: `BS_GodFile.uproject` (Unreal) + any `.blend` (Blender).

**Step 3** -- Bridge: Blender `N`-panel -> Melodia Studio tab -> **Live Bridge** -> **Refresh Status**.

**Step 4** -- Connect: Expand "LiveLink :9876" -> **Start Server**.

**Step 5** -- Generate: Genome Carousel -> pick style -> **Apply**.

**Step 6** -- Send: Material Bridge -> Scan Slots -> Auto-Match -> **Send + Materials**.

**Step 7** -- In Unreal: `/Game/LiveLink/` -> drag into viewport.

```
◇──◇──◇──◇─◇
```

---

## Path 3: Material Designer (15 min)

```
◇─── Materials ───◇
```

**Step 1** -- Finish Path 1 first.

**Step 2** -- Open `/Game/EnvSandbox/Levels/L_Template`.

**Step 3** -- Master materials at `/Game/EnvSandbox/Materials/Masters/`:

```
M_Master_Toon_Universal
M_Master_Toon_Landscape_HeightBlend
M_Water_Master_Grand_v6
```

**Step 4** -- Right-click any master -> Create Material Instance -> edit parameters.

**Step 5** -- Apply to test object, adjust in real-time.

**Step 6** -- UE Python console:

```python
import capture_material_grid
capture_material_grid.capture_material("/Game/EnvSandbox/Materials/Instances/MI_Test_MyMaterial")
```

```
◇──◇──◇──◇─◇
```

---

## Path 4: Full Collaborator (30 min)

```
◇─── Full Collab ───◇
```

**Step 1** -- Complete Paths 1, 2, and 3 first.

**Step 2** -- Install [VOICEVOX](https://voicevox.hiroshiba.jp/). Launch, verify:
```powershell
curl http://127.0.0.1:50021/version
```

**Step 3** -- Generate NPC voices:
```powershell
cd G:\EnvironmentPortfolio\BS_GodFile\Tools
$env:PYTHONIOENCODING = "utf-8"
python generate_all_voices.py
```
-> 102 voice files for 7 characters.

**Step 4** -- Create NPC Blueprints (UE Python console):
```python
import create_zunzun_bps; create_zunzun_bps.run()
```

**Step 5** -- Enable Live Sync (Blender Live Bridge -> toggle "Live Sync ON").

**Step 6** -- Full test: Open `L_ZenForestTest`, `Alt+P`, walk into trigger -> rhythm battle -> dungeon clear.

```
◇──◇──◇──◇─◇
```

---

## Live Bridge

```
◇─── Bridge ───◇
```

### Port health

| Service | Check |
|---------|-------|
| **UE MCP** | `curl http://127.0.0.1:9316/health` -> `{"status":"ok","tools_registered":1325}` |
| **LiveLink** | Blender N-panel -> Melodia Studio -> Live Bridge -> Refresh Status |
| **VOICEVOX** | `curl http://127.0.0.1:50021/version` -> `"0.25.2"` |
| **Melusina** | `curl http://127.0.0.1:50022/version` -> `{"version":"melusina-1.0"}` |

### Port map

| Port | Service | Direction |
|------|---------|-----------|
| `9876` | LiveLink -- FBX/texture/animation stream | Blender -> UE |
| `9316` | UE Monolith MCP -- Python execution (1,325 tools) | Any -> UE |
| `9317` | Blender MCP -- genome/agent control | Any -> Blender |
| `50021` | VOICEVOX -- TTS (7 characters) | Any -> VOICEVOX |
| `50022` | Melusina Voice -- custom SBV2 | Any -> Melusina |

### Troubleshooting

| Problem | Fix |
|---------|-----|
| Port 9876 "in use" | Close extra Blender instances (Task Manager) |
| Materials gray in UE | `resolve_material_crosswalk.resolve_all()` |
| Speaker not found | VOICEVOX Settings -> Manage Voice Libraries -> download |
| PIE crash | Rebuild MelodiaCore (.dll) |

### Key scripts

| Script | Does | Where |
|--------|------|-------|
| `Tools/setup_zunzun_studio.py` | Import ZunZun models + studio layout | Blender |
| `Tools/generate_all_voices.py` | Batch-generate 102 NPC voice WAVs | Terminal |
| `Content/Python/import_zundamon.py` | Import Zundamon FBX + materials | UE |
| `Content/Python/create_zunzun_bps.py` | Auto-create 7 NPC BPs + quests/shop/party | UE |
| `Content/Python/resolve_material_crosswalk.py` | Post-import material auto-resolver | UE |
| `deploy/deploy_all.ps1` | Launch all 11 agent loops | Terminal |

### Two-designer workflow

| Role | Tool | Responsibility |
|------|------|---------------|
| **Geometry Designer** | Blender | Procedural gen, mesh editing, materials, live sync |
| **Level Scripter** | Unreal | Blueprints, encounters, lighting, PCG scatter, NPCs |

Live sync ON -> Designer tweaks -> UE auto-updates -> Scripter places gameplay.

Full guide: [Docs/ONBOARDING_LIVE_COLLAB.md](Docs/ONBOARDING_LIVE_COLLAB.md)

```
◇──◇──◇──◇─◇
```

---

## Documentation

```
◇─── Docs ───◇
```

**Getting started:**
- [QUICKSTART.md](QUICKSTART.md) -- 5-minute setup
- [DOC_INDEX.md](DOC_INDEX.md) -- complete documentation map (68 docs)
- [PIPELINE.md](PIPELINE.md) -- unified pipeline architecture
- [CURRENT_STATE.md](CURRENT_STATE.md) -- system readiness

**Workflows:**
- [UNIVERSAL_ENVIRONMENT_PIPELINE.md](UNIVERSAL_ENVIRONMENT_PIPELINE.md) -- production flow
- [MATERIAL_LOOKDEV_PIPELINE.md](MATERIAL_LOOKDEV_PIPELINE.md) -- material & look-dev
- [AGENT_OPERATING_MODEL.md](AGENT_OPERATING_MODEL.md) -- agent roles & safety

**Collaboration:**
- [Docs/SETUP_COLLAB.md](Docs/SETUP_COLLAB.md) -- lightweight collab setup (50 MB)
- [Docs/ONBOARDING_LIVE_COLLAB.md](Docs/ONBOARDING_LIVE_COLLAB.md) -- full step-by-step guide
- [Docs/LEVEL_DESIGNER_ONBOARDING.md](Docs/LEVEL_DESIGNER_ONBOARDING.md) -- level design workflow
- [Docs/COLLABORATION_WORKFLOW.md](Docs/COLLABORATION_WORKFLOW.md) -- Git/LFS handoff rules

**Status:**
- [PORTFOLIO_READINESS.md](PORTFOLIO_READINESS.md) -- readiness checklist
- [Docs/REPORTS/MELODIA_CONSOLIDATION_2026-07-13.md](Docs/REPORTS/MELODIA_CONSOLIDATION_2026-07-13.md) -- verified/partial/not-started

```
◇──◇──◇──◇─◇
```

---

## Systems

```
◇─── Systems ───◇
```

**Materials:** [PIPELINE](MATERIAL_PIPELINE.md) / [Review](MATERIAL_SYSTEM_REVIEW.md) / [Integration](Docs/MATERIAL_INTEGRATION.md) / [Node Tree](Docs/MATERIAL_NODE_TREE_REVIEW.md) / [Unification](Docs/ECOSYSTEM_UNIFICATION_PLAN.md)

**Portfolio:** [Deep Review](Docs/PROJECT_DEEP_REVIEW_2026-07-08.md)

**Agents:** [Framework](AGENTS.md) / [Boundaries](AGENT_BOUNDARIES.md) / [Ownership](AGENT_OWNERSHIP.md)

**Pipeline:**
```
Material/PCG/world systems
  -> L_Template or neutral test map validation
  -> Saved/Portfolio render and metadata fragments
  -> renders_manifest.json
  -> portfolio_package.json
  -> website / Figma / ArtStation handoff
```

**24/7 Agent Grid:**
```powershell
.\deploy\deploy_all.ps1     # Launch all 11 loops
.\deploy\stop_all.ps1       # Graceful shutdown
.\deploy\loop_status.ps1    # Live dashboard (PID/state per loop)
```
Blender-side (4): surreal_micro10, surreal_micro2, surreal_tierb, world_micro10
UE Python (6): material_aaa, master_texture, portfolio_orch, specialist_pcg, specialist_terrain, sdf_factory
Meta (1): recursive_learner

**SDF Material Catalog:** 32 Substrate Toon instances across Cathedral/Gothic (8), Cosmo (6), Landscape (6), Stylized (6), Base (5). 6 drop-in ready, 16 adaptable. [Scorecard](NEXT_HIGHEST_LEVERAGE_TASK.md)

```
◇──◇──◇──◇─◇
```

```
✧ ┊ ⋆ ┊ . ┊ ┊┊ ┊⋆ ┊ .┊ ┊ ⋆˚  ✧  ┊ ┊ ⋆ ┊ . ┊ ┊┊ ┊⋆ ┊ .┊ ┊ ⋆˚  ✧
```

**Boundary:** Do not automate final Sakura level art direction. `L_SakuraPath` is human-owned.
