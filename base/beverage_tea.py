from abc import ABCMeta

from base.beverage import Beverage


class BeverageTea(Beverage, metaclass=ABCMeta):
    def get_dict(self, dict2: dict):
        d = self.beverage.get_dict(dict2)

        if isinstance(d, str):
            dict2.setdefault(d, 1)
        else:
            dict2.update(d)

        if dict2.get(self.description) is None:
            dict2.setdefault(self.description, 1)
        else:
            dict2[self.description] += 1

        return dict2

