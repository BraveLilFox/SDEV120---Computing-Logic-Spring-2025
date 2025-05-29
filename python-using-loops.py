# Function to check if a number is even or odd
def check_odd_even(numbers):
    for number in numbers:
        
        # Check if number is odd or even
        if number % 2 == 0:
            print(str(number) + " is even")   # Print that number is even
            print(str(number) + " is odd")   # Print that number is odd
        
        # Main Program
        def main():
            # Initialize an empty list to store the numbers
            user_numbers = []
            
            # Ask the user to input 15 numbers
            print("Please enter 15 numbers: )
            for i in range(15):
                while True:
                    try:
                        # Get user input, covert to