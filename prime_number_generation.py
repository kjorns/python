# PRIME NUMBER GENERATION

def main():
    # Ask user to enter a number greater than 1
    user_input_str = input("Please Enter a Number Greater Than 1: ")
    user_input = int(user_input_str) # Turn user input string into an integer

    # Check every number from 2 to the one the user entered
    for number in range(2, user_input + 1):
        
        # We start by saying the number is a prime number
        is_it_prime = True

        # Check to see if the number has any divisors
        # Check from 2 to the one the user entered
        for index in range(2, number):
            # If there is a divisor it is not a prime number
            if number % index == 0:
                is_it_prime = False
                break # Stop checking

        # Print the results
        if is_it_prime:
            print(f"The Number {number} is a Prime Number")
        else:
            print(f"The Number {number} is a Composite Number.")

# Call the main function
if __name__ == "__main__":
    main()