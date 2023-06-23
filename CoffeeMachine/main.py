MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 170,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 260,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 320,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_status():
    report = print(
        f'water: {resources["water"]}ml\nmilk: {resources["milk"]}ml\ncoffee: {resources["coffee"]}gms\n{profit} rs')
    return report


def check_resources_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def money_inserted():
    print(f"Cost for your {choice} is {choice_cost}")
    print(" Please insert Rupees Notes ")
    total = int(input("How Many Hundred RS Note: ")) * 100
    total += int(input("How Many Fifty RS Note: ")) * 50
    total += int(input("How Many Twenty's RS Note: ")) * 20
    total += int(input("How Many Ten's RS Note: ")) * 10
    return total


def is_transaction_sucessful(total, choice_cost):
    if total >= choice_cost:
        change = total - choice_cost
        print(f"Here is your RS{change} Change")
        global profit
        profit += choice_cost
        return True
    elif total <= choice_cost:
        print(f"Insufficient Amount Inserter, Here is Your Money RS{total}")
        return False


def make_coffee(resources, ingredients):
    for item in resources:
        resources[item] -= ingredients[item]
    print(f"Here is Your {choice} Coffee ☕")

is_on = True
profit = 0

while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        check_status()
    else:
        ingredients = MENU[choice]["ingredients"]
        choice_cost = MENU[choice]["cost"]

        if check_resources_sufficient(ingredients) == False:
            is_on = False
        elif check_resources_sufficient(ingredients) == True:
            total = money_inserted()
            if is_transaction_sucessful(total, choice_cost) == False:
                break
            make_coffee(resources, ingredients)


