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

user_coffee = ''
total_money = 0
req_water = 0
req_milk = 0
req_coffee = 0


def report():
    print(f"Water:{resources['water']}ml")
    print(f"milk:{resources['milk']}ml")
    print(f"coffee:{resources['coffee']}g")
    print(f"Money: ${total_money}")
    coffee_machine()


def coffee_machine():
    global user_coffee
    global req_water
    global req_coffee
    global req_milk

    user_coffee = input("What Would You Like? (espresso/latte/cappuccino):")

    if user_coffee == "report":
        report()
    elif user_coffee == "off":
        print("coffee machine is off")
        return
    else:
        req_water = MENU[user_coffee]["ingredients"]["water"]
        if user_coffee != "espresso":
            req_milk = MENU[user_coffee]["ingredients"]["milk"]
        req_coffee = MENU[user_coffee]["ingredients"]["coffee"]

        if req_coffee <= resources["coffee"]:
            if req_water <= resources["water"]:
                if user_coffee != "espresso":
                    if req_milk <= resources["milk"]:
                        resources["water"] -= req_water
                        resources["coffee"] -= req_coffee
                        resources["milk"] -= req_milk
                        payment()
                    else:
                        print("not enough milk")
                        coffee_machine()
                else:
                    resources["coffee"] -= req_coffee
                    resources["water"] -= req_water
                    payment()

            else:
                print("not enough water")
                coffee_machine()
        else:
            print("not enough coffee")
            coffee_machine()


# payment
# Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
def payment():
    global user_coffee
    global total_money
    print("PLease insert coins.")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))

    user_payment = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)

    if user_payment >= MENU[user_coffee]["cost"]:
        total_money += MENU[user_coffee]["cost"]
        refund_money = user_payment - MENU[user_coffee]["cost"]
        print(f"Here is {refund_money} in change.")
        print(f"Here is you {user_coffee} enjoy.")
        coffee_machine()
    else:
        print("Sorry that is not enough money. money refunded")
        resources["water"] += req_water
        if user_coffee != "espresso":
            resources["milk"] += req_milk
        resources["coffee"] += req_coffee

        coffee_machine()


coffee_machine()