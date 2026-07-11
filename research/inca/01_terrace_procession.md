# Study: Inca Terrace Processional Ramp

**Style:** inca / andean  
**Version:** 0.1  
**Sources:** Machu Picchu agricultural terraces; Ollantaytambo processional stairs; Andean ushnu plaza typology

## Motifs

- Stepped battered retaining faces (andenes)
- Long processional ramps climbing terrace bands
- Ceremonial stair blocks cut into terrace fronts
- Horizontal colonnade / arcade along plaza edges
- Lintel stone portals (trapezoidal Inca doorways approximated as LINTEL)
- Plaza terminus with water / fountain basin

## Proportions

- Terrace batter ~0.08–0.12; multi-step retaining stacks
- Ramp rise modest vs length (horizontal civic, not tower spine)
- Stair blocks wide (~2.4 m) with shallow rise (~0.22 m)
- Colonnade bays ~3.2 m clear

## Rhythms

- Retaining face → ramp ascent → stair landing → arcade edge → lintel gate → plaza fountain
- Horizontal chain preferred over vertical monument spines

## Structural rules

- No tower / keep / obelisk spines
- Corner markers are pillars, not watchtowers
- Compose roles map wall→retaining, gate→lintel portal, sacred→stair block

## Ornament systems

- Ashlar stone courses; recess trim on arcade/ramp curbs
- Minimal filigree — structural stone logic dominates

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| andenes_retaining | RETAINING_WALL | Battered terrace face |
| processional_ramp | GREYBOX_RAMP | Inclined civic ascent |
| ceremonial_stair | GREYBOX_STAIR_BLOCK | Wide stair into terrace |
| plaza_arcade | GB_ROMANESQUE_ARCADE | Edge colonnade stand-in |
| lintel_portal | ARCHWAY_ADV (LINTEL) | Stone doorway |
| plaza_basin | PUBLIC_FOUNTAIN | Plaza water terminus |

## OS hooks

- Genome: `inca_terrace_v1`
- Grammar graph: `INCA_TERRACE`
- Compose style: `INCA_TERRACE`
- Transform: `axis_compression`
