

from effects.SimpleHapticEffectBase import SimpleHapticEffectBase

class WeaponHaptics(SimpleHapticEffectBase):
    def __init__(self, pattern: list):
        super().__init__(pattern)
        self.effect_stage = 0
