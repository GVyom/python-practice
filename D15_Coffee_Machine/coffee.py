from receipe import resources
from receipe import menu

def print_report():
    print("Here is what all I have right now")

    for item in resources:
        print(f"{item.capitalize()}: {resources[item]}")

def check_resources(choice):
    check = menu[choice]["ingredients"]

    for i in check:
        if check[i] > resources[i]:
            print(f"Sorry, not enough {i}. Please re-fill")
            return False
    return True

def check_money(quaters,dimes,nickels,pennies,choice):
    total_money =  0.25*quaters + 0.10*dimes + 0.05*nickels + 0.01*pennies
    if total_money >= menu[choice]['cost']:
        change = total_money - menu[choice]['cost']
        return True, change
    else:
        print(f'Sorry you do not have enough amount! Here is your ${total_money} back')
        return False, 0
    
def inventory_management(choice):
    resources["money"] += menu[choice]['cost']
    ingredients = menu[choice]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]

def collect_coins():
        quarters = float(input('Please enter quaters paid: '))
        dimes = float(input('Please enter dimes paid: '))
        nickels = float(input('Please enter nickels paid: '))
        pennies = float(input('Please enter pennies paid: '))
        return quarters, dimes, nickels, pennies

def refill():
    for item in ["water", "milk", "coffee"]:
        amount = float(input(f"How much {item} would you like to add? "))
        resources[item] += amount

    print("Machine successfully refilled.")
    print_report()

while True:
    choice = input(f'Hey, Hope you are having a nice day. Please let me know what you need, and I shall get to it right away (espresso, latte, or cappuccino): ').lower()
    
    while True:
        if choice == "off":
            refill()
            maintenance = input(f"As requested by user, the machine is in maintenance mode. Please turn it on by writing all Done: ").lower()
            if maintenance == "all done":
                print('maintenance is all done, thankyou for keeping me well :)')
                break
            else:
                continue
        else:
            break

    if choice == 'report':
        print_report()
        continue

    valid_choices = ["espresso", "latte", "cappuccino"]
   
    if choice not in valid_choices:
        print(f'Sorry! I don\'t know how to make that :/')
        continue

    if check_resources(choice):
        print('Please Enter the units of each coin paid:')
        quarters, dimes, nickels, pennies = collect_coins()
        payment_sucess, change = check_money(quarters,dimes,nickels,pennies,choice)
    else:
        continue

    if payment_sucess:
        inventory_management(choice)
        print(f'Thankyou for ordering! Have a great day, here is your orderd {choice} and {change}')
