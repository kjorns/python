# LOTTERY NUMBER GENERATOR

# I followed along with the tutorial on this one

import random

# Constants for the number of digits and the range of numbers
MAX_DIGITS = 7
START = 0
END = 9

def main():
    # Create a list with seven zeros
    numbers = [0] * 7

    # The loop to generate random numbers and populate the list
    for index in range(MAX_DIGITS):
        # The randint function returns a random integer between START and END
        numbers[index] = random.randint(START, END)

    # Print 'Here are you lottery numbers:' before the generated random number
    print('Here are your lottery numbers:')
    # The loop to print each number in the list
    for index in range(MAX_DIGITS):
        print(numbers[index], end='') # 'end' prevents a new line after each number

# Call the main function
if __name__ == "__main__":
    main()