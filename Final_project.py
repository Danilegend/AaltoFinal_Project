import tkinter as tk
from tkinter import ttk

def convert():
    try:
        # Retrieve the input value from the user
        valueToConvert = float(entry1.get())
        fromUnit = from_unit.get()
        toUnit = to_unit.get()
        
        # Perform the conversion based on the selected units
        if fromUnit == "Celsius" and toUnit == "Fahrenheit":
            convertedValue = (valueToConvert * 9/5) + 32
        elif fromUnit == "Fahrenheit" and toUnit == "Celsius":
            convertedValue = (valueToConvert - 32) * 5/9
        elif fromUnit == "Kilometers" and toUnit == "Miles":
            convertedValue = valueToConvert * 0.621371
        elif fromUnit == "Miles" and toUnit == "Kilometers":
            convertedValue = valueToConvert / 0.621371
        else:
            # Handle invalid unit combinations
            raise ValueError("Invalid unit conversion combination.")
        
        # Display the converted value, rounded to two decimal places
        result.config(text=str(round(convertedValue, 2)))
    
    except ValueError as e:
        # Display error message if there's an issue with the input or conversion
        result.config(text=f"Error: {str(e)}")

# Create the main application window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("600x500")  # Set window size

# Centering the window on the screen
window_width = 600
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Add a title at the top of the window
title_label = tk.Label(root, text=" A!  Aalto Professional Diploma Final Project", font=("Helvetica", 30, "bold"))
title_label.pack(pady=20)

# Create a frame to contain the input fields and labels
frame = tk.Frame(root)
frame.pack(pady=15, padx=30)

# Styling labels for better readability
label_style = {"font": ("Helvetica", 25), "padx": 40, "pady": 20}

# Label and input for the value to convert
label1 = tk.Label(frame, text="Enter Value:",**label_style)
label1.grid(column=0, row=0, sticky="e")

entry1 = tk.Entry(frame, font=("Helvetica", 20), bd=2, relief="groove", width=21)
entry1.grid(column=1, row=0, padx=10, pady=1, ipady=5, sticky="w")
# Dropdown menu for selecting the "from" unit
label2 = tk.Label(frame, text="From:", **label_style)
label2.grid(column=0, row=1, sticky="e")

from_unit = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kilometers", "Miles"], font=("Helvetica", 20))
from_unit.grid(column=1, row=1, padx=5, pady=5, sticky="w")
from_unit.current(0)  # Set default value

# Dropdown menu for selecting the "to" unit
label3 = tk.Label(frame, text="To:", **label_style)
label3.grid(column=0, row=2, sticky="e")

to_unit = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kilometers", "Miles"], font=("Helvetica", 20))
to_unit.grid(column=1, row=2, padx=10, pady=5, sticky="w")
to_unit.current(1)  # Set default value

# Label for displaying the conversion result
result_label = tk.Label(frame, text="Result:", **label_style)
result_label.grid(column=0, row=3, sticky="e")

result = tk.Label(frame, text="", font=("Helvetica", 20, "bold"), fg="green", anchor="w")
result.grid(column=1, row=3, padx=10, pady=5, sticky="w")

# Convert button with enhanced styling

convert_button = tk.Button(root, text="Convert", command=lambda: convert(), font=("Helvetica", 20))
convert_button.pack(pady=20)

# Run the application
root.mainloop()
