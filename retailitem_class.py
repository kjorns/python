# 10/08/2025
# RETAILITEM CLASS

class RetailItem:
    def __init__(self, d, u, p):
        self.description = d
        self.units_in_inventory = u
        self.price = p

    # This method prints the retail item along with it's inventory and price
    def __str__(self):
        return self.description + " has " + str(self.units_in_inventory) + " units, selling for $" + str(self.price)

def main():
    # Item 1: Jacket, 12 units, $59.95
    item_1 = RetailItem("Jacket", 12, 59.95)

    # Item 2: Designer Jeans, 40 units, $34.95
    item_2 = RetailItem("Designer Jeans", 40, 34.95)

    # Item 3: Shirt, 20 units, $24.95
    item_3 = RetailItem("Shirt", 20, 24.95)

    # Print information for Item 1
    print(item_1)

    # Print information for Item 2
    print(item_2)

    # Print information for Item 3
    print(item_3)

# Call the main function
if __name__ == '__main__':
    main()