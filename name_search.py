# NAME SEARCH

def main():
    # The list for storing popular names
    popular_names = []

    # try block for potential errors
    try:
        # Read the contents of the file into a list
        with open('popular_names.txt', 'r') as names_file:
            popular_names = names_file.readlines()
        
        # Strip the \n from each element
        for index in range(len(popular_names)):
            popular_names[index] = popular_names[index].rstrip('\n')

    except FileNotFoundError:
        # This part runs if the file is not found
        print("Error: The file 'popular_names.txt' was not found.")
        return # Stop if file isn't found
    
    # The loop to check if the user entered name exists on the list or not
    while True:
        # Get user input
        user_input = input("Enter Name: ")

        # Check if the name exists in the list
        if user_input in popular_names:
            print(f"{user_input} was a popular name")
        else:
            print(f"{user_input} was NOT a popular name")

# Call the main function
if __name__ == '__main__':
    main()