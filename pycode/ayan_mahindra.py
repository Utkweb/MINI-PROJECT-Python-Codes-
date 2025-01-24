# // module - when you are importing something with the keyword 'import'

# // numpy - Working wiht the arrays (Numerical Python)


# import numpy as np 

# arr = np.array([1,2,3,4,5])

# print(arr)
# print(type(arr))

# 1d array -
# 2d array -

# import numpy as np 

# arr = np.array([[1,2,3],[5,8,9],[5,6,7]])

# print(arr)


# import numpy as np 

# arr = np.array([1,2,3,4,5])

# print(arr[-1])

# indexing :

# 1. Positive indexing : it starts from left to right (0 n= length of the array -1 )
# 2. Negative indexing : it starts from right to left (-1 to - n)


# Slicing : cutting up the arrays

# import numpy as np

# arr = np.array([5,8,9,7,6,4,3,2,1])

# print(arr[::-1])

# [start:end:steps]

# i - integer
# b - boolean
# u - unsigned integer


# import numpy as np

# arr = np.array(["Apple","Banana","Mango"])

# print(arr.dtype)

# Type casting 


# when we are doing a conversion from one data type to another one .

# a = 9
# b = float(a)

# print(f"a : {a}   ||    b : {b}")



# from tkinter import *
# from tkinter import ttk,messagebox


# exchange_rates = {
#     'USD' : {'USD': 1, 'EUR': 0.96, 'INR': 85},
#     'EUR' : {'EUR' : 1, 'USD': 1.04, 'INR' : 88},
#     'INR' : {'INR' : 1, 'USD' : 0.012 , 'EUR' : 0.011}
# }

# def conversion():
#     amount = float(entry_amount.get())
#     f_currency = from_currency_combobox.get()
#     t_currency = to_currency_combobox.get()

#     if f_currency == "" or t_currency == "":
#         messagebox.showinfo("Input Error","Please select both currencies.")
#         return
    
#     converted_amount = amount*exchange_rates[f_currency][t_currency]
#     result_label.config(text=f"{converted_amount:.2f} {t_currency}")
    


# root = Tk()   #initialize  the main window
# root.title("Currency Convertor")
# root.geometry('400x300')
# root.resizable(False,False)

# title_label = Label(root,text="Currency Convertor",font=("Times New Roman",20,"bold"),fg="black")
# title_label.pack(pady=10)

# input_frame = Frame(root)
# input_frame.pack(pady=10)

# Label(input_frame,text="Amount : ").grid(row=0,column=0,padx=10,pady=5 )
# entry_amount = Entry(input_frame,width=15)
# entry_amount.grid(row=0,column=1,padx=10,pady=5)


# Label(input_frame,text="From : ").grid(row=1,column=0,padx=10,pady=5)
# from_currency_combobox= ttk.Combobox(input_frame,width=13,values=list(exchange_rates.keys()))
# from_currency_combobox.grid(row=1,column=1,padx=10,pady=5)
# from_currency_combobox.set("USD")   #default selection

# Label(input_frame,text="To : ").grid(row=2,column=0,padx=10,pady=5)
# to_currency_combobox= ttk.Combobox(input_frame,width=13,values=list(exchange_rates.keys()))
# to_currency_combobox.grid(row=2,column=1,padx=10,pady=5)
# to_currency_combobox.set("USD")   #default selection

# convert_button = Button(root,text="Convert",command=conversion)
# convert_button.pack(pady=10)

# result_label = Label(root,text="",fg="green")
# result_label.pack(pady=10)


# root.mainloop()



