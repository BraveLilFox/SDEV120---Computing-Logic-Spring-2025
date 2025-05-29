
# This program computes and displays the cost of home ownership
# for any number of users. It ends when the user enters 0 for the mortgage payment.

def start_up():
    global mortgage_payment
    try:
        mortgage_payment = float(input("Enter your mortgage payment or 0 to quit: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        mortgage_payment = -1  # To prevent immediate termination on error

def main_loop():
    try:
        utilities = float(input("Enter utilities: "))
        taxes = float(input("Enter taxes: "))
        upkeep = float(input("Enter amount for upkeep: "))
        total = mortgage_payment + utilities + taxes + upkeep
        print(f"Total is ${total:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def finish_up():
    print("End of program")

# Main program
mortgage_payment = -1
start_up()

while mortgage_payment != 0:
    main_loop()
    start_up()

finish_up()
