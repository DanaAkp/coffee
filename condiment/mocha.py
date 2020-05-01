from base.beverage_coffee import BeverageCoffee
from base.condiment_coffee import CondimentCoffee
from config.cost_config import CONDIMENT_MOCHA_COST
from config.description_config import CONDIMENT_MOCHA


class Mocha(CondimentCoffee):
    def __init__(self, beverage):
        self.beverage = beverage
        self.check(BeverageCoffee)

    description = CONDIMENT_MOCHA
    cost_ = CONDIMENT_MOCHA_COST
    dict_description = {}

