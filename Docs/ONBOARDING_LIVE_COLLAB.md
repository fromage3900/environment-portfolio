# Live Collaborative Level Designer ΓÇö Step-by-Step Onboarding

> **Goal:** Get two designers building levels together ΓÇö one in Blender, one in Unreal ΓÇö with live streaming, automatic materials, voiced NPCs, and rhythm combat. **Time to first live sync: ~10 minutes.**

---

## Prerequisites

| Tool | Version | Path / Source |
|------|---------|---------------|
| Unreal Engine 5 | 5.8 | `C:\Program Files\Epic Games\UE_5.8\` |
| Blender | 5.1+ | `C:\Program Files\Blender Foundation\Blender 5.1\` |
| VOICEVOX | 0.25+ | [voicevox.hiroshiba.jp](https://voicevox.hiroshiba.jp/) |
| Material Maker | 1.7 | `G:\programs\MaterialMaker\` |

**Required Blender addons** (pre-installed):
- SurrealArch (Melodia Studio) ΓÇö procedural generation, live bridge, material bridge
- VRM Importer v4.4 ΓÇö character model import
- LiveLink v3.3 ΓÇö FBX streaming to Unreal

**Unreal project:** `G:\EnvironmentPortfolio\BS_GodFile\BS_GodFile.uproject`

---

## Step 1 ΓÇö Launch (3 min)

### 1a. Open Unreal
```
Open: BS_GodFile.uproject
Wait for shader compilation and Monolith MCP startup.
```

Verify the UE MCP is running:
```powershell
curl http://127.0.0.1:9316/health
# ΓåÆ {"status":"ok","port":9316,"tools_registered":1325}
```

### 1b. Open Blender
```
Open: WorkingMelusinaScene5.blend (or any .blend with SurrealArch addon loaded)
```

In the 3D Viewport, press `N` to open the **N-panel**. Switch to the **Melodia Studio** tab.

### 1c. Close Extra Blender Instances
```powershell
# Check: Task Manager ΓåÆ sort by Name ΓåÆ find blender.exe
# Only ONE Blender should be open. Multiple instances will conflict on port 9876.
```

---

## Step 2 ΓÇö Start the Bridge (2 min)

### 2a. Open the Live Bridge Panel
N-panel ΓåÆ **Melodia Studio** ΓåÆ **Live Bridge** (nested under the genome carousel, `bl_order=15`).

Click **Refresh Status** ΓÇö you should see:

```
[Γ£ô] LiveLink   [ ] BL MCP   [Γ£ô] UE MCP
```

If `BL MCP` shows offline, don't worry ΓÇö it's optional for this workflow. The important ones are LiveLink and UE MCP.

### 2b. Start the LiveLink Server
Expand **LiveLink :9876** ΓåÆ Click **Start Server**.

Status changes to `CONNECTED`. The LiveLink server is now listening for UE to connect.

### 2c. Start VOICEVOX (Terminal)
```powershell
& "G:\programs\VOICEVOX\VOICEVOX\VOICEVOX.exe"
```
The engine starts on port `:50021`. Verify:
```powershell
curl http://127.0.0.1:50021/version
# ΓåÆ "0.25.2"
```

---

## Step 3 ΓÇö First Live Export (3 min)

### 3a. Generate Geometry (Blender)
N-panel ΓåÆ **Melodia Studio** ΓåÆ **Genome Carousel**

Pick a style (e.g. `ZEN_SHRINE`, `CASTLE_TOWER`, `GOTHIC_CATHEDRAL`) and click **Apply**.

### 3b. Set Up Materials
N-panel ΓåÆ **Material Bridge**:
1. Select your generated object
2. Click **Scan Slots** ΓÇö lists all material slots
3. Click **Auto-Match** ΓÇö fuzzy-matches to UE material catalog
4. Review and click **Save Map** (persists as `.material_map.json`)

### 3c. Send to Unreal
N-panel ΓåÆ **Live Bridge** ΓåÆ **Quick Actions**:
- Click **Send + Materials** ΓÇö auto-crosswalks materials then streams FBX + textures to UE
- **Or** toggle **Live Sync ON** ΓÇö every change in Blender automatically streams to UE

In Unreal, imported assets appear under `/Game/LiveLink/`.

### 3d. Verify in UE
Open `/Game/LiveLink/` in the Content Browser ΓÇö your geometry with correct materials should be there. Drag it into the viewport to see it in-level.

---

## Step 4 ΓÇö Collaborative Workflow (ongoing)

### Roles

| Designer | Tool | What They Do |
|----------|------|-------------|
| **Geometry Designer** | Blender | Procedural generation, mesh editing, material assignment, live sync |
| **Level Scripter** | Unreal | Blueprint placement, encounter triggers, lighting, PCG scatter, NPCs |

### Live Handoff Loop
1. Geometry Designer builds in Blender ΓåÆ hits **Live Sync ON**
2. Level Scripter sees new geometry in `/Game/LiveLink/`
3. Scripter places encounters, NPCs, PCG around it
4. Designer tweaks geometry ΓåÆ changes stream live ΓåÆ Scripter sees updates in seconds
5. Material paths auto-apply via the crosswalk ΓÇö no manual reassignment

### UE Remote Control (MCP)
From Blender or any HTTP client, execute Python in UE:

```json
POST http://127.0.0.1:9316/mcp
{
  "jsonrpc": "2.0", "id": 1,
  "method": "tools/call",
  "params": {
    "name": "editor_query",
    "arguments": {"action": "load_level", "level_path": "/Game/Melodia/Levels/L_ZenForestTest"}
  }
}
```

---

## Step 5 ΓÇö NPCs & Voice (2 min after models imported)

### 5a. Generate Voice Lines
```powershell
cd G:\EnvironmentPortfolio\BS_GodFile\Tools
$env:PYTHONIOENCODING = "utf-8"
python generate_all_voices.py
# ΓåÆ 102 WAVs across 7 characters
```

### 5b. Create NPC Blueprints (in UE Python console)
```python
import create_zunzun_bps
create_zunzun_bps.run()
# ΓåÆ Creates 7 BP_*_NPC + quest tables + shop data + party stats
```

### 5c. Voice Speaker Reference
| Character | VOICEVOX ID | Role |
|-----------|-------------|------|
| Zundamon | `3` | Questkeeper / Shopkeeper |
| Tohoku Zunko | `14` | Town Elder / Healer |
| Tohoku Kiritan | `5` | Blacksmith / DPS |
| Tohoku Itako | `6` | Spirit Guide / Lore |
| Shikoku Metan | `2` | Alchemist / Elemental |
| Kyushu Sora | `16` | Bard / Rhythm Host |
| Chubu Tsurugi | `17` | Arena Master / Tank |
| Melusina | `100` | Threshold Guardian (custom SBV2) |

---

## Step 6 ΓÇö Playtesting (2 min)

### 6a. Open the Vertical Slice Map
In Unreal Content Browser, open `/Game/Melodia/Levels/L_ZenForestTest`.

Hit **Play** (Alt+P). What you should see:
1. Player spawns ΓåÆ Sir Melodious flies off
2. Walk forward ΓåÆ encounter trigger ΓåÆ rhythm battle begins
3. Press keys in time to the beat
4. Victory ΓåÆ choose reward (Heart Token / Swirl Token / Song Power)
5. Room exit unlocks ΓåÆ walk through ΓåÆ next stage generates
6. 3 stages ΓåÆ Sir Melodious reunion ΓåÆ run complete

### 6b. Combat Quick Reference
| Key | Action |
|-----|--------|
| WASD | Movement |
| 1/2/3/4 | Skill lanes (elemental wheel) |
| Q | Basic attack |
| E | Defend |
| R | Ultimate (when gauge full) |
| Space | Dodge |

### 6c. Smoke Test
```powershell
cd G:\EnvironmentPortfolio\BS_GodFile\Content\Python
python -m gmm.gameplay_smoke
```

---

## Port Map

| Port | Protocol | Service | Direction |
|------|----------|---------|-----------|
| `9876` | TCP + JSON | LiveLink ΓÇö FBX/texture/animation streaming | Blender ΓåÆ UE |
| `9317` | HTTP REST | Blender MCP ΓÇö genome/agent control | External ΓåÆ Blender |
| `9316` | HTTP JSON-RPC | UE Monolith MCP ΓÇö Python execution, 1,325 tools | Any ΓåÆ UE |
| `50021` | HTTP REST | VOICEVOX ΓÇö text-to-speech (7 ZunZun voices) | Any ΓåÆ VOICEVOX |
| `50022` | HTTP REST | Melusina Voice ΓÇö custom SBV2 TTS | Any ΓåÆ Melusina |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **Port 9876 "in use"** | Multiple Blender instances. Close extras via Task Manager. |
| **BL MCP :9317 not responding** | Reload SurrealArch addon: Scripting ΓåÆ `import surreal_architecture_gen; surreal_architecture_gen.reload_addon()` |
| **Materials gray after import** | Run UE Python: `import resolve_material_crosswalk; resolve_material_crosswalk.resolve_all()` |
| **VOICEVOX "speaker X not found"** | Open VOICEVOX ΓåÆ Settings ΓåÆ Manage Voice Libraries ΓåÆ download missing voices |
| **LiveLink "Send + Materials" fails** | Ensure Material Bridge panel has a saved crosswalk for the active object |
| **PIE crash on encounter** | Rebuild MelodiaCore: UE ΓåÆ Tools ΓåÆ Refresh Visual Studio Project ΓåÆ Build |

---

## Key Scripts

| Script | What It Does | Run In |
|--------|-------------|--------|
| `Tools/setup_zunzun_studio.py` | Import all ZunZun models, studio layout with lights/cameras | Blender |
| `Tools/generate_all_voices.py` | Batch-generate 102 NPC voice WAVs via VOICEVOX | Terminal |
| `Content/Python/import_zundamon.py` | Import Zundamon FBX + create materials in UE | UE Python |
| `Content/Python/create_zunzun_bps.py` | Auto-create 7 NPC Blueprints + quest/shop/party data | UE Python |
| `Content/Python/resolve_material_crosswalk.py` | Post-import material auto-resolver (.material_map.json) | UE Python |
| `Content/Python/setup_material_functions.py` | Rebuild 17 UE material functions | UE Python |
| `deploy/deploy_all.ps1` | Launch all 11 autonomous agent loops | Terminal |
| `deploy/loop_status.ps1` | Live dashboard of agent loop status | Terminal |
