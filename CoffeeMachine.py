MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 120,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 240,
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


def refill():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    coffee_machine()


def report():
    print(f"Water:{resources['water']}ml")
    print(f"milk:{resources['milk']}ml")
    print(f"coffee:{resources['coffee']}g")
    print(f"Money: {total_money}rs")
    coffee_machine()


def coffee_machine():
    global user_coffee
    global req_water
    global req_coffee
    global req_milk

    user_coffee = input("What Would You Like? (espresso/latte/cappuccino):")

    if user_coffee == "report":
        report()
    elif user_coffee == "refill":
        refill()
    elif user_coffee == "off":
        print("coffee machine is off")
        return
    else:
        print(f"{user_coffee} is of {MENU[user_coffee]['cost']}rs.")
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
    print("PLease Pay.")
    quarters = int(input("How many 200 ke note?:"))
    dimes = int(input("How many 100 ke note?:"))
    nickles = int(input("How many 50 ke note?:"))
    pennies = int(input("How many 10 ke note?:"))

    user_payment = (200 * quarters) + (100 * dimes) + (50 * nickles) + (10 * pennies)

    if user_payment >= MENU[user_coffee]["cost"]:
        total_money += MENU[user_coffee]["cost"]
        refund_money = user_payment - MENU[user_coffee]["cost"]
        print(f"Here is {refund_money}rs in change.")
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
