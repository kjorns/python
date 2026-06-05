# 11/05/2025
# LONG-DISTANCE CALLS

import tkinter
import tkinter.messagebox

class MyGUI:
    # Define constants
    RATES = {
        "daytime": {"label": "Daytime (6AM - 5:59PM) ($0.07/min)", "rate": 0.07},
        "evening": {"label": "Evening (6PM - 11:59PM) ($0.12/min)", "rate": 0.12},
        "off_peak": {"label": "Off-Peak (Midnight - 5:59AM) ($0.05/min)", "rate": 0.05}
    }

    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Long-Distance Calls")
        
        # Set up variables to hold the input and output
        self.minutes_var = tkinter.StringVar()       # Input for minutes
        self.rate_choice_var = tkinter.StringVar()   # Input for selected radio button key
        self.rate_display_var = tkinter.StringVar()  # Output for name of the selected rate
        self.charge_result_var = tkinter.StringVar() # Output for final calculated charge

        # Set initial values
        self.rate_choice_var.set("daytime") # Default to the 'daytime' rate
        self.minutes_var.set("")
        self.rate_display_var.set("")
        self.charge_result_var.set("")
        
        # Frame 1: Minutes Input
        minutes_frame = tkinter.Frame(self.main_window)
        minutes_label = tkinter.Label(minutes_frame, text="Call Duration (Minutes):")
        minutes_entry = tkinter.Entry(minutes_frame, textvariable=self.minutes_var)

        # Frame 2: Rate Selection Area
        rate_title_label = tkinter.Label(self.main_window, text="Select Rate Category:")
                                         
        rate_select_frame = tkinter.Frame(self.main_window)
        
        # Create Radio Buttons for each rate category
        for key, data in self.RATES.items():
            # Create the radio button
            radio_button = tkinter.Radiobutton(rate_select_frame, text=data["label"], variable=self.rate_choice_var, value=key)
            # Pack the radio button
            radio_button.pack()
                                
        # Frame 3: Selected Rate Display
        rate_display_frame = tkinter.Frame(self.main_window)
        rate_desc_label = tkinter.Label(rate_display_frame, text="Selected Rate:")
        self.rate_label = tkinter.Label(rate_display_frame, textvariable=self.rate_display_var)

        # Frame 4: Final Charge Display
        charge_frame = tkinter.Frame(self.main_window)
        charge_desc_label = tkinter.Label(charge_frame, text="Total Call Charge:")
        self.charge_label = tkinter.Label(charge_frame, textvariable=self.charge_result_var)

        # Create button to calculate
        calc_button = tkinter.Button(self.main_window, text="Calculate Charge", command=self.calculate_call_charge)

        # Create button to quit
        quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)
        
        # Pack elements inside the frames
        minutes_label.pack()
        minutes_entry.pack()
        
        rate_desc_label.pack()
        self.rate_label.pack()

        charge_desc_label.pack()
        self.charge_label.pack()

        # Pack the main frames and related components
        minutes_frame.pack()
        rate_title_label.pack()
        rate_select_frame.pack()
        rate_display_frame.pack()
        charge_frame.pack()
        calc_button.pack()
        quit_button.pack()
        
    def calculate_call_charge(self):
        try:
            # Get and validate minutes input
            minutes_str = self.minutes_var.get().strip()
            if not minutes_str:
                 tkinter.messagebox.showerror("Input Error", "Please enter the call duration in minutes.")
                 return

            minutes = float(minutes_str)

            # Get the selected rate data
            rate_key = self.rate_choice_var.get()
            rate_data = self.RATES.get(rate_key)
            
            rate_per_min = rate_data["rate"]
            rate_label = rate_data["label"]

            # Calculate Total Charge
            total_charge = minutes * rate_per_min

            # Format and update output variables
            self.rate_display_var.set(rate_label)
            self.charge_result_var.set(f"${total_charge:,.2f}")

        except ValueError:
            tkinter.messagebox.showerror("Input Error", "Please enter a valid numeric value for minutes.")
            self.rate_display_var.set("")
            self.charge_result_var.set("")


if __name__ == '__main__':
    # Create an instance of the class and start the main loop
    instance = MyGUI()
    instance.main_window.mainloop()