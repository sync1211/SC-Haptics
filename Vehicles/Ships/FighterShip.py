from Vehicles.Vehicle import Vehicle
from effects.Engines.FighterEngineEffect import FighterEngineEffect
from effects.Weapons.Guns.RepeaterFiringEffect import RepeaterFiringEffect
from effects.Weapons.Ordinance.MissileFiringEffect import MissileFiringEffect


class FighterShip(Vehicle):
    def __init__(self):
        engine = FighterEngineEffect(self)
        weapon1 = RepeaterFiringEffect() 
        weapon2 = RepeaterFiringEffect()
        ordinance = MissileFiringEffect() 
        super().__init__(engine, weapon1, weapon2, ordinance)