# 10/01/2025
# WORD INDEX

# Define the function for GET
def get_word_index_data(input_file_name):
    
    # Initialize the dictionary
    word_index = {}

    # Initialize the line counter
    line_number = 0
    
    try:
        # Read file and loop through line by line
        with open(input_file_name, 'r') as infile:
            for line in infile:
                # Add 1 to the counter for every line read
                line_number = line_number + 1
                
                # Set line to lowercase
                cleaned_line = line.lower()
                
                # Remove special characters and put spaces in their place
                cleaned_line = cleaned_line.replace('.', ' ')
                cleaned_line = cleaned_line.replace(',', ' ')
                cleaned_line = cleaned_line.replace('?', ' ')
                cleaned_line = cleaned_line.replace('!', ' ')
                cleaned_line = cleaned_line.replace(':', ' ')
                cleaned_line = cleaned_line.replace(';', ' ')
                cleaned_line = cleaned_line.replace('"', ' ')
                cleaned_line = cleaned_line.replace("'", ' ')
                
                # Split the line into words
                words = cleaned_line.split()
                
                # Build the dictionary
                for word in words:
                    if word:
                        if word in word_index:
                            if line_number not in word_index[word]:
                                word_index[word].append(line_number)
                        else:
                            word_index[word] = [line_number]
        
        return word_index

    except FileNotFoundError:
        print(f"Error: '{input_file_name}' Was Not Found.")
        return

# Define the function for WRITE
def write_word_index_file(word_index, output_file_name):
    if not word_index: 
        print("The Word Dictionary is Empty")
        return

    # Sort the words alphabetically
    sorted_words = sorted(word_index.keys())

    with open(output_file_name, 'w') as outfile:
        for word in sorted_words:
            line_numbers = word_index[word]
            
            # Create a string to hold the line numbers
            number_string = ""
            
            # Loop through the list of numbers
            for num in line_numbers:
                # Add the number (converted to a string) and a comma-space separator
                number_string = number_string + str(num) + ", "
            
            # Remove the extra comma and space at the end
            if len(number_string) > 0:
                 line_numbers_str = number_string[:-2] 
            else:
                 line_numbers_str = ""
            
            # Write the final formatted line
            outfile.write(f'{word}: {line_numbers_str}\n')
            
    print(f"Word Index Saved To '{output_file_name}'.")

def main():
    INPUT_FILE = 'Kennedy.txt'
    OUTPUT_FILE = 'index.txt'
    
    # GET - Call the get function to read the file and build the dictionary
    word_data = get_word_index_data(INPUT_FILE)
    
    # WRITE - Call the write function to write the index file
    if word_data is not None:
        write_word_index_file(word_data, OUTPUT_FILE)

# Call the main function
if __name__ == '__main__':
    main()