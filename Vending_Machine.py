money = {
    1: 5,   # key:value pairs for available money options
    2: 10,
    3: 15,
    4: 20
}

drink_price = {
    1: 3.35,  # key:value pairs for drink price options
    2: 2.10,
    3: 2.85
}

txt = {
    "money": "Insert your money (1: 5$, 2: 10$, 3: 15$, 4: 20$): ",
    "drink": "What drink would you like to choose (1: Coca Cola = 3.35$, 2: Pepsi = 2.10$, 3: Orange = 2.85$)?: ",
    "not_enough": "You don't have enough money. Please insert again."
}

class NotValidChoice(Exception):
    """Custom exception to handle invalid choices"""
    pass


def vending_machine():
    """Main function to run the vending machine"""
    finish = False
    user_money = get_input(txt["money"], money)  # get user's money
    user_drink_price = 0
# loop until user does not want to choose any more drinks
    while not finish:
        user_drink_price += get_input(txt["drink"], drink_price)
        if user_money < min(drink_price.values()):
            print(txt["not_enough"])
            user_money += get_input(txt["money"], money)
            continue
        change = user_money - user_drink_price
        # loop until user has enough money to pay for the chosen drink(s)
        while change < 0:
            print(txt["not_enough"])
            user_money += get_input(txt["money"], money)
            change = user_money - user_drink_price
        # check if user has sufficient funds to choose a drink
        
            
        finish = input("Do you want to choose another drink? [y/n]: ").lower() == "n"

    

    print(f"Here is your change: {change}$\nThanks for buying!")


def get_input(prompt, choices):
    """Function to get input from user and validate the input"""
    while True:
        try:
            choice = int(input(prompt))
            if choice not in choices:
                raise NotValidChoice
            return choices[choice]
        except ValueError:
            print("Invalid input. Please enter a number.")
        except NotValidChoice:
            print("Invalid choice. Please enter a valid number.")


vending_machine()