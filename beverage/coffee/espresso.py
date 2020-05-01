from dataclasses import dataclass

from base.beverage_coffee import BeverageCoffee
from config.cost_config import ESPRESSO_COFFEE_COST
from config.description_config import ESPRESSO_COFFEE


@dataclass
class Espresso(BeverageCoffee):
    description = ESPRESSO_COFFEE
    cost_ = ESPRESSO_COFFEE_COST

    def cost(self):
        return self.cost_

    def get_description(self):
        return self.description

    def get_dict(self):
        return self.description
