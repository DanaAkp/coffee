from dataclasses import dataclass

from base.beverage_coffee import BeverageCoffee
from config.cost_config import HOUSE_BLEND_COFFEE_COST
from config.description_config import HOUSE_BLEND_COFFEE


@dataclass
class HouseBlend(BeverageCoffee):
    description = HOUSE_BLEND_COFFEE
    cost_ = HOUSE_BLEND_COFFEE_COST

    def cost(self):
        return self.cost_

    def get_description(self):
        return self.description

    def get_dict(self):
        return self.description
