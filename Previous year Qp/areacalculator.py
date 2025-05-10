import tkinter as tk

def calculate_area():
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())
        area = length * width
        result_label.config(text=f"Area: {area}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

window = tk.Tk()
window.title("Rectangle Area Calculator")

tk.Label(window, text="Length:").grid(row=0, column=0)
entry_length = tk.Entry(window)
entry_length.grid(row=0, column=1)

tk.Label(window, text="Width:").grid(row=1, column=0)
entry_width = tk.Entry(window)
entry_width.grid(row=1, column=1)

tk.Button(window, text="Calculate Area", command=calculate_area).grid(row=2, column=0, columnspan=2)

result_label = tk.Label(window, text="Area:")
result_label.grid(row=3, column=0, columnspan=2)

window.mainloop()
