from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    coffee_maker = CoffeeMaker
    money_machine = MoneyMachine

    machine_on = True
    while machine_on:
        choice = input("What would you like? (espresso/latte/cappuccino/): ")

        if choice == 'off':
            break
        elif choice == 'report':
            coffee_maker.report()
            money_machine.report()
        elif choice in menu.get_items():
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            print('Invalid selection. Please try again.')

if __name__ == '__main__':
    main()