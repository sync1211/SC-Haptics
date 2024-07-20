
from effects.Weapons.FiringEffect import FiringEffect


PATTERN = [
    [{"index": 18, "intensity": 100}, {"index": 17, "intensity": 100}],
    [{"index": 14, "intensity": 100}, {"index": 13, "intensity": 100}],
    [{"index": 10, "intensity": 100}, {"index": 9, "intensity": 100}],
    [{"index": 6, "intensity": 100}, {"index": 5, "intensity": 100}],
    [{"index": 2, "intensity": 100}, {"index": 1, "intensity": 100}]
]

class RepeaterFiringEffect(FiringEffect):
    def __init__(self):
        super().__init__(PATTERN)
        
