# 10/15/2025
# EMPLOYEE MANAGEMENT SYSTEM

import pickle

DATA_FILE = 'employees.pkl'

# EMPLOYEE CLASS
class Employee:
    def __init__(self, n, i, d, j):
        self.name = n
        self.id_number = i
        self.department = d
        self.job_title = j

    # This method prints the employee information
    def display_info(self):
        print("Name:", self.name)
        print("ID Number:", self.id_number)
        print("Department:", self.department)
        print("Job Title:", self.job_title)

#def main():
    # Employee object for Susan Meyers
    #emp1 = Employee("Susan Meyers", "47899", "Accounting", "Vice President")

    # Employee object for Mark Jones
    #emp2 = Employee("Mark Jones", "39119", "IT", "Programmer")

    # Employee object for Joy Rogers
    #emp3 = Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

    # Print employee information for Susan Meyers
    #emp1.display_info()

    # Print employee information for Mark Jones
    #emp2.display_info()

    # Print employee information for Joy Rogers
    #emp3.display_info()

# Call the main function
#if __name__ == '__main__':
    #main()

def load_stuff():
    # Dictionary to hold the employee information
    employees = {} 

    try:
        # Open the file for binary reading
        with open(DATA_FILE, 'rb') as input_file:
            employees = pickle.load(input_file) 
            print("Employee Data Loaded")
    except FileNotFoundError:
        print("Data File Not Found")
        
    # Return the dictionary
    return employees 

def save_stuff(employees):
    # Open the file for binary writing
    with open(DATA_FILE, 'wb') as output_file:
        pickle.dump(employees, output_file)
    print("Employee Data Saved")

def do_lookup(employees):
    # Get user input
    emp_id = input("Enter Employee ID: ").strip() 
    
    # Check if the Employee ID is in the dictionary
    if emp_id in employees:
        employees[emp_id].display_info()
    else:
        print(f"Employee ID {emp_id} Not Found")

def do_add(employees):
    # Get user input for new Employee ID
    emp_id = input("Enter New Employee ID: ").strip()

    # Check if the Employee ID is in the dictionary
    if emp_id in employees:
        print("This Employee ID Already Exists")
        return employees 

    # Get user input for Name, Department, and Job Title
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    job_title = input("Enter Job Title: ")

    # Create the Employee object
    new_employee = Employee(name, emp_id, department, job_title)
    
    # Store the object in the dictionary
    employees[emp_id] = new_employee

    print(f"Employee {emp_id} ({name}) Has Been Added")
    
    return employees # Send the dictionary back to main()

def do_change(employees):
    # Get user input
    emp_id = input("Enter Employee ID: ").strip()

    # Check if the Employee ID is in the dictionary
    if emp_id in employees:
        employee = employees[emp_id] # Get the Employee object

        print(f"Current Name: {employee.name}")
        print(f"Current Department: {employee.department}")
        print(f"Current Job Title: {employee.job_title}")
        
        # Change Name
        new_name = input("Enter New Name: ")
        employee.name = new_name

        # Change Department
        new_department = input("Enter New Department: ")
        employee.department = new_department

        # Change Job Title
        new_job_title = input("Enter New Job Title: ")
        employee.job_title = new_job_title

        print(f"Employee ID {emp_id} Details Have Been Changed")
    else:
        print(f"Employee ID {emp_id} Not Found")
    
    return employees # Send the dictionary back to main()

def do_delete(employees):
    # Get user input
    emp_id = input("Enter Employee ID: ").strip()

    # Check if the Employee ID is in the dictionary
    if emp_id in employees:
        del employees[emp_id]
        print(f"Employee ID {emp_id} Has Been Deleted")
    else:
        print(f"Employee ID {emp_id} Not Found")
    
    return employees # Send the dictionary back to main()

def main(): 
    # Load the dictionary of Employee objects at startup  
    employees = load_stuff()

    while True:
        print("1: Look Up an Employee")
        print("2: Add a New Employee")
        print("3: Change an Employee's Details")
        print("4: Delete an Employee")
        print("5: Quit and Save")
        
        user_choice = input("Type a Number (1-5) and Hit Enter: ")
        
        if user_choice == '1':
            do_lookup(employees)
        elif user_choice == '2':
            employees = do_add(employees) 
        elif user_choice == '3':
            # Note: The 'do_change' function modifies the object IN PLACE
            # but we return the dictionary anyway, matching your original style.
            employees = do_change(employees) 
        elif user_choice == '4':
            employees = do_delete(employees) 
        elif user_choice == '5':
            save_stuff(employees)
            break
        else:
            print("Try Again. Type a Number (1-5) and Hit Enter: ")

# Call the main function
if __name__ == "__main__":
    main()