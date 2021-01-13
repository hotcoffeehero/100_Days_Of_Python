from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cash_register = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

on = True



while on:
    options = menu.get_items()
    choix = input(f"What'll it be? {options}")
    if choix == 'off':
        on = False
    elif choix == 'report':
        cash_register.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choix)
        enough_stuff = coffee_maker.is_resource_sufficient(drink)
        enough_money = cash_register.make_payment(drink.cost)
        if enough_stuff and enough_money:
            coffee_maker.make_coffee(drink)

