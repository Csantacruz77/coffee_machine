from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    order_name = input(f"What would you like to order? {menu.get_items()}").lower()
    if order_name == "report":
        coffee_maker.report()
        money_machine.report()
    elif order_name == "off":
        machine_on = False
    else:
        drink = menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


