import tkinter as tk
from tkinter import ttk

exchange_rates = {
    "USD": {"EUR": 0.95, "INR": 84.48, "PES": 20.35, "GBP": 0.79},
    "INR": {"EUR": 0.0113, "USD": 0.012, "PES": 0.21, "GBP": 0.0098},
    "EUR": {"USD": 1.5, "INR": 88.89, "PES": 80.65, "GBP": 0.86},
    "GBP": {"PES": 22.64, "EUR": 1.15, "INR": 101.78, "USD": 1.22},
    "PES": {"GBP": 0.045, "USD": 0.056, "EUR": 0.052, "INR": 4.65}
}

root = tk.Tk()
root.title("Currency Converter")
root.geometry("600x600")

def currency_convertor():
    try:
        amount = float(entry.get())
        f_currency = from_currency.get()
        t_currency = to_currency.get()

        if f_currency == t_currency:
            converted_amount = amount
        else:
            converted_amount = amount * exchange_rates[f_currency][t_currency]
        result_label.config(text=f"{converted_amount}")
    except ValueError:
        result_label.config(text=f"Please enter a valid amount!")
    except KeyError:
        result_label.config(text=f"Conversion rate not available")

def swap_currencies():
    current_from = from_currency.get()
    current_to = to_currency.get()
    from_currency.set(current_to)
    to_currency.set(current_from)

title_label = tk.Label(root, text="Currency Conversion", font="Lobster")
title_label.pack()

amount_label = tk.Label(root, text="Enter your amount: ")
amount_label.pack()

entry = tk.Entry(root)
entry.pack()

converter = list(exchange_rates.keys())  # Convert all the conversions into a list
from_currency = tk.StringVar(value="USD")
to_currency = tk.StringVar(value="INR")

f_dropdown = tk.Label(root, text="Convert from")
f_dropdown.pack()
from_dropdown = ttk.Combobox(root, textvariable=from_currency, values=converter)
from_dropdown.pack()

t_dropdown = tk.Label(root, text="Converted to")
t_dropdown.pack()
to_dropdown = ttk.Combobox(root, textvariable=to_currency, values=converter)
to_dropdown.pack()

converter_button = tk.Button(root, text="Convert your currency", command=currency_convertor)
converter_button.pack()

swap_button = tk.Button(root, text="Swap Currencies", command=swap_currencies)
swap_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
