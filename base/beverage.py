from abc import ABCMeta, abstractmethod


class Beverage(metaclass=ABCMeta):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

    def discount(self, discount):
        self.cost_ = self.cost_*(100-discount)/100