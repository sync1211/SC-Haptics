from HapticsBase import HapticsBase
from Vehicles import Vehicle


class EngineHaptics(HapticsBase):
    def __init__(self, shipState: Vehicle):
        super().__init__()
        self.shipState = shipState