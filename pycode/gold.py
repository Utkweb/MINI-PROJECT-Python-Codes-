import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

def fetch_gold_rates():
    try:
        url = "https://www.tanishq.co.in/homepage?lang=en_IN"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the elements containing gold rates for different purities
        # This part depends on the specific structure of Tanishq's website
        # You may need to inspect the website's HTML structure to identify the appropriate elements
        # For example:
        gold_24k = soup.find("div", {"class": "goldrate-table"}).text.strip()
        gold_22k = soup.find("div", {"class": "goldrate-table"}).text.strip()
        gold_18k = soup.find("div", {"class": "goldrate-table"}).text.strip()
        
        return {
            "24k": gold_24k,
            "22k": gold_22k,
            "18k": gold_18k
        }
    except Exception as e:
        print("Error fetching gold rates:", e)
        return None

def update_table():
    gold_rates = fetch_gold_rates()
    if gold_rates:
        tree.delete(*tree.get_children())
        tree.insert("", "end", values=("24k", gold_rates["24k"]))
        tree.insert("", "end", values=("22k", gold_rates["22k"]))
        tree.insert("", "end", values=("18k", gold_rates["18k"]))

root = tk.Tk()
root.title("Gold Rates")

# Create Treeview
tree = ttk.Treeview(root, columns=("Purity", "Rate"))
tree.heading("#0", text="Purity")
tree.heading("#1", text="Rate")
tree.column("#0", width=100)
tree.column("#1", width=100)
tree.pack(padx=10, pady=10)

# Button to fetch and update gold rates
update_button = tk.Button(root, text="Update", command=update_table)
update_button.pack(pady=10)

# Initial update
update_table()

root.mainloop()
