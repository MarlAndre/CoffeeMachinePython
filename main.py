MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


# TODO 2. Check resources sufficient to make drink order
def is_resources_sufficient(order_ingredients):
    """Return True if enough ingredients, else will return False."""
    is_enough = True
    for ingredients in order_ingredients:
        if order_ingredients[ingredients] > resources[ingredients]:
            print(f"Sorry, there's not enough {ingredients}")
            is_enough = False
    return is_enough


# TODO 3. Process coins
def process_coins():
    """Return total calculated from coin inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many nickles?: ")) * 0.10
    total += int(input("How many dimes?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# TODO 4. Check transaction is successful
def is_transaction_successful(coin_inserted, drink_cost):
    """Return True if payment accepted, else will return False if money insufficient."""
    if coin_inserted >= drink_cost:
        change = round(coin_inserted - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money. Money refunded.")
        return False


# TODO 5. Make drink order
def make_coffee(drink_name, order_ingredients):
    for ingredients in order_ingredients:
        resources[ingredients] -= order_ingredients[ingredients]
    print(f"Here's your {drink_name}. Enjoy =)")


is_on = True

while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        is_on = False
# TODO 1. Print a report of all coffee resources
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}l")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[order]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])



