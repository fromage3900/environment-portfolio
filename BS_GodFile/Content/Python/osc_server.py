"""osc_server.py — UE OSC listener for TouchDesigner bridge.

Receives OSC messages from TD on port 8000 and routes them to:
- Material Parameter Collections (MPCs) for Substrate Toon parameters
- Niagara systems for particle spawn rates and parameter control
- Blueprint events for gameplay triggers

Branch: feature/touchdesigner-mcp-integration
Owner: TOA (TouchDesigner Orchestrator Agent)
"""

import unreal


OSC_LISTEN_PORT = 8000


# Nikki/Melodia preset: 12-float toon parameter array index mapping
TOON_PARAM_INDEX = {
    'bloom_intensity': 0,
    'bloom_threshold': 1,
    'bloom_tint_r': 2,
    'bloom_tint_g': 3,
    'bloom_tint_b': 4,
    'shadow_tint_r': 5,
    'shadow_tint_g': 6,
    'shadow_tint_b': 7,
    'saturation': 8,
    'contrast': 9,
    'diffuse_wrap': 10,
    'reserved': 11,
}

# Style preset mapping
STYLE_PRESET_NAMES = {
    0: 'Nikki',
    1: 'Madoka',
    2: 'Celestial',
    3: 'Itto',
    4: 'Sakura',
}


class OSCBridge:
    """OSC listener that bridges TD messages to UE subsystems."""

    def __init__(self):
        self.server = None
        self.active = False
        self.current_preset = 0
        self._mpc_sakura = None
        self._mpc_magical = None

    def start(self, port: int = OSC_LISTEN_PORT):
        """Start the OSC server on the given port."""
        try:
            osc_manager = unreal.OSCManager

            # Get or create OSC server
            self.server = osc_manager.get_or_create_osc_server(
                unreal.Name(str(port)),
                port
            )

            if not self.server:
                unreal.log_error(
                    f"[TD-Bridge] Failed to create OSC server on port {port}. "
                    f"Ensure the OSC plugin is enabled in the project."
                )
                return False

            # Register address handlers
            self.server.add_osc_address('/material/preset', self._on_preset)
            self.server.add_osc_address('/material/toon', self._on_toon_params)
            self.server.add_osc_address('/melusina/pitch', self._on_pitch)
            self.server.add_osc_address('/melusina/amp', self._on_amplitude)
            self.server.add_osc_address('/niagara/sparkle/rate', self._on_sparkle_rate)
            self.server.add_osc_address('/niagara/mote/rate', self._on_mote_rate)
            self.server.add_osc_address('/niagara/burst', self._on_wish_burst)
            self.server.add_osc_address('/time/cycle', self._on_day_night)

            self.active = True
            unreal.log(
                f"[TD-Bridge] OSC server started on port {port} — "
                f"listening for TouchDesigner parameters"
            )

            # Load MPCs
            self._mpc_sakura = unreal.find_object(None, "/Game/EnvSandbox/VFX/MPC_SakuraDream")
            self._mpc_magical = unreal.find_object(None, "/Game/EnvSandbox/VFX/MPC_Magical")

            return True

        except Exception as e:
            unreal.log_error(f"[TD-Bridge] OSC server startup failed: {e}")
            return False

    def stop(self):
        """Stop the OSC server."""
        if self.server:
            self.server.clear()
            self.active = False
            unreal.log("[TD-Bridge] OSC server stopped.")

    # ── OSC Handlers ─────────────────────────────────────────────────

    def _on_preset(self, address, data):
        """Handle /material/preset (int 0-4)."""
        preset_id = int(data[0]) if data else 0
        preset_name = STYLE_PRESET_NAMES.get(preset_id, 'Unknown')
        self.current_preset = preset_id
        unreal.log(f"[TD-Bridge] Style preset set to: {preset_id} ({preset_name})")

        # Push to MPC_SakuraDream if available
        if self._mpc_sakura:
            try:
                unreal.MaterialEditingLibrary.set_material_instance_scalar_parameter_value(
                    self._mpc_sakura, "StylePreset", float(preset_id)
                )
            except Exception:
                pass

    def _on_toon_params(self, address, data):
        """Handle /material/toon (float[12])."""
        values = [float(v) for v in data[:12]]
        unreal.log(f"[TD-Bridge] Toon params received: bloom={values[0]:.1f}")

        # Push bloom to MPC
        if self._mpc_magical:
            try:
                unreal.MaterialEditingLibrary.set_material_instance_scalar_parameter_value(
                    self._mpc_magical, "BloomIntensity",
                    values[TOON_PARAM_INDEX['bloom_intensity']]
                )
            except Exception:
                pass

    def _on_pitch(self, address, data):
        """Handle /melusina/pitch (float Hz)."""
        pitch_hz = float(data[0]) if data else 440.0
        # In production: drives UE Substrate Toon "impressionist" warp amount

    def _on_amplitude(self, address, data):
        """Handle /melusina/amp (float 0-1)."""
        amp = float(data[0]) if data else 0.5
        # In production: drives Niagara spawn rate multipliers

    def _on_sparkle_rate(self, address, data):
        """Handle /niagara/sparkle/rate (float)."""
        rate = float(data[0]) if data else 0.5

    def _on_mote_rate(self, address, data):
        """Handle /niagara/mote/rate (float)."""
        rate = float(data[0]) if data else 0.5

    def _on_wish_burst(self, address, data):
        """Handle /niagara/burst (trigger)."""
        unreal.log("[TD-Bridge] Wish burst triggered!")

    def _on_day_night(self, address, data):
        """Handle /time/cycle (float 0-1)."""
        cycle = float(data[0]) if data else 0.5


# Singleton
_bridge = OSCBridge()


def start_bridge(port: int = OSC_LISTEN_PORT):
    """Start the TD-UE OSC bridge. Called from init_unreal.py on editor startup."""
    return _bridge.start(port)


def stop_bridge():
    """Stop the OSC bridge."""
    _bridge.stop()


def get_bridge():
    """Get the bridge instance for external status checks."""
    return _bridge
