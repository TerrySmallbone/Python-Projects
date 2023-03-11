from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
# print(my_money_machine)#test print
# print(my_coffee_maker)#test print
# print(my_coffee_maker)#test print

machine_running = True
while machine_running:

    order_choice = input(f"Hello, what would you like to order? Our options are {my_menu.get_items()}").lower()
    if order_choice == "off":
        machine_running = False
    elif order_choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        order_choice = my_menu.find_drink(order_choice)#turns order name into an item with name, cost & ingredients
        if my_coffee_maker.is_resource_sufficient(order_choice):
            if my_money_machine.make_payment(order_choice.cost):
                my_coffee_maker.make_coffee(order_choice)
                my_money_machine.report()#test print





