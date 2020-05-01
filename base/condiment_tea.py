from base.beverage_tea import BeverageTea
from dataclasses import dataclass


@dataclass
class CondimentTea(BeverageTea):
    def check(self, tuple_beverage):
        if not isinstance(self.beverage, tuple_beverage):
            raise Exception('Error! Invalid condiment.')

    def cost(self):
        return self.beverage.cost() + self.cost_

    def get_description(self):
        return '{} {}'.format(self.beverage.get_description(), self.description)

    def print_description(self):
        d = self.get_dict({})
        print(d)
