# MAGIC 8 BALL

import random

def main():
    # The list for holding different answers listed in file
    answers = []

    # try block for potential errors
    try:
        # Read the contents of the file into a list
        with open('8_ball_responses.txt', 'r') as infile:
            answers = infile.readlines()

        # Strip the \n from each element
        for index in range(len(answers)):
            answers[index] = answers[index].rstrip('\n')

    except FileNotFoundError:
        print("Error: The file '8_ball_responses.txt' was not found.")
        return  # Stop if file isn't found

    # The loop to keep going until user types quit
    while True:
        # Get the user's question
        question = input("Ask the Magic 8 Ball a Question: ")

        # I had to do some research here
        # Check if the user typed 'quit' and break loop if they did
        if question.lower() == 'quit':
            break

        # Pick one of the answers from the list randomly
        the_answer = random.choice(answers)

        # Print results
        print(f"The Magic 8 Ball Says: {the_answer}")

# Call the main function
if __name__ == "__main__":
    main()