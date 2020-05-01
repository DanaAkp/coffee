from dataclasses import dataclass

from base.beverage_coffee import BeverageCoffee
from config.cost_config import DECAF_COFFEE_COST
from config.description_config import DECAF_COFFEE


@dataclass
class Decaf(BeverageCoffee):
    description = DECAF_COFFEE
    cost_ = DECAF_COFFEE_COST

    def cost(self):
        return self.cost_

    def get_description(self):
        return self.description

    def get_dict(self):
        return self.description
