# Kyp Schoon

import tkinter as tk
from tkinter import ttk

def calculateFutureValue(investment, rate, years):
    future_value = 0.0
    for i in range(int(years) * 12):
        future_value += float(investment)
        monthly_interest = future_value * (float(rate) / 100) / 12
        future_value += monthly_interest
    return future_value

def main():
    root = tk.Tk()
    root.title("Future Value Calculator")
    root.geometry("400x300")

    frame = ttk.Frame(root, padding="10 10 10 10")
    frame.pack(fill=tk.BOTH, expand=True)

    investmentText = tk.StringVar()
    interestRateText = tk.StringVar()
    yearsText = tk.StringVar()
    FutureValueText = tk.StringVar()

    def clickButton1():
        try:
            investment = float(investmentText.get())
            rate = float(interestRateText.get())
            years = int(yearsText.get())
            
            future_value = calculateFutureValue(investment, rate, years)
            FutureValueText.set(f"${future_value:,.2f}")
        except ValueError:
            FutureValueText.set("Invalid input")

    ttk.Label(frame, text="Monthly Investment:").grid(column=0, row=0, sticky=tk.E)
    ttk.Entry(frame, width=25, textvariable=investmentText).grid(column=1, row=0)
    ttk.Label(frame, text="Yearly Interest Rate:").grid(column=0, row=1, sticky=tk.E)
    ttk.Entry(frame, width=25, textvariable=interestRateText).grid(column=1, row=1)
    ttk.Label(frame, text="Years:").grid(column=0, row=2, sticky=tk.E)
    ttk.Entry(frame, width=25, textvariable=yearsText).grid(column=1, row=2)
    ttk.Label(frame, text="Future Value").grid(column=0, row=3, sticky=tk.E)
    ttk.Entry(frame, width=25, textvariable=FutureValueText, state="readonly").grid(column=1, row=3, sticky=tk.E)

    ttk.Button(frame, text="Calculate", command=clickButton1).grid(column=1, row=4, sticky=tk.E)

    for child in frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()