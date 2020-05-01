from dataclasses import dataclass

from base.beverage_tea import BeverageTea
from config.cost_config import BLACK_TEA_COST
from config.description_config import BLACK_TEA


@dataclass
class BlackTea(BeverageTea):
    description = BLACK_TEA
    cost_ = BLACK_TEA_COST

    def cost(self):
        return self.cost_

    def get_description(self):
        return self.description

    def get_dict(self, dict2):
        return self.description
