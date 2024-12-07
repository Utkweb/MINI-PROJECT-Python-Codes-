import tkinter as tk
from tkinter import ttk

# Conversion factors
CONVERSIONS = {
    "Length": {
        "Meters to Feet": lambda x: x * 3.28084,
        "Feet to Meters": lambda x: x / 3.28084,
        "Kilometers to Miles": lambda x: x * 0.621371,
        "Miles to Kilometers": lambda x: x / 0.621371,
        "Centimeters to Inches": lambda x: x * 0.393701,
        "Inches to Centimeters": lambda x: x / 0.393701,
    },
    "Weight": {
        "Kilograms to Pounds": lambda x: x * 2.20462,
        "Pounds to Kilograms": lambda x: x / 2.20462,
        "Grams to Ounces": lambda x: x * 0.035274,
        "Ounces to Grams": lambda x: x / 0.035274,
        "Tonnes to Pounds": lambda x: x * 2204.62,
        "Pounds to Tonnes": lambda x: x / 2204.62,
    },
    "Temperature": {
        "Celsius to Fahrenheit": lambda x: x * 9 / 5 + 32,
        "Fahrenheit to Celsius": lambda x: (x - 32) * 5 / 9,
        "Celsius to Kelvin": lambda x: x + 273.15,
        "Kelvin to Celsius": lambda x: x - 273.15,
        "Fahrenheit to Kelvin": lambda x: (x - 32) * 5 / 9 + 273.15,
        "Kelvin to Fahrenheit": lambda x: (x - 273.15) * 9 / 5 + 32,
    },
}

# Conversion function
def convert_units():
    try:
        value = float(entry_value.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        conversion_type = conversion_type_var.get()
        conversion_key = f"{from_unit} to {to_unit}"

        # Check for valid conversion
        if conversion_type in CONVERSIONS and conversion_key in CONVERSIONS[conversion_type]:
            result = CONVERSIONS[conversion_type][conversion_key](value)
            result_label.config(text=f"Result: {result:.2f}")
        else:
            result_label.config(text="Error: Invalid Conversion")
    except ValueError:
        result_label.config(text="Error: Invalid Input")

# Clear fields function
def clear_fields():
    entry_value.delete(0, tk.END)
    result_label.config(text="Result: ")

# Main window setup
root = tk.Tk()
root.title("Unit Converter")

# Conversion type dropdown
conversion_type_var = tk.StringVar()
conversion_type_var.set("Length")
conversion_type_label = tk.Label(root, text="Conversion Type:")
conversion_type_label.grid(row=0, column=0, padx=10, pady=10)
conversion_type_dropdown = ttk.Combobox(
    root, textvariable=conversion_type_var, values=list(CONVERSIONS.keys())
)
conversion_type_dropdown.grid(row=0, column=1, padx=10, pady=10)

# Input field
entry_label = tk.Label(root, text="Value:")
entry_label.grid(row=1, column=0, padx=10, pady=10)
entry_value = tk.Entry(root)
entry_value.grid(row=1, column=1, padx=10, pady=10)

# From unit dropdown
from_unit_var = tk.StringVar()
from_unit_label = tk.Label(root, text="From Unit:")
from_unit_label.grid(row=2, column=0, padx=10, pady=10)
from_unit_dropdown = ttk.Combobox(root, textvariable=from_unit_var)
from_unit_dropdown.grid(row=2, column=1, padx=10, pady=10)

# To unit dropdown
to_unit_var = tk.StringVar()
to_unit_label = tk.Label(root, text="To Unit:")
to_unit_label.grid(row=3, column=0, padx=10, pady=10)
to_unit_dropdown = ttk.Combobox(root, textvariable=to_unit_var)
to_unit_dropdown.grid(row=3, column=1, padx=10, pady=10)

# Update units based on conversion type
def update_units(*args):
    conversion_type = conversion_type_var.get()
    if conversion_type in CONVERSIONS:
        units = {key.split(" to ")[0] for key in CONVERSIONS[conversion_type].keys()}
        from_unit_dropdown["values"] = list(units)
        to_unit_dropdown["values"] = list(units)
        from_unit_var.set("")
        to_unit_var.set("")

conversion_type_var.trace("w", update_units)
update_units()

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_units)
convert_button.grid(row=4, column=0, columnspan=2, pady=10)

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=5, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
