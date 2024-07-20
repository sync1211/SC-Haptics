
from HapticsBase import HapticsBase


class SimpleHapticEffectBase(HapticsBase):
    '''
    Undirectional haptic effect
    Haptics patterns are applied to the front and the back of the haptic vest
    '''
    def __init__(self, pattern: list):
        super().__init__()
        self.effect_stage = 0
        self.pattern = pattern

    def GetPattern(self) -> dict:
        if self.effect_stage < len(self.pattern):
            self.effect_stage += 1
            self.effect_stage %= len(self.pattern)

        pattern = self.pattern[self.effect_stage]
        return {"front": pattern, "back": pattern}