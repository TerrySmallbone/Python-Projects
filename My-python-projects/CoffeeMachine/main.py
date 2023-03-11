from data import MENU, resources

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01
machine_resources = resources
money = 0.00

## Print report.
def report(current_resources):
    """ Returns F string with current report of materials. Use in a print statement!"""
    print(f"Water: {current_resources['water']}ml\n"
          f"Milk: {current_resources['milk']}ml \n"
          f"Coffee: {current_resources['coffee']}g")

#Check resources sufficient?
def check_resources(machine_resources, MENU, coffee_choice):
    """Returns True if machine has sufficient resources"""
    if machine_resources["water"] > MENU[coffee_choice]["ingredients"]["water"]:
        # print("true")
        if machine_resources["coffee"] > MENU[coffee_choice]["ingredients"]["coffee"]:
            # print("true")
            if "milk" in MENU[coffee_choice]["ingredients"]:
                # print("true")
                if machine_resources["milk"] > MENU[coffee_choice]["ingredients"]["milk"]:
                    # print("true")
                    return True
                else:
                    # print("False")
                    return False
            else:
                # print("False")
                return True
        else:
            # print("False")
            return False
    else:
        # print("False")
        return False


## Process coins.
def payment(cost):
    """Gives cost, promts payment and gives total payment amount"""
    print(f"Total Cost: £{cost} Please insert coins.")
    quarters_total = QUARTER * float(input("How many Quarters?"))
    dimes_total = DIME * float(input("How many Dimes?"))
    nickles_total = NICKLE * float(input("How many Nickles?"))
    pennies_total = PENNY * float(input("How many Pennies?"))
    money_total = quarters_total + dimes_total + nickles_total + pennies_total
    return money_total

## Check transaction successful?
def check_payment(money_paid, coffee_choice):
    """Checks payment is sufficient, refundeds extra and updates machine total money"""
    print(f"£{money_paid} inserted")
    if money_paid < coffee_choice["cost"]:
        print(f"Sorry, you inserted £{money_paid} but the cost is £{coffee_choice['cost']}. Money refunded. ")
        exit()# TODO. change to restart order later
    else:
        refund = round(money_paid - coffee_choice["cost"], 2)
        print(f"The price was £{coffee_choice['cost']}, here is £{refund} back")
        new_money_total = round(money_paid - refund, 2)
        return new_money_total

# Make Coffee.
def make_coffee(machine_resources, MENU, coffee_choice):
    """Subtracts chosen coffee ingredients from machine resources"""
    # print(MENU[coffee_choice])#test print
    machine_resources['water'] -= MENU[coffee_choice]['ingredients']['water']
    if "milk" in MENU[coffee_choice]['ingredients']:
        machine_resources['milk'] -= MENU[coffee_choice]['ingredients']['milk']
    machine_resources['coffee'] -= MENU[coffee_choice]['ingredients']['coffee']
    # Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”.
    print(f"Here's your {coffee_choice}, please enjoy")
    print(report(machine_resources))
    return machine_resources['coffee'], machine_resources['water'], machine_resources['milk']



def machine_operation():
    machine_operating = True
    while machine_operating:
        # report(machine_resources) ###complete### temp commented out

        ## Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
        coffee_choice = input("What would you like? (espresso/latte/cappuccino \n").lower()
        if coffee_choice == "off":
            machine_operating = False
        else:


            if check_resources(machine_resources, MENU, coffee_choice) == False:
                print("I'm sorry, the machine does not have enough resources to fulfill this request")
                exit()

            money = payment(MENU[coffee_choice]["cost"])

            money = check_payment(money, MENU[coffee_choice])

            # report(machine_resources)#test print

            make_coffee(machine_resources, MENU, coffee_choice)
            # print(machine_resources)#test print

            report(machine_resources)#test print

            another_coffee = input("Would you like to order again? 'Y' or 'N'\n").lower()
            if another_coffee == "N":
                machine_operating = False



machine_operation()
# TODO: 2.Turn off the Coffee Machine by entering “ off ” to the prompt.
#  a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
#  the machine. Your code should end execution when this happens.


