from effects.Engines.EngineHaptics import EngineHaptics


class FighterEngineEffect(EngineHaptics):
    def __init__(self, shipState):
        super().__init__(shipState)

    def GetPattern(self) -> dict:
        if not self.shipState.engine_active:
            return {"front": [], "back": []}

        pattern = [
            {"index": 19, "intensity": self.shipState.throttle}, 
            {"index": 16, "intensity": self.shipState.throttle}, 
            {"index": 15, "intensity": self.shipState.throttle}, 
            {"index": 12, "intensity": self.shipState.throttle}
        ]

        return {"front": pattern, "back": pattern}