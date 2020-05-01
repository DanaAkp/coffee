from base.beverage_coffee import BeverageCoffee
from base.condiment_coffee import CondimentCoffee
from config.cost_config import CONDIMENT_SOY_COST
from config.description_config import CONDIMENT_SOY


class Soy(CondimentCoffee):
    def __init__(self, beverage):
        self.beverage = beverage
        self.check(BeverageCoffee)

    description = CONDIMENT_SOY
    cost_ = CONDIMENT_SOY_COST
    dict_description = {}
