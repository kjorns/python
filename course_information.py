# 09/24/2025
# COURSE INFORMATION

def main():
    # Dictionary #1: Course Numbers (Key) & Room Numbers (Value)
    room_numbers = {
        'CS101': '3004',
        'CS102': '4501',
        'CS103': '6755',
        'NT110': '1244',
        'CM241': '1411'
    }

    # Dictionary #2: Course Numbers (Key) & Instructors (Value)
    instructors = {
        'CS101': 'Haynes',
        'CS102': 'Alvarado',
        'CS103': 'Rich',
        'NT110': 'Burke',
        'CM241': 'Lee'
    }

    # Dictionary #3: Course Numbers (Key) & Meeting Times (Value)
    meeting_times = {
        'CS101': '8:00 a.m.',
        'CS102': '9:00 a.m.',
        'CS103': '10:00 a.m.',
        'NT110': '11:00 a.m.',
        'CM241': '1:00 p.m.'
    }

    # Tell the user to enter a course number
    course_number = input("Enter a Course Number: ").upper() # upper() is used so that they can type in lowercase too

    # Check if the user entered course number exists in the dictionaries
    if course_number in room_numbers and course_number in instructors and course_number in meeting_times:
        room_number = room_numbers.get(course_number)
        instructor = instructors.get(course_number)
        meeting_time = meeting_times.get(course_number)
        
        # Print results
        print("Course Number:", course_number)
        print("Room Number:", room_number)
        print("Instructor:", instructor)
        print("Meeting Time:", meeting_time)
    else:
        # If the user entered course number does not exist in the dictionaries display this message
        print("Course Number Not Found")

# Call the main function
if __name__ == "__main__":
    main()