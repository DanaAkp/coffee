from beverage.tea.black_tea import BlackTea
from beverage.coffee.dark_roast import DarkRoast

from condiment.milk import Milk
from condiment.caramel import Caramel
from condiment.mocha import Mocha

tea = BlackTea()
tea.discount(30)
car = Caramel(tea)
milk = Milk(car)
print('milk', milk.cost())
print(milk.get_description())

dr = DarkRoast()
ml = Milk(dr)
moc = Mocha(ml)
moc3 = Mocha(moc)
print('moc3', moc3.cost())
print(moc3.get_description())

moc3.print_description()

# moc2 = Mocha(tea)

