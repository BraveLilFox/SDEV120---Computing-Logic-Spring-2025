# This program determines whether students have passed or failed a course.
# The student needs to average 60 or more on two tests.

PASSING = 60

# Prompt the user for the first score
firstTest = int(input("Enter first score or 0 to quit: "))

# Loop until the user enters 0
while firstTest != 0:
    # Prompt for the second score
    secondTest = int(input("Enter second score: "))

    # Calculate the average
    average = (firstTest + secondTest) / 2
    print("Average is", average)

    # Determine pass/fail
    if average >= PASSING:
        print("Pass")
    else:
        print("Fail")

    # Prompt again for the first score
    firstTest = int(input("Enter first score or 0 to quit: "))
