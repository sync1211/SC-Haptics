from effects.SimpleHapticEffectBase import SimpleHapticEffectBase


class AdvancedHapticEffectBase(SimpleHapticEffectBase):
    '''
    Directional haptic effect
    Uses patterns containing a dict of a haptic response
    '''
    def __init__(self, pattern: list):
        super().__init__(pattern)

    def GetPattern(self) -> dict:
        if self.effect_stage < len(self.pattern):
            self.effect_stage += 1
            self.effect_stage %= len(self.pattern)

        return self.pattern[self.effect_stage]