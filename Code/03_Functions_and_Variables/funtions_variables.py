# Functions with parameters and return values
# This program also demonstrates local and global variables

# Global variable
school_name = "Whitecliffe College"


# Function with parameters
def add_numbers(number1, number2):
    # Local variable
    total = number1 + number2

    # Return the result to the function call
    return total


# Getting values from the user
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Calling the function and passing arguments
answer = add_numbers(first_number, second_number)

# Displaying the returned result
print("The total is:", answer)

# Using the global variable
print("College:", school_name)
