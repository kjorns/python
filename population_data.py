# POPULATION DATA

# I had to do a lot of research on this one. Please let me know if it is not working the way it is supposed to.

def main():
    # try block for potential errors
    try:
        # The list for storing populatons
        pop_list = []

        # Read the contents of the file into a list
        with open('USPopulation.txt', 'r') as infile:
            pop_list = infile.readlines()

        # Strip the newline characters from each element
        for index in range(len(pop_list)):
            pop_list[index] = pop_list[index].rstrip('\n')

        # Convert each element to an int
        for index in range(len(pop_list)):
            pop_list[index] = int(pop_list[index])

    except FileNotFoundError:
        # This part runs if the file is not found
        print("Error: The file 'USPopulation.txt' was not found.")
        return # Stop if file isn't found

    # The list to hold all the annual changes
    annual_changes = []

    # Go through the list starting with the second number
    for index in range(1, len(pop_list)):
        # Calculate change from one year to the next
        increase = pop_list[index] - pop_list[index-1]

        # Add this year's increase to new list
        annual_changes.append(increase)

    # Use the sum(), min(), and max() functions to find total, biggest, and smallest
    total_increase = sum(annual_changes)
    biggest_increase = max(annual_changes)
    smallest_increase = min(annual_changes)

    # Find year with biggest increase
    index_of_biggest = annual_changes.index(biggest_increase)
    year_with_biggest_increase = 1950 + index_of_biggest + 1

    # Find year with smallest increase
    index_of_smallest = annual_changes.index(smallest_increase)
    year_with_smallest_increase = 1950 + index_of_smallest + 1

    # Calculate the average
    number_of_changes = len(pop_list) - 1
    average_increase = total_increase / number_of_changes

    # Print the results
    print(f"Average Annual Change: {average_increase}")
    print(f"Year With the Greatest Increase: {year_with_biggest_increase}")
    print(f"Year With the Smallest Increase: {year_with_smallest_increase}")

# Call the main function
if __name__ == "__main__":
    main()