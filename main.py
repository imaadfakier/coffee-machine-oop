from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

user_input = ''

# menu = Menu()
# menu_item = MenuItem()
# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()

a_menu = Menu()
# a_menu_item = MenuItem()
machine_finance = MoneyMachine()
machine = CoffeeMaker()

while user_input != 'off':
    user_input = input('What would you like? (espresso/latte/cappuccino): ')

    if user_input == 'report':
        # CoffeeMaker.report()
        # machine.report()

        machine.report()
        machine_finance.report()
    elif user_input in a_menu.get_items():
        drink_wanted = a_menu.find_drink(user_input)
        # print(drink_wanted)
        # print(drink_wanted.ingredients)

        # if machine.is_resource_sufficient(drink_wanted):
        #     # machine_finance.process_coins()
        #     # print(total_monetary_value)
        #
        #     if machine_finance.make_payment(drink_wanted.cost):
        #         machine.make_coffee(drink_wanted)

        if machine.is_resource_sufficient(drink_wanted) and machine_finance.make_payment(drink_wanted.cost):
            machine.make_coffee(drink_wanted)
