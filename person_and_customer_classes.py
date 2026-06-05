# 10/22/2025
# PERSON AND CUSTOMER CLASSES

# FOLLOWED ALONG WITH VIDEONOTE 11-1

class Person:
    #Initialize the object
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    # Mutator for the __name attribute
    def set_name(self, name):
        self.__name = name

    # Mutator for the __address attribute
    def set_address(self, address):
        self.__address = address

    # Mutator for the __phone attribute
    def set_phone(self, phone):
        self.__phone = phone

    # Accessor for the __name attribute
    def get_name(self):
        return self.__name
    
    # Accessor for the __address attribute
    def get_address(self):
        return self.__address
    
    # Accessor for the __phone attribute
    def get_phone(self):
        return self.__phone
    
class Customer(Person):
    # Initialize the object
    def __init__(self, name, address, phone, customer_number, mailing_list):
        # Call the superclass __init__ method
        Person.__init__(self, name, address, phone)

        # Initialize the specialized attributes
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    # Mutator for the __customer_number attribute
    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    # Mutator for the __mailing_list attribute
    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

    # Accessor for the __customer_number attribute
    def get_customer_number(self):
        return self.__customer_number
    
    # Accessor for the __mailing_list attribute
    def get_mailing_list(self):
        return self.__mailing_list
    
# Get some customer information
name = input('Name: ')
address = input('Address: ')
phone = input('Phone: ')
customer_number = input('Customer Number: ')
mail = input('Include In Mailing List? (y/n): ')

# Determine True or False for mailing list
if mail.lower() == 'y':
    mailing_list = True
else:
    mailing_list = False

# Create an instance of the Customer class
my_customer = Customer(name, address, phone, customer_number, mailing_list)

# Display the object's data
print('Customer Information')
print('--------------------')
print('Name:', my_customer.get_name())
print('Address:', my_customer.get_address())
print('Phone:', my_customer.get_phone())
print('Customer Number:', my_customer.get_customer_number())
print('Mailing List:', my_customer.get_mailing_list())