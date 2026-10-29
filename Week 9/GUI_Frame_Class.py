#How to code a class  that defines a frame.
import tkinter as tk
from tkinter import ttk, messagebox 

class InvestmentFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)

        #Define the StringVar for the monthly investment
        self.monthlyInvestment = tk.StringVar()

        #Create the widgets for the frame
        ttk.Label(self, text="Monthly Investment:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.monthlyInvestment).grid(column=1, row=0, sticky=tk.E)
        ttk.Button(self, text="Clear", command=self.clear).grid(column=2, row=0, sticky=tk.E)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def clear(self):
        messagebox.showinfo("Info", "The monthly investment is" + str(self.monthlyInvestment.get()))
        #print("Monthly Investment:", self.monthlyInvestment.get())
        self.monthlyInvestment.set("")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Future Value Calculator")
    InvestmentFrame(root)
    root.mainloop()


