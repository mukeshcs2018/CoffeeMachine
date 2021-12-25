
from data import MENU

from art import logo
print(logo)
print()

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """"Returns true when resources is sufficient and False when resources is insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns  the total calculated """
    print("Please insert coins.")
    total = int(input("How many quaters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickeles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    """Return True when the payment is accepted, or False  if money is insufficient."""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """"Deduct the required ingredients from the resources. """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cuppuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:$ {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])