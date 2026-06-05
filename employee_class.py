# 10/08/2025
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

def main():
    # Employee object for Susan Meyers
    emp1 = Employee("Susan Meyers", "47899", "Accounting", "Vice President")

    # Employee object for Mark Jones
    emp2 = Employee("Mark Jones", "39119", "IT", "Programmer")

    # Employee object for Joy Rogers
    emp3 = Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

    # Print employee information for Susan Meyers
    emp1.display_info()

    # Print employee information for Mark Jones
    emp2.display_info()

    # Print employee information for Joy Rogers
    emp3.display_info()

# Call the main function
if __name__ == '__main__':
    main()