#10/22/2025
# EMPLOYEE AND PRODUCTIONWORKER CLASSES

class Employee:
    # Initialize the object
    def __init__(self, name_in, number_in):
        self.__employee_name = name_in
        self.__employee_number = number_in

    # Mutators for attributes
    def set_name(self, new_name):
        self.__employee_name = new_name

    def set_number(self, new_number):
        self.__employee_number = new_number

    # Accessors for attributes
    def get_name(self):
        return self.__employee_name

    def get_number(self):
        return self.__employee_number

class ProductionWorker(Employee):
    # Initialize the object
    def __init__(self, name_in, number_in, shift_num_in, pay_in):
        # Call the superclass __init__ method
        Employee.__init__(self, name_in, number_in)
        
        # Initialize the specialized attributes
        self.__shift_number = shift_num_in
        self.__hourly_pay = pay_in

    # Mutators for attributes
    def set_shift_number(self, new_shift):
        self.__shift_number = new_shift

    def set_pay_rate(self, new_pay):
        self.__hourly_pay = new_pay

    # Accessors for attributes

    def get_shift_number(self):
        return self.__shift_number

    def get_pay_rate(self):
        return self.__hourly_pay

    def get_shift_name(self):
        # Figure out if it is day or night
        if self.__shift_number == 1:
            return "Day Shift"
        elif self.__shift_number == 2:
            return "Night Shift"
        else:
            # Handle unexpected shift number
            return "Unknown Shift"


def main():
    # Get Employee info
    name = input("Employee Name: ")
    num = input("Employee Number: ")
    
    # Get Production Worker info
    shift = int(input("Shift Number: (1 for Day, 2 for Night): "))
    pay = float(input("Hourly Pay Rate: "))
    
    # Create the object
    production_worker_object = ProductionWorker(name, num, shift, pay)

    # Display the results
    print('Production Worker Information')
    print('-----------------------------')
    print("Name:", production_worker_object.get_name())
    print("Employee Number:", production_worker_object.get_number())
    print("Shift:", production_worker_object.get_shift_name())
    print(f"Hourly Pay: ${production_worker_object.get_pay_rate():.2f}")

# Call the main function
if __name__ == "__main__":
    main()