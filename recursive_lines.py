# 10/22/2025
# RECURSIVE LINES

def asterisks(x):
    # BASE CASE - if the number is 0 then stop
    if x <= 0:
        return

    asterisks(x - 1)

    print('*' * x)

def main():
    # Get user input
    user_input = input("Enter a Number: ")
    
    # Turn user input from a string into an integer
    try:
        lines_to_draw = int(user_input)
        
        asterisks(lines_to_draw)
    
    except ValueError:
        # Error message for when a whole number is not entered
        print("Not a Valid Number. Try Again.")

# Call the main function
if __name__ == '__main__':
    main()