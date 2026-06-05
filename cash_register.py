# 10/15/2025
# CASH REGISTER

# RETAILITEM CLASS
class RetailItem:
    def __init__(self, d, u, p):
        self.description = d
        self.units_in_inventory = u
        self.price = p

    # This method prints the retail item along with it's inventory and price
    def __str__(self):
        return self.description + " has " + str(self.units_in_inventory) + " units, selling for $" + str(self.price)

# CASHREGISTER CLASS
class CashRegister:
    # The list to hold the stuff being bought
    def __init__(self):
        self.shopping_list = []

    def purchase_item(self, item_to_buy):
        # Add the item object to the list
        self.shopping_list.append(item_to_buy)
        print("ADDED: " + item_to_buy.description)

    def get_total(self):
        # Add up all the prices
        total_price = 0.0
        for item in self.shopping_list:
            total_price = total_price + item.price
        return total_price

    def show_items(self):
        # Loop through and print what was bought
        if len(self.shopping_list) == 0:
            print("Your Shopping Cart is Empty.")
            return

        item_number = 1
        for item in self.shopping_list:
            # Calls original __str__ method here
            print(str(item_number) + ". " + str(item)) 
            item_number = item_number + 1


    def clear(self):
        # Clear the list
        self.shopping_list = []

# DEMONSTRATION PROGRAM
def main():
    # Create RetailItem objects
    item1 = RetailItem("Jacket", 12, 59.95)
    item2 = RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem("Shirt", 20, 24.95)

    # Dictionary with available items
    available = {
        '1': item1,
        '2': item2,
        '3': item3
    }

    # Create CashRegister object
    my_register = CashRegister()
    
    while True:
        print("1. Buy Jacket ($59.95)")
        print("2. Buy Designer Jeans ($34.95)")
        print("3. Buy Shirt ($24.95)")
        print("4. CHECK OUT")
        
        choice = input("Enter a Choice: ").strip()

        if choice in available:
            # Add the item to the list
            my_register.purchase_item(available[choice])
        
        elif choice == '4':
            # Show everything
            my_register.show_items()
            
            # Get the total
            final_total = my_register.get_total()
            print("TOTAL PRICE IS: $" + str(final_total))
            
            # Clear the list
            my_register.clear()
            
        else:
            print("That Was Not a Valid Choice. Try Again.")

# Call the main function
if __name__ == '__main__':
    main()