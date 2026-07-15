# Live Collaborative Level Designer ΓÇö 5-Minute Setup

> **No 300 GB download. No Unreal content.** Set up Blender Γåö UE5 live bridge for collaborative level design using sparse checkout. Only downloads the scripts, addons, and tools you need ΓÇö ~50 MB total.

---

## Option A: Sparse Checkout (Recommended ΓÇö 50 MB)

```powershell
git clone --filter=blob:none --no-checkout https://github.com/fromage3900/environment-portfolio.git MelodiaCollab
cd MelodiaCollab
git sparse-checkout init --cone
git sparse-checkout set `
  deploy/surreal_arch `
  deploy/surreal_world `
  deploy/surreal_os `
  deploy/surreal_greybox `
  Content/Python/gmm `
  Content/Python/material_lib.py `
  Content/Python/create_zunzun_bps.py `
  Content/Python/import_zundamon.py `
  Content/Python/resolve_material_crosswalk.py `
  Content/Python/fix_vertical_slice_p0.py `
  Tools `
  Docs/ONBOARDING_LIVE_COLLAB.md `
  Docs/ZUNZUN_FAMILY_INTEGRATION.md `
  Docs/ZUNDAMON_DESIGN_BIBLE.md `
  Docs/ZUNDAMON_NPC_SPEC.md `
  README.md `
  DOC_INDEX.md
git checkout
```

**What you get (~50 MB):**
- Γ£à SurrealArch Blender addon (procedural generation, live bridge, material bridge)
- Γ£à GMM game systems (Python combat/rhythm/roguelike rules)
- Γ£à All pipeline tools and scripts
- Γ£à Full documentation
- Γ¥î No .uasset files, .blend files, textures, or UE content

---

## Option B: Collaboration Kit Zip (If git sparse checkout is unavailable)

The `deploy/surreal_arch/` folder IS the Blender addon. Copy it to:
```
C:\Users\<you>\AppData\Roaming\Blender Foundation\Blender\5.1\scripts\addons\surreal_arch\
```

Then copy the companion folders:
```
deploy/surreal_world/  ΓåÆ Blender addons/surreal_world/
deploy/surreal_os/     ΓåÆ Blender addons/surreal_os/
deploy/surreal_greybox/ΓåÆ Blender addons/surreal_greybox/
```

---

## Prerequisites

| Tool | Version | Download |
|------|---------|----------|
| Blender | 5.1+ | [blender.org](https://www.blender.org/) |
| Unreal Engine | 5.8 | Epic Games Launcher |
| VOICEVOX | 0.25+ | [voicevox.hiroshiba.jp](https://voicevox.hiroshiba.jp/) |
| VRM Importer (Blender) | 4.4+ | [GitHub](https://github.com/saturday06/VRM-Addon-for-Blender/releases) |

---

## Step-by-Step

### 1. Open the Unreal Project
```
G:\EnvironmentPortfolio\BS_GodFile\BS_GodFile.uproject
```
Wait for shader compilation. The Monolith MCP starts automatically on port `:9316`.

### 2. Open Blender ΓÇö Verify the Addon
```
Open any .blend ΓåÆ N-panel ΓåÆ "Melodia Studio" tab should appear.
```
If it doesn't: Edit ΓåÆ Preferences ΓåÆ Add-ons ΓåÆ search "surreal_arch" ΓåÆ enable.

### 3. Start the Bridge
```
N-panel ΓåÆ Melodia Studio ΓåÆ Live Bridge ΓåÆ Refresh Status ΓåÆ Start Server
```
You should see: `Γ£ô LiveLink  Γ£ô BL MCP  Γ£ô UE MCP`

### 4. Generate & Send
```
1. Genome Carousel ΓåÆ pick style ΓåÆ Apply
2. Material Bridge ΓåÆ Scan Slots ΓåÆ Auto-Match
3. Live Bridge ΓåÆ Send + Materials
4. In Unreal: /Game/LiveLink/ ΓÇö geometry with correct materials
```

---

## Two-Designer Workflow

| Role | Tool | What They Do |
|------|------|-------------|
| **Geometry Designer** | Blender | Procedural gen, mesh editing, materials, live sync |
| **Level Scripter** | Unreal | Blueprints, encounters, lighting, PCG, NPCs |

---

## Port Map

| Port | Service | Direction |
|------|---------|-----------|
| `9876` | LiveLink ΓÇö FBX streaming | Blender ΓåÆ UE |
| `9316` | UE MCP ΓÇö Python execution | Any ΓåÆ UE |
| `9317` | Blender MCP ΓÇö genome control | Any ΓåÆ Blender |
| `50021` | VOICEVOX ΓÇö NPC voices | Any ΓåÆ VOICEVOX |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Melodia Studio tab missing | Enable surreal_arch addon in Blender preferences |
| Port 9876 "in use" | Close extra Blender instances via Task Manager |
| Materials gray in UE | `resolve_material_crosswalk.resolve_all()` in UE Python |
| No voices | Start VOICEVOX, run `Tools/generate_all_voices.py` |

---

Full guide: [Docs/ONBOARDING_LIVE_COLLAB.md](Docs/ONBOARDING_LIVE_COLLAB.md)
Character integration: [Docs/ZUNZUN_FAMILY_INTEGRATION.md](Docs/ZUNZUN_FAMILY_INTEGRATION.md)
NPC Blueprint spec: [Docs/ZUNDAMON_NPC_SPEC.md](Docs/ZUNDAMON_NPC_SPEC.md)
