# 09/24/2025
# UNIQUE WORDS

def main():
    # The empty set for storing all words
    unique_words = set()

    # Read the contents of the file into a list
    with open('text.txt', 'r') as infile:
        lines = infile.readlines()

    # The loop to go through each line of the file one by one
    for line in lines:
        # Change to lowercase letters so that all duplicate words are the exact same
        line_lowercase = line.lower()
        
        # Get rid of punctuation so that all duplicate words are the exact same
        line_lowercase_no_punctuation = line_lowercase.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
        
        # Split line into separate words
        words_in_line = line_lowercase_no_punctuation.split()

        # Go through each word and add to the set
        for one_word in words_in_line:
            unique_words.add(one_word)

    # Print results
    for word in unique_words:
        print(word)

# Call the main function
if __name__ == '__main__':
    main()