# DRIVER'S LICENSE EXAM

def main():
    # The list for the correct answers
    correct_answers = ['A', 'D', 'B', 'B', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']

    # try block for potential errors
    try:
        # Read the contents of the file into a list
        with open('student_answers.txt', 'r') as answers_file:
            student_answers = answers_file.readlines()
        
        # Strip the \n from each element
        for index in range(len(student_answers)):
            student_answers[index] = student_answers[index].rstrip('\n')

    except FileNotFoundError:
        # This part runs if the file is not found
        print("Error: The file 'student_answers.txt' was not found.")
        return # Stop if file isn't found

    # Variables for grading
    correct_count = 0
    incorrect_count = 0
    incorrect_questions = []

    # The loop to compare each answer to the correct answer
    for index in range(len(correct_answers)):
        if student_answers[index] == correct_answers[index]:
            correct_count += 1
        else:
            incorrect_count += 1
            incorrect_questions.append(index + 1) # Add the question number to the list of incorrect questions

    # Determine if the student passed or failed
    if correct_count >= 15:
        print("Congratulations! You passed the exam.")
    else:
        print("Sorry. You failed the exam.")

    # Print results
    print("Total Correct Answers:", correct_count)
    print("Total Incorrect Answers:", incorrect_count)
    print("Question Numbers For Incorrect Answers:", incorrect_questions)

# Call the main function
if __name__ == "__main__":
    main()