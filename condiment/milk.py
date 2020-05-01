from base.condiment_coffee import CondimentCoffee

from config.cost_config import CONDIMENT_MILK_COST
from config.description_config import CONDIMENT_MILK

from base.beverage_coffee import BeverageCoffee
from base.beverage_tea import BeverageTea


class Milk(CondimentCoffee):
    def __init__(self, beverage):
        self.beverage = beverage
        self.check((BeverageTea, BeverageCoffee))

    description = CONDIMENT_MILK
    cost_ = CONDIMENT_MILK_COST
    dict_description = {}
