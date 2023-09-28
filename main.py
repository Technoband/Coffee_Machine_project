MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}


def coffee_resource_check(coffee_type):
    # TODO: 3. if coin fulfil the amount required for coffee then print the change
    if MENU[coffee_type]["ingredients"]["water"] <= resources["water"]:
        if MENU[coffee_type]["ingredients"]["milk"] <= resources["milk"]:
            if MENU[coffee_type]["ingredients"]["coffee"] <= resources["coffee"]:
                return True
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough milk")
    else:
        print("Sorry there is not enough water")


def calculate_coins(quarters, dimes, nickles, pennies):
    a = 0.25 * quarters
    b = 0.1 * dimes
    c = 0.05 * nickles
    d = 0.01 * pennies
    return a + b + c + d


def update_resources(coffee_type):
    water = resources["water"] - MENU[coffee_type]["ingredients"]["water"]
    milk = resources["milk"] - MENU[coffee_type]["ingredients"]["milk"]
    coffee = resources["coffee"] - MENU[coffee_type]["ingredients"]["coffee"]
    resources["water"] = water
    resources["milk"] = milk
    resources["coffee"] = coffee
    print(resources)


def coffee_order():
    # TODO: 1. Ask user for the coffee type
    print("Available resources")
    for key in resources.keys():
        print(key, ":", resources[key])

    coffee_type = input("What would you like? (espresso/latte/cappuccino/off):\n").lower()
    if coffee_type == "off":
        exit()

    # TODO: 2. ask user to insert coins (quarters, dimes, nickles, pennies)
    resource_check = coffee_resource_check(coffee_type)

    if resource_check:
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total_coins = calculate_coins(quarters, dimes, nickles, pennies)
        if total_coins < MENU["espresso"]["cost"]:
            print(" Sorry your amount is insufficient for this order, Money refunded")
        else:
            resources["money"] += MENU["espresso"]["cost"]
            change = total_coins - MENU["espresso"]["cost"]
            print(f"Here is {change} in change")
            print("Here is your coffee ☕")
            update_resources(coffee_type)
    # TODO 5. Repeatedly ask customer what coffe type he wants

    conti = input("Do you want to continue, Enter 'yes' or 'no'\n").lower()
    if conti == "yes":
        coffee_order()
    else:
        print("Turning off the Machine")
        exit()


# TODO 4. print here os your coffe name
coffee_order()

