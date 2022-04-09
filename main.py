import random


# this function evaluates weather entry is higher or low the price to guess
def evaluates(user_entry, expected_entry):
    if user_entry < expected_entry:
        print("It's more !")
    elif user_entry > expected_entry:
        print("It's less !")
    else:
        print("You won !!!!")
        exit(0)


# this function validates that the price enter by user is a number and in range of
def validate_price(user_input):
    return user_input.isnumeric() and int(user_input) > 0


# this function initialize price to guess between 1 and 100
def init_price():
    return random.randint(1, 100)


if __name__ == '__main__':
    hidden_price = init_price()
    print("to divine : ", hidden_price)
    user_entry = 0
    while True:
        user_entry = input("enter price")
        if validate_price(user_entry):
            evaluates(int(user_entry), hidden_price)
        else:
            print("not a digit or negative number")
            pass
