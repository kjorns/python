# 09/17/2025
# MOST FREQUENT CHARACTER

def main():
    # Get user entered word
    user_word = input("Please Enter a String: ")

    # Variable to remember most frequent letter
    most_frequent_letter = ""

    # Variable to remember how many times the most frequent letter appeared
    most_frequent_count = 0

    # The list for letters that have already been checked
    already_checked_letters = []

    # The loop to go through the string letter by letter
    for letter in user_word:
        # Make sure the character is not a space and not in the already checked list
        if not letter.isspace() and letter not in already_checked_letters:
            
            # Counter for letter
            current_count = 0
            
            # The loop to go through the string again from the beginning
            for letter_to_check in user_word:
                # If letters match, then add to count
                if letter == letter_to_check:
                    current_count = current_count + 1
            
            # After counting all letter appearances check to see if it appears more than the last letter so far
            if current_count > most_frequent_count:
                most_frequent_count = current_count
                most_frequent_letter = letter
            
            # Add letter to already checked list
            already_checked_letters.append(letter)

    # Print results
    print("The Most Frequent Letter:", most_frequent_letter)

# Call the main function
if __name__ == "__main__":
    main()