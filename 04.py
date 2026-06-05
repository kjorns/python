# NUMBER ANALYSIS PROGRAM

def main():
    # The list to hold the numbers
    numbers = []

    # The loop to ask for the numbers one by one twenty times
    for index in range(20):
        # The loop to enter a valid number, convert it to an integer, and add it to the list
        while True:
            # try block for potential errors
            try:
                number_input = input("Enter Number: ")
                
                # Convert string into integer
                the_number = int(number_input)
                
                # Add the number to the list
                numbers.append(the_number)
                
                break # Ends while loop once valid number is entered
            except ValueError:
                # This part runs if they didn't enter a valid number
                print("Please Enter a Number")

    # Find the lowest number in the list
    lowest = min(numbers)

    # Find the highest number in the list
    highest = max(numbers)

    # Add up all of the numbers to get the total
    total = sum(numbers)

    # Find the average by dividing the total and how many numbers there are
    average = total / len(numbers) # len tells us how many items are in the list

    # Print results
    print("The Lowest Number:", lowest)
    print("The Highest Number:", highest)
    print("The Total of All Numbers:", total)
    print("The Average of the Numbers:", average)

# Call the main function
if __name__ == '__main__':
    main()