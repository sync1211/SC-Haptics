from effects.AdvancedHapticEffectBase import AdvancedHapticEffectBase
from effects.ImpactEffect import ImpactEffect
from effects.Weapons.WeaponHaptics import WeaponHaptics

PATTERN = [
    [{"index": 18, "intensity": 100}, {"index": 17, "intensity": 100}],
    [{"index": 14, "intensity": 100}, {"index": 13, "intensity": 100}],
    [{"index": 10, "intensity": 100}, {"index": 9, "intensity": 100}],
    [{"index": 6, "intensity": 100}, {"index": 5, "intensity": 100}],
    [{"index": 2, "intensity": 100}, {"index": 1, "intensity": 100}]
]


class MissileFiringEffect(AdvancedHapticEffectBase, WeaponHaptics):
    def __init__(self):
        decay_factor = 50
        base_intensity = 100
        effect_center = (1.5, 2)
        effect_frames = 3

        matrix_length_y = 4
        matrix_length_x = 5

        effect = ImpactEffect()
        pattern = list(
            map(
                lambda x: {"front": x, "back": []},
                effect.GetPattern(
                    decay_factor,
                    base_intensity,
                    effect_center,
                    effect_frames,
                    matrix_length_y,
                    matrix_length_x
                )
            )
        )
        super().__init__(pattern)

    def GetPattern(self, is_firing: bool) -> dict:
        if not (is_firing or self.effect_stage != 0):
            self.effect_stage = 0
            return {"front": [], "back": []}

        return super().GetPattern()


    
