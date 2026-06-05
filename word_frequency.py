# 09/26/2025
# WORD FREQUENCY

def main():
    word_counts = {}
    
    # Define the punctuation we want to get rid of
    punctuation_to_remove = '.,!?"\'()—:\n' 

    # try block for potential errors
    try:
        # Read the contents of the file into a list
        with open('WordFreq.txt', 'r') as infile:
            text_lines = infile.readlines()
        
        # Strip the \n from each element
        for index in range(len(text_lines)):
            text_lines[index] = text_lines[index].rstrip('\n')

        # Combine the list of lines into one large string 
        text_data = ''
        for line in text_lines:
            text_data += line + ' ' # Add the line and a space after it
        
        # Make everything lowercase
        text_data = text_data.lower()
        
        # Get rid of punctuation by looping through and replacing it with a space
        cleaned_text = ""
        for char in text_data:
            if char not in punctuation_to_remove:
                cleaned_text += char
            else:
                cleaned_text += " "
        
        # Split the cleaned text into a list of words
        word_list = cleaned_text.split()
        
        # Loop through the word list and count them
        for word in word_list:
            if word: 
                # Check if the word is already in the dictionary
                if word in word_counts:
                    # If it is, add 1 to its current count
                    word_counts[word] = word_counts[word] + 1
                else:
                    # If it is not, start its count at 1
                    word_counts[word] = 1

        # Print the results
        for word, count in word_counts.items():
            print(f"The word '{word}' showed up {count} times.")
        
    except FileNotFoundError:
        print("Error: The file 'WordFreq.txt' was not found.")
        return # Stop if file isn't found

# Call the main function
if __name__ == '__main__':
    main()