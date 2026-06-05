# 09/17/2025
# POWERBALL LOTTERY - PART 1
# Display the 10 most overdue numbers

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

    # STRUGGLED STARTING HERE, HAD TO RESEARCH
    # The list for holding numbers and the number of draws ago, list will essentially have 2 columns
    last_drawn_info = []

    # Go through all regular numbers, starting with most recent
    for index in range(len(regular_numbers) - 1, -1, -1):
        current_num = regular_numbers[index]

        # Use any with a generator expression to check if the number is already in the list
        if not any(item[0] == current_num for item in last_drawn_info):
            draws_ago = len(regular_numbers) - index
            last_drawn_info.append([current_num, draws_ago])

    # Use the sort method to arrange list
    # Use a special key to tell it to sort by the number of draws (the second item in each pair)
    # reverse=True means we put the highest counts first, from most overdue to least overdue
    last_drawn_info.sort(key=lambda item: item[1], reverse=True)
    # I am not exactly sure what lambda is, but it came up in my research for sorting this data

    # Print results
    print("Top 10 Most Overdue Numbers:")
    for index in range(10):
        if index < len(last_drawn_info):
            num, count = last_drawn_info[index]
            print(f"Number {num} has been overdue for {count} draws.")
        else:
            break

# Call the main function
if __name__ == "__main__":
    main()