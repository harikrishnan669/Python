import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        b_date = datetime.strptime(entry.get(), "%d-%m-%Y")
        today = datetime.today()
        age = today.year - b_date.year - ((today.month, today.day) < (b_date.month, b_date.day))
        result_label.config(text=f"Age: {age} years")
    except ValueError:
        result_label.config(text="Invalid date format. Use DD-MM-YYYY")

window = tk.Tk()
window.title("Age Calculator")

tk.Label(window, text="Enter birth date (DD-MM-YYYY):").grid(row=0, column=0)
entry = tk.Entry(window)
entry.grid(row=0, column=1)

tk.Button(window, text="Calculate Age", command=calculate_age).grid(row=2, column=0, columnspan=2)
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2)

window.mainloop()
