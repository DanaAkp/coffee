from base.condiment_tea import CondimentTea
from config.cost_config import CONDIMENT_CARAMEL_COST
from config.description_config import CONDIMENT_CARAMEL

from base.beverage_coffee import BeverageCoffee
from base.beverage_tea import BeverageTea


class Caramel(CondimentTea):
    def __init__(self, beverage):
        self.beverage = beverage
        self.check((BeverageCoffee, BeverageTea))
    description = CONDIMENT_CARAMEL
    cost_ = CONDIMENT_CARAMEL_COST
    dict_description = {}
