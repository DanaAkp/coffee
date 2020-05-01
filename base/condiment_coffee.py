from dataclasses import dataclass

from base.beverage_coffee import BeverageCoffee


@dataclass
class CondimentCoffee(BeverageCoffee):
    def check(self, tuple_beverage):
        if not isinstance(self.beverage, tuple_beverage):
            raise Exception('Error! Invalid condiment.')

    def cost(self):
        return self.beverage.cost() + self.cost_

    def get_description(self):
        return '{} {}'.format(self.beverage.get_description(), self.description)

    def print_description(self):
        d = self.get_dict({})
        for i in d:
            if d[i] == 1:
                print(i, end=' ')
            elif d[i] == 2:
                print('double', i)
            else:
                print('triple', i)
