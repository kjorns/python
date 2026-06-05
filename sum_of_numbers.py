# 10/22/2025
# SUM OF NUMBERS

def sum_function(num):
    # BASE CASE - when we get to 1, stop the loop and return 1
    if num == 1:
        return 1

    else:
        x = num + sum_function(num - 1)
        return x

def main(): 
    # Get user input
    user_input = input("Enter a Number: ")
    
    # Turn user input from a string into an integer
    try:
        number = int(user_input)

    except ValueError:
        # Error message for when a whole number is not entered
        print("Not a Valid Number. Try Again.")

    # Run the calculation
    final_result = sum_function(number)
    
    # Display the results
    print("Your Number:", number)
    print("The Sum From 1 Up To That Number:", final_result)


# Call the main function
if __name__ == '__main__':
    main()