# 10/29/2025
# PROPERTY TAX

import tkinter
import tkinter.messagebox

class MyGUI:
    # Constants
    ASSESSMENT_RATE = 0.60    # 60% assessment
    TAX_RATE_PER_100 = 0.75   # $0.75 tax for each $100 of assessed value

    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        
        # Create label for the main window
        self.main_window.title("Property Tax")
        
        # Set up variables to hold the input and output
        self.value_var = tkinter.StringVar()
        self.assessment_result_var = tkinter.StringVar()
        self.tax_result_var = tkinter.StringVar()
        self.assessment_result_var.set("")
        self.tax_result_var.set("")

        # Create frame for actual value
        value_frame = tkinter.Frame(self.main_window)
        
        # Create label for actual value
        value_label = tkinter.Label(value_frame, text="Actual Value:")
        
        # Create entry box for actual value
        value_entry = tkinter.Entry(value_frame, textvariable=self.value_var, width=15)

        # Create frame for assessment
        assessment_frame = tkinter.Frame(self.main_window)
        
        # Create label for assessment
        assessment_desc_label = tkinter.Label(assessment_frame, text="Assessment Value:")
        
        # Create label for assessment result
        self.assessment_label = tkinter.Label(assessment_frame, textvariable=self.assessment_result_var)

        # Create frame for property tax
        tax_frame = tkinter.Frame(self.main_window)
        
        # Create label for property tax
        tax_desc_label = tkinter.Label(tax_frame, text="Property Tax:")
        
        # Create label for property tax result
        self.tax_label = tkinter.Label(tax_frame, textvariable=self.tax_result_var)

        # Create button to calculate tax
        calc_button = tkinter.Button(self.main_window, text="Calculate", command=self.calculate_property_tax)

        # Create button to quit
        quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)
        
        # Pack elements in the Actual Value Frame
        value_label.pack(side='left', padx=(0, 10))
        value_entry.pack(side='right')

        # Pack elements in the Assessment Frame
        assessment_desc_label.pack(side='left', padx=(0, 10))
        self.assessment_label.pack(side='right')

        # Pack elements in the Property Tax Frame
        tax_desc_label.pack(side='left', padx=(0, 10))
        self.tax_label.pack(side='right')

        # Pack the main frames and buttons
        value_frame.pack(pady=5, padx=10)
        assessment_frame.pack(pady=5, padx=10)
        tax_frame.pack(pady=5, padx=10)
        calc_button.pack(pady=10)
        quit_button.pack(pady=5)
        
    def calculate_property_tax(self):
        try:
            # Get and validate actual value input
            actual_value_str = self.value_var.get().replace(',', '').strip()
            if not actual_value_str:
                 tkinter.messagebox.showerror("Input Error", "Please enter a value for the property.")
                 return

            actual_value = float(actual_value_str)

            if actual_value < 0:
                tkinter.messagebox.showerror("Input Error", "The actual property value must be non-negative.")
                self.assessment_result_var.set("")
                self.tax_result_var.set("")
                return

            # Calculate Assessment Value (60% of actual value)
            assessment_value = actual_value * self.ASSESSMENT_RATE

            # Calculate Property Tax ($0.75 per $100 of assessment value)
            taxable_units = assessment_value / 100.0
            property_tax = taxable_units * self.TAX_RATE_PER_100

            # Format and update output variables
            self.assessment_result_var.set(f"${assessment_value:,.2f}")
            self.tax_result_var.set(f"${property_tax:,.2f}")

        except ValueError:
            tkinter.messagebox.showerror("Input Error", "Please enter a valid numeric value for the property.")

if __name__ == '__main__':
    # Create an instance of the class and start the main loop
    instance = MyGUI()
    instance.main_window.mainloop()