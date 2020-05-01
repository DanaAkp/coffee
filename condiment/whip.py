from dataclasses import dataclass

from base.condiment_coffee import CondimentCoffee
from config.cost_config import CONDIMENT_WHIP_COST
from config.description_config import CONDIMENT_WHIP

from base.beverage_coffee import BeverageCoffee


class Whip(CondimentCoffee):
    def __init__(self, beverage):
        self.beverage = beverage
        self.check(BeverageCoffee)

    description = CONDIMENT_WHIP
    cost_ = CONDIMENT_WHIP_COST
    dict_description = {}
