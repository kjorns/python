# 11/12/2025
# POPULATION DATABASE

# FOLLOWED ALONG WITH VIDEONOTE 14-6

import sqlite3

# Main Function
def main():
    # Menu Choice
    choice = 0

    # Connect to the Database
    conn = sqlite3.connect('cities.db')

    # Get a Database Cursor
    cur = conn.cursor()

    # Get the User's Menu Choice
    while choice != 8:
        choice = get_menu_choice()
        execute_choice(choice, cur)

    # Close the Connection
    conn.close()

# The Display Menu Function Displays a Menu
def display_menu():
    print('                                 MENU                                 ')
    print('----------------------------------------------------------------------')
    print('1 - Display a List of Cities Sorted By Population, in Ascending Order')
    print('2 - Display a List of Cities Sorted By Population, in Descending Order')
    print('3 - Display a List of Cities Sorted By Name')
    print('4 - Display the Total Population of All the Cities')
    print('5 - Display the Average Population of All the Cities')
    print('6 - Display the City With the Highest Population')
    print('7 - Display the City With the Lowest Population')
    print('8 - EXIT')

# The Get Menu Choice Function Displays the Menu and Gets the User's Choice
def get_menu_choice():
    display_menu()
    choice = int(input('Enter Your Choice: '))
    # Validate The Choice
    while choice < 1 or choice > 8:
        choice = int(input('Enter a Valid Choice: '))
    return choice
    
# Perform the Action that the User Selected
def execute_choice(choice, cur):
    if choice == 1:
        cities_sorted_ascending(cur)
    elif choice == 2:
        cities_sorted_descending(cur)
    elif choice == 3:
        cities_sorted_by_name(cur)
    elif choice == 4:
        total_population(cur)
    elif choice == 5:
        average_population(cur)
    elif choice == 6:
        highest_population(cur)
    elif choice == 7:
        lowest_population(cur)

# Display a List of Cities Sorted By Population, in Ascending Order
def cities_sorted_ascending(cur):
    # Execute the SELECT Statement on the Database
    cur.execute('''SELECT CityName, Population
                   FROM Cities
                   ORDER BY Population''')
    
    # Fetch the Results
    results = cur.fetchall()

    # Display the Results
    print('\nCities Sorted By Population in Ascending Order')
    display_results(results)

# Display a List of Cities Sorted By Population, in Descending Order
def cities_sorted_descending(cur):
    # Execute the SELECT Statement on the Database
    cur.execute('''SELECT CityName, Population
                   FROM Cities
                   ORDER BY Population DESC''')
    
    # Fetch the Results
    results = cur.fetchall()

    # Display the Results
    print('\nCities Sorted By Population in Descending Order')
    display_results(results)

# Display a List of Cities Sorted By Name
def cities_sorted_by_name(cur):
    # Execute the SELECT Statement on tHE Database
    cur.execute('''SELECT CityName, Population
                   FROM Cities
                   ORDER BY CityName''')
    
    # Fetch the Results
    results = cur.fetchall()

    # Display the Results
    print('\nCities Sorted By Name')
    display_results(results)

# Display the Total Population of All the Cities
def total_population(cur):
    # Execute the SELECT Statement on the Database
    cur.execute('SELECT SUM(Population) FROM Cities')

    # Fetch the Results
    results = cur.fetchone()

    # Display the Results
    print(f'\nTotal Population: {results[0]:,.0f}\n')

# Display the Average Population of All the Cities
def average_population(cur):
    # Execute the SELECT Statement on the Database
    cur.execute('SELECT AVG(Population) FROM Cities')

    # Fetch the Results
    results = cur.fetchone()

    # Display the Results
    print(f'\nAverage Population: {results[0]:,.0f}\n')

# Display the City With the Highest Population
def highest_population(cur):
    # Get the Highest Value in the Population Column
    cur.execute('SELECT MAX(Population) FROM Cities')

    # Fetch the Results
    max_results = cur.fetchone()

    # Get the Entire Row that Contains that Population
    cur.execute('''SELECT CityName, Population FROM Cities
                   WHERE Population = ?''', (max_results[0],))
    
    # Fetch the Results
    results = cur.fetchone()

    # Display the Results
    print(f'\n{results[0]} has the Highest Population: {results[1]:,.0f}\n')

# Display the City With the Lowest Population
def lowest_population(cur):
    # Get the Lowest Value in the Population Column
    cur.execute('SELECT MIN(Population) FROM Cities')

    # Fetch the Results
    min_results = cur.fetchone()

    # Get the Entire Row that Contains that Population
    cur.execute('''SELECT CityName, Population FROM Cities
                   WHERE Population = ?''', (min_results[0],))
    
    # Fetch the Results
    results = cur.fetchone()

    # Display the Results
    print(f'\n{results[0]} has the Lowest Population: {results[1]:,.0f}\n')

# The Display Results Function Displays the Values in the Results of a SELECT Statement
def display_results(results):
    print(f'{"City":20}{"Population"}')
    for row in results:
        print(f'{row[0]:20}{row[1]:,.0f}')
    print()

# Execute the Main Function
if __name__ == '__main__':
    main()