
# This program displays employee net pay values.
# All employees have a standard $45 deduction from their checks.
# If an employee does not earn enough to cover the deduction,
# an error message is displayed.

DEDUCTION = 45
EOFNAME = "ZZZ"

print("Enter first name or", EOFNAME, "to quit")
name = input("Name: ")

while name != EOFNAME:
    try:
        hours = float(input(f"Enter hours worked for {name}: "))
        rate = float(input(f"Enter hourly rate for {name}: "))

        gross = hours * rate
        net = gross - DEDUCTION

        if net > 0:
            print(f"Net pay for {name} is ${net:.2f}")
        else:
            print("Deductions not covered. Net is $0.")
    except ValueError:
        print("Invalid input. Please enter numeric values for hours and rate.")

    print("\nEnter next name or", EOFNAME, "to quit")
    name = input("Name: ")

print("End of job")
