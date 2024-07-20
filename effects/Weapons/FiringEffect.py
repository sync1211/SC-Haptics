from effects.Weapons.WeaponHaptics import WeaponHaptics


class FiringEffect(WeaponHaptics):
    def __init__(self, pattern: list):
        super().__init__(pattern)
        self.effect_stage = 0

    def GetPattern(self, is_firing: bool) -> dict:
        if not (is_firing or self.effect_stage != 0):
            self.effect_stage = 0
            return {"front": [], "back": []}

        return super().GetPattern()
