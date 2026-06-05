# 09/17/2025
# POWERBALL LOTTERY - PART 2
# Display the frequency of each number 1–69, and the frequency of each Powerball number 1–26

def main():
    # The list for holding the first five numbers in each line
    regular_numbers = []
    # The list for holding the last numbers in each line
    powerball_numbers = []

    # try block for potential errors
    try:
        # Read the contents of the file into a list
        with open('pbnumbers.txt', 'r') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print("Error: The file 'pbnumbers.txt' was not found.")
        return # Stop if file isn't found

    # The loop to go through each line
    for line in lines:
        # Remove leading and trailing whitespace
        stripped_line = line.strip()

        # Split string by whitespace
        numbers = stripped_line.split()
        
        # Check if line has the right amount of numbers
        if len(numbers) == 6:
            # Add first five numbers to regular_numbers list
            for num_str in numbers[:5]:
                # Convert number from a string to an integer
                current_number = int(num_str)
                # Add number to list
                regular_numbers.append(current_number)
                
                # Add last number to powerball_numbers list
                powerball_number = int(numbers[5])
                powerball_numbers.append(powerball_number)
    
    print("Frequency of Each Number (1-69):")
    # The loop for looping through every possible regular number from 1 to 69
    for num in range(1, 70):
        count = 0
        # The loop for looping through all the numbers in regular_numbers list
        for item in regular_numbers:
            # If numbers match, add 1 to count
            if item == num:
                count += 1
        # Print final count for that number
        print(f"Number {num}: picked {count} times")

    print("Frequency of Each PowerBall Number (1-26):")
    # The loop for looping through every possible PowerBall number from 1 to 26
    for num in range(1, 27):
        count = 0
        # The loop for looping through all the numbers in powerball_numbers list
        for item in powerball_numbers:
            # If numbers match, add 1 to count
            if item == num:
                count += 1
        # Print final count for that number
        print(f"PowerBall {num}: picked {count} times")
        
# Call the main function
if __name__ == "__main__":
    main()