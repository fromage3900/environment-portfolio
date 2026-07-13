# Study: Korean Hanok Madang Courtyard

**Style:** korean  
**Version:** 0.1  
**Sources:** hanok courtyard typology (madang), hongsalmun shrine gates, daecheong open halls

## Motifs

- Red-arrow **hongsalmun** gate as ceremonial threshold
- Enclosed **madang** court ringed by single-story timber halls
- Raised ondol / platform stairs and gentle approach ramps
- Open **daecheong** colonnade facing the court (arcade stand-in)
- Horizontal civic chain — gate → lane → hall → colonnade → stair/ramp → court fountain

## Proportions

- Low eave line relative to court width (verticality ~0.35–0.45)
- Gate span narrower than main hall bay
- Stair rise shallow; ramp as secondary accessible approach

## Rhythms

- Alternating solid hall / open colonnade bays around the court
- Corridor offset after the gate compresses the entry axis
- Axis compression surreal transform for court enclosure feel

## Structural rules

- No tower spines — pillars mark corners, not vertical monuments
- Prefer timber hall + stone curb language (`material_choice: AUTO` / `STONE`)
- Graph terminates on a civic water feature, not a vertical marker

## Ornament systems

- Minimal carved ridge / cheoma cues via existing KR_HANOK kit
- Hongsalmun red-arrow posts as gate ornament

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| hongsalmun_gate | KR_HONG_SAL_MUN | Ceremonial red-arrow gate |
| madang_hall | KR_HANOK | Elevated timber hall on platform |
| daecheong_arcade | GB_ROMANESQUE_ARCADE | Open hall colonnade stand-in |
| madang_stair | GREYBOX_STAIR_BLOCK | Raised platform stair |
| madang_ramp | GREYBOX_RAMP | Accessible approach ramp |
| madang_fountain | PUBLIC_FOUNTAIN | Court-center water feature |

## OS hooks

- Genome: `korean_hanok_madang_v1`
- Grammar graph: `KOREAN_HANOK_MADANG`
- Compose style: `KOREAN_HANOK_MADANG`
