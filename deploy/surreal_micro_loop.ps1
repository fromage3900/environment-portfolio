# 10-minute Surreal Architecture micro-loop with optional stop sentinel.
$stopFile = Join-Path $PSScriptRoot "SURREAL_ARCH_LOOP_STOP"
$tickPrompt = '10m micro-cycle: (1) read deploy/SURREAL_ARCH_LOOP_STATE.md + SURREAL_ARCHITECTURE_RESEARCH.md; (2) pick ONE micro slice (QA/verify/docs/UX glue/pipeline tweak, no big new kits); (3) implement in deploy/; (4) sync to live Blender addons; (5) py_compile touched files + run deploy/_mcp_verify_overhaul.py; (6) if MCP up, smoke-generate one affected GB_* type; (7) append LOOP_STATE'

while ($true) {
    Start-Sleep -Seconds 600
    if (Test-Path $stopFile) {
        Write-Output "AGENT_LOOP_STOP_surreal_micro10 stop sentinel detected"
        break
    }
    Write-Output "AGENT_LOOP_TICK_surreal_micro10 {`"prompt`":`"$tickPrompt`"}"
}
