from tkinter import *
from tkinter import messagebox
from datetime import datetime
from dateutil.relativedelta import *

class AgeCalculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Age Calculator")
        self.grid()

        self.label = Label(self, text='Enter the date of birth in dd-mm-yyyy format')  # Fixed `label` to `Label`
        self.label.grid()

        self.dobentry = Entry(self)
        self.dobentry.grid()

        self.calculate_btn = Button(self, text='Calculate', command=self.calc_age)  # Fixed `button` to `Button`
        self.calculate_btn.grid()

    def calc_age(self):
        dob_str = self.dobentry.get()
        try:
            dob = datetime.strptime(dob_str, '%d-%m-%Y')
            today = datetime.now()
            age = relativedelta(today, dob)
            messagebox.showinfo("Age Calculator", f"Age is {age.years} years, {age.months} months, {age.days} days.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter the date in dd-mm-yyyy format.")

def main():
    AgeCalculator().mainloop()

main()
