# 10/29/2025
# MILES PER GALLON CALCULATOR

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create label for the main window
        self.main_window.title("Miles Per Gallon Calculator")

        # Set up variables to hold the input and output
        self.gallons_var = tkinter.StringVar()
        self.miles_var = tkinter.StringVar()
        self.mpg_result_var = tkinter.StringVar()
        self.mpg_result_var.set("")
        
        # Create frame for gallons
        gallons_frame = tkinter.Frame(self.main_window)

        # Create label for gallons
        gallons_label = tkinter.Label(gallons_frame, text="Gallons tank holds:")

        # Create entry box for gallons
        gallons_entry = tkinter.Entry(gallons_frame, textvariable=self.gallons_var, width=15)

        # Create frame for miles
        miles_frame = tkinter.Frame(self.main_window)

        # Create label for miles
        miles_label = tkinter.Label(miles_frame, text="Miles driven on full tank:")

        # Create entry box for miles
        miles_entry = tkinter.Entry(miles_frame, textvariable=self.miles_var, width=15)

        # Create button to calculate MPG
        calc_button = tkinter.Button(self.main_window, text="Calculate MPG", command=self.calculate_mpg)

        # Create label to show the result
        self.result_label = tkinter.Label(self.main_window, textvariable=self.mpg_result_var)
        
        # Create button to quit
        quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        # Pack elements in the Gallons Frame
        gallons_label.pack(side='left', padx=(0, 10))
        gallons_entry.pack(side='right')

        # Pack elements in the Miles Frame
        miles_label.pack(side='left', padx=(0, 10))
        miles_entry.pack(side='right')

        # Pack the main frames and buttons
        gallons_frame.pack(pady=5, padx=10)
        miles_frame.pack(pady=5, padx=10)
        calc_button.pack(pady=10)
        self.result_label.pack(pady=10)
        quit_button.pack(pady=5)


    def calculate_mpg(self):
        try:
            # Get and convert input values
            gallons = float(self.gallons_var.get())
            miles = float(self.miles_var.get())

            # Make sure gallons is not zero
            if gallons <= 0:
                tkinter.messagebox.showerror("Input Error", "The number of gallons must be greater than zero.")
                self.mpg_result_var.set("")
                return

            # Calculate MPG
            mpg = miles / gallons

            # Display the result, formatted to two decimal places
            self.mpg_result_var.set(f"MPG: {mpg:.2f}")

        except ValueError:
            tkinter.messagebox.showerror("Input Error", "Please enter valid numeric values for both fields.")
            self.mpg_result_var.set("")


if __name__ == '__main__':
    # Create an instance of the class and start the main loop
    instance = MyGUI()
    instance.main_window.mainloop()