# 10/29/2025
# CELSIUS TO FAHRENHEIT

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create label for the main window
        self.main_window.title("Celsius to Fahrenheit")

        # Set up variables to hold the input and output
        self.celsius_var = tkinter.StringVar()
        self.fahrenheit_result_var = tkinter.StringVar()
        self.fahrenheit_result_var.set("") 

        # Create frame for celsius input
        self.celsius_frame = tkinter.Frame(self.main_window)
        
        # Create frame for fahrenheit output
        self.result_frame = tkinter.Frame(self.main_window)

        # Create label for celsius input
        self.celsius_label = tkinter.Label(self.celsius_frame, text="Celsius (C):")

        # Create entry box for celsius input
        self.celsius_entry = tkinter.Entry(self.celsius_frame, textvariable=self.celsius_var)
        
        # Create button to convert
        self.convert_button = tkinter.Button(self.main_window, 
                                             text="Convert to F", command=self.convert_temperature)

        # Create label for fahrenheit output
        self.fahrenheit_static_label = tkinter.Label(self.result_frame, text="Fahrenheit (F):")

        # Create label for fahrenheit output result
        self.fahrenheit_display_label = tkinter.Label(self.result_frame, textvariable=self.fahrenheit_result_var)

        # Create button to quit
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)
        
        # Pack elements in the Celsius Frame
        self.celsius_label.pack(side='left', padx=(0, 10))
        self.celsius_entry.pack(side='right')

        # Pack elements in the Fahrenheit Frame
        self.fahrenheit_static_label.pack(side='left', padx=(0, 10))
        self.fahrenheit_display_label.pack(side='right')

        # Pack the main frames and buttons
        self.celsius_frame.pack(pady=10, padx=10)
        self.convert_button.pack(pady=15, padx=10)
        self.result_frame.pack(pady=10, padx=10)
        self.quit_button.pack(pady=10, padx=10)

    def convert_temperature(self):
        try:
            # Get and convert input
            celsius_input = float(self.celsius_var.get())

            # Apply the conversion formula: F = (9/5) * C + 32
            fahrenheit_output = (9.0 / 5.0) * celsius_input + 32.0

            # Display the result, formatted to two decimal places
            self.fahrenheit_result_var.set(f"{fahrenheit_output:.2f}")

        except ValueError:
            tkinter.messagebox.showerror("Input Error", "Please enter a valid number for the Celsius temperature.")

if __name__ == '__main__':
    # Create an instance of the class and start the main loop
    instance = MyGUI()
    instance.main_window.mainloop()