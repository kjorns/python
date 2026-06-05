# 11/05/2025
# JOE'S AUTOMOTIVE

import tkinter

class MyGUI:
    # Define constants
    SERVICES = {
        "Oil Change": 30.00,
        "Lube Job": 20.00,
        "Radiator Flush": 40.00,
        "Transmission Flush": 100.00,
        "Inspection": 35.00,
        "Muffler Replacement": 200.00,
        "Tire Rotation": 20.00
    }

    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive")
        
        # Dictionary to hold IntVar for each check button
        self.service_vars = {} 
        
        # Set up variable for the output total
        self.total_result_var = tkinter.StringVar() 
        self.total_result_var.set("$0.00") # Set initial value

        # Frame 1: Service Selection
        self.service_frame = tkinter.Frame(self.main_window)
        
        # Create and pack the check buttons
        for service, price in self.SERVICES.items():
            # 0 = unchecked, 1 = checked
            var = tkinter.IntVar(value=0)
            self.service_vars[service] = var
            
            display_text = f"{service} (${price:.2f})"
            
            # Create the Checkbutton
            chk = tkinter.Checkbutton(self.service_frame, text=display_text, variable=var)
            
            chk.pack()

        # Frame 2: Total Display
        self.total_frame = tkinter.Frame(self.main_window)
        
        # Total description label
        total_desc_label = tkinter.Label(self.total_frame, text="Total Charges:")
        
        # Total result label
        self.total_label = tkinter.Label(self.total_frame, textvariable=self.total_result_var)

        # Pack elements in the Total Display Frame
        total_desc_label.pack()
        self.total_label.pack()

        # Frame 3: Button
        self.button_frame = tkinter.Frame(self.main_window)
        
        # Create button to calculate 
        calc_button = tkinter.Button(self.button_frame, text="Calculate Total", command=self.update_total)

        # Create button to quit
        quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.main_window.destroy)

        # Pack elements in the Button Frame
        calc_button.pack()
        quit_button.pack()
        
        # Pack the main frames in the main window
        self.service_frame.pack()
        self.total_frame.pack()
        self.button_frame.pack()
        
    def update_total(self):
        total_charge = 0.0
        
        for service_name, var in self.service_vars.items():
            # The get() method returns 1 if checked, 0 if unchecked
            if var.get() == 1:
                price = self.SERVICES[service_name]
                total_charge += price
                
        # Update total display
        self.total_result_var.set(f"${total_charge:,.2f}")

if __name__ == "__main__":
    # Create an instance of the class and start the main loop
    instance = MyGUI()
    instance.main_window.mainloop()