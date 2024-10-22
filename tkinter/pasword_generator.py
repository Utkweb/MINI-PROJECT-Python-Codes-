import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password
def generate_password():
    length = password_length_slider.get()
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()

    if not (include_uppercase or include_lowercase or include_numbers or include_symbols):
        messagebox.showwarning("Selection Error", "Select at least one option!")
        return
    
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_output.delete(0, tk.END)
    password_output.insert(0, password)

# Function to copy the password to the clipboard
def copy_to_clipboard():
    password = password_output.get()
    if password:
        app.clipboard_clear()  # Clear the clipboard first
        app.clipboard_append(password)  # Append the password to the clipboard
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Copy Error", "No password to copy!")

# Create the main application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x300")

# Password length slider
tk.Label(app, text="Password Length:").pack()
password_length_slider = tk.Scale(app, from_=8, to=32, orient="horizontal")
password_length_slider.pack()

# Checkboxes for character options
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(app, text="Include Uppercase Letters", variable=uppercase_var).pack()
tk.Checkbutton(app, text="Include Lowercase Letters", variable=lowercase_var).pack()
tk.Checkbutton(app, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(app, text="Include Symbols", variable=symbols_var).pack()

# Button to generate the password
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Entry widget to display the generated password
password_output = tk.Entry(app, width=40, font=("Helvetica", 12))
password_output.pack(pady=10)

# Copy button to copy the password to clipboard
copy_button = tk.Button(app, text="Copy Password", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Run the application
app.mainloop()


