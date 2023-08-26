import tkinter as tk
import mysql.connector

# Connect to the database

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cur = conn.cursor(buffered=True)

try:
    cur.execute("use registration")
except:
    cur.execute("create database registration")
    cur.execute("use registration")

try:
    cur.execute("describe register")
except:
    cur.execute("create table register(id int primary key auto_increment, fname varchar(20), lname varchar(20), age int, email varchar(20), mobile varchar(20))")

def Registration():
    fname = e1.get()
    lname = e2.get()
    age = e3.get()
    email = e4.get()
    mobile = e5.get()
    
    query = "insert into register(fname, lname, age, email, mobile) values (%s, %s, %s, %s, %s)"
    values = (fname, lname, age, email, mobile)
    
    try:
        cur.execute(query, values)
        conn.commit()
        print("Data inserted successfully!")
    except Exception as e:
        print("Error:", e)
        conn.rollback()

win = tk.Tk()
win.geometry("400x400")
win.title("Registration Form")

tk.Label(win, text="Registration Form", font=("Helvetica", 16, "bold")).grid(row=0, column=1, pady=10, columnspan=2)

labels = ["First Name", "Last Name", "Age", "Email", "Mobile No."]
entry_fields = []

for i, label_text in enumerate(labels, start=1):
    tk.Label(win, text=label_text).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(win)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entry_fields.append(entry)

submit_button = tk.Button(win, text="Submit", command=Registration)
submit_button.grid(row=len(labels) + 1, column=1, pady=20)

win.mainloop()
