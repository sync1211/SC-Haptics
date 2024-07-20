import utils
from Vehicles.Ships.Modes.ShipMode import ShipMode
from effects.Engines import EngineHaptics
from effects.Weapons import WeaponHaptics



class Vehicle:
    def __init__(self, engine: EngineHaptics, weapon1: WeaponHaptics, weapon2: WeaponHaptics, ordinance: WeaponHaptics):
        self.engine_active = False
        self.firing1 = False
        self.firing2 = False
        self.firing_missile = False
        self.throttle = 0
        self.engine = engine
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.missiles = ordinance

        self.currentMode = ShipMode.WEAPON

    def GetHapticsPattern(self) -> dict:
        pattern = {"front": [], "back": []}

        # Add engine pattern
        if self.engine_active:
            utils._merge_patterns(pattern, self.engine.GetPattern())    

        # Add weapon patterns
        utils._merge_patterns(pattern, self.weapon1.GetPattern(self.firing1)) 
        utils._merge_patterns(pattern, self.weapon2.GetPattern(self.firing2)) 
        utils._merge_patterns(pattern, self.missiles.GetPattern(self.firing_missile)) 

        return pattern