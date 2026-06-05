# 09/17/2025
# PIG LATIN

def main():
    # Get user input
    sentence = input("Enter a Sentence to Convert to Pig Latin: ")

    # Split sentence into individual words
    words = sentence.split()
    
    # The list to store words after converting
    pig_latin_words = []
    
    # The loop to go through each word
    for word in words:
        # Make sure word isn't empty
        if word:
            # Get the first letter of the word
            first_letter = word[0]
            # Get the rest of the word
            rest_of_word = word[1:]
            
            # Combine with ay to form Pig Latin word
            pig_latin_word = rest_of_word + first_letter + "ay"
            
            # Add the new word to the list
            pig_latin_words.append(pig_latin_word)
            
    # The loop to join the words
    result = ""
    # Add a space after each word
    for word in pig_latin_words:
        result += word + " "
    
    # Print results
    print(f"English: {sentence}")
    print(f"Pig Latin: {result}")

# Call the main function
if __name__ == "__main__":
    main()