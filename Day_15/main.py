MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def enough_stuff(order_reqs):
    for item in order_reqs:
        if order_reqs[item] >= resources[item]:
            print(f"Sorry we are low on {item}")
            return False
    return True


def handle_money():
    print(f"That will be ${order['cost']}0")
    print('Please insert coins:')
    total = int(input('How many quarters? ')) * .25
    total += int(input('How many dimes? ')) * .1
    total += int(input('How many nickles? ')) * .05
    total += int(input('How many pennies? ')) * .01
    return total


def pay_auth(tender, cost):
    if tender >= cost:
        change = tender - cost
        print(f"Here is {change}0 in change.")
        print(f"Here you are. Appreciate your business.")
        global profit
        profit += cost
        return True
    else:
        print("Not enough money, Chuck. Try again. ")
        return False


working = True

while working:
    print("Welcome to CoffeeBallz.")
    prompt = input('Would you like an espresso, a latte or a cappuccino? ')
    if prompt == 'off':
        working = False
    elif prompt == 'report':
        print(f"water: {resources['water']}ml"),
        print(f"milk: {resources['milk']}ml"),
        print(f"coffee: {resources['coffee']}ml"),
        print(f"profit: ${profit}")
    else:
        order = MENU[prompt]
        if enough_stuff(order['ingredients']):
            pay = handle_money()
            pay_auth(pay, order['cost'])