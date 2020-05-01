from dataclasses import dataclass

from base.beverage_coffee import BeverageCoffee
from config.cost_config import DARK_ROAST_COFFEE_COST

from config.description_config import DARK_ROAST_COFFEE


@dataclass
class DarkRoast(BeverageCoffee):
    description = DARK_ROAST_COFFEE
    cost_ = DARK_ROAST_COFFEE_COST

    def cost(self):
        return self.cost_

    def get_description(self):
        return self.description

    def get_dict(self, dict2):
        return self.description
