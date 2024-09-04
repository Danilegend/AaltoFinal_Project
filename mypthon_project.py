import tkinter as tk
from tkinter import ttk

def convert():
    try:
        value = float(entry1.get())
        from_u = from_unit.get()
        to_u = to_unit.get()
        
        # Temperature conversion
        if from_u == "Celsius" and to_u == "Fahrenheit":
            converted_value = (value * 9/5) + 32
        elif from_u == "Fahrenheit" and to_u == "Celsius":
            converted_value = (value - 32) * 5/9
            
        # Distance conversion
        elif from_u == "Kilometers" and to_u == "Miles":
            converted_value = value * 0.621371
        elif from_u == "Miles" and to_u == "Kilometers":
            converted_value = value / 0.621371
        
        else:
            converted_value = "Invalid conversion"
        
        result.config(text=str(round(converted_value, 2)))
    
    except ValueError:
        result.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x250")  # Set window size

# Centering the window on the screen
window_width = 400
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Add a title at the top
title_label = tk.Label(root, text="Final Aalto Professional Diploma in Data Analytics Final Project", font=("Helvetica", 24, "bold"))
title_label.pack(pady=10)

# Create and place labels, entries, and buttons
frame = tk.Frame(root)
frame.pack(pady=10)

label1 = tk.Label(frame, text="Enter Value:")
label1.grid(column=0, row=0, padx=15, pady=15)

entry1 = tk.Entry(frame)
entry1.grid(column=1, row=0, padx=15, pady=15)

label2 = tk.Label(frame, text="From:")
label2.grid(column=0, row=1, padx=15, pady=15)

from_unit = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kilometers", "Miles"])
from_unit.grid(column=1, row=1, padx=15, pady=15)
from_unit.current(0)  # Set default value

label3 = tk.Label(frame, text="To:")
label3.grid(column=0, row=2, padx=15, pady=15)

to_unit = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kilometers", "Miles"])
to_unit.grid(column=1, row=2, padx=15, pady=15)
to_unit.current(1)  # Set default value

result_label = tk.Label(frame, text="Result:")
result_label.grid(column=0, row=3, padx=15, pady=15)

result = tk.Label(frame, text="")
result.grid(column=1, row=3, padx=15, pady=15)

convert_button = tk.Button(root, text="Convert", command=lambda: convert())
convert_button.pack(pady=20)

# Run the application
root.mainloop()
