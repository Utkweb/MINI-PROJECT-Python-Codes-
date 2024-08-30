import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        tk.messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        tk.messagebox.showwarning("Warning", "Please select a task to delete.")

window = tk.Tk()
window.title("To-Do List")

frame_tasks = tk.Frame(window)
frame_tasks.pack()

listbox = tk.Listbox(
    frame_tasks,
    height=10,
    width=50,
    bg="#f2f2f2",
    fg="#444444",
    font=("Courier New", 12),
    borderwidth=1,
)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame_tasks)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(window, width=50, bg="#f2f2f2", fg="#444444", font=("Courier New", 12))
entry.pack(pady=10)

button_add_task = tk.Button(
    window,
    text="Add Task",
    width=48,
    bg="#c5f0f0",
    fg="#444444",
    font=("Courier New", 12),
    command=add_task,
)
button_add_task.pack(pady=5)

button_delete_task = tk.Button(
    window,
    text="Delete Task",
    width=48,
    bg="#c5f0f0",
    fg="#444444",
    font=("Courier New", 12),
    command=delete_task,
)
button_delete_task.pack(pady=5)

window.mainloop()