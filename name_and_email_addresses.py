# 10/01/2025
# NAME AND EMAIL ADDRESSES

import pickle

DATA_FILE = 'information.pkl'

def load_stuff():
    # Dictionary to hold the information
    information = {} 

    try:
        # Open the file for binary reading
        with open(DATA_FILE, 'rb') as input_file:
            information = pickle.load(input_file) 

    except FileNotFoundError:
        print("Data File Not Found")
        
    # Return the dictionary
    return information 

def save_stuff(information):
    # Open the file for binary writing
    with open(DATA_FILE, 'wb') as output_file:
        pickle.dump(information, output_file)

def do_lookup(information):
    # Get user input and normalize it by stripping spaces and converting to lowercase
    name_to_find = input("Enter Name: ").strip().lower() 
    
    # Check if the normalized name is in the dictionary
    if name_to_find in information:
        print(name_to_find + ": " + information[name_to_find])
    else:
        print(name_to_find + " Not Found")

def do_add(information):
    # Get user input and normalize it by stripping spaces and converting to lowercase
    new_name = input("Enter Name: ").strip().lower()
    new_email = input("Enter Email Address: ")

    # Check if the normalized name is in the dictionary
    if new_name in information:
        print("This Person Already Exists")
    else:
        information[new_name] = new_email
        print(new_name + " Has Been Added")
    
    return information # Send the dictionary back to main()

def do_change(information):
    # Get user input and normalize it by stripping spaces and converting to lowercase
    name_to_change = input("Enter Name: ").strip().lower()

    # Check if the normalized name is in the dictionary
    if name_to_change in information:
        print("Current Email Address: " + information[name_to_change])
        new_email = input("Enter New Email Address: ")
        information[name_to_change] = new_email
        print(name_to_change + " Has Been Changed")
    else:
        print(name_to_change + " Not Found")
    
    return information # Send the dictionary back to main()

def do_delete(information):
    # Get user input and normalize it by stripping spaces and converting to lowercase
    name_to_delete = input("Enter Name: ").strip().lower()

    # Check if the normalized name is in the dictionary
    if name_to_delete in information:
        del information[name_to_delete]
        print(name_to_delete + " Has Been Deleted")
    else:
        print(name_to_delete + " Not Found")
    
    return information # Send the dictionary back to main()


def main():    
    information = load_stuff()

    while True:
        print("1: Look Up a Person's Email Address")
        print("2: Add a New Name and Email Address")
        print("3: Change an Existing Email Address")
        print("4: Delete an Existing Name and Email Address")
        print("5: Quit and Save")
        
        user_choice = input("Type a Number (1-5) and Hit Enter: ")
        
        if user_choice == '1':
            do_lookup(information)
        elif user_choice == '2':
            information = do_add(information) 
        elif user_choice == '3':
            information = do_change(information) 
        elif user_choice == '4':
            information = do_delete(information) 
        elif user_choice == '5':
            save_stuff(information)
            break
        else:
            print("Try Again. Type a Number (1-5) and Hit Enter: ")

# Call the main function
if __name__ == "__main__":
    main()