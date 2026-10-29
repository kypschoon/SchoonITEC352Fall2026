import tkinter as tk
from tkinter import ttk

# the code below creates a root window and sets its title and size
root = tk.Tk()
root.title("Future Value Calculator")
root.geometry("300x150")

# the code below creates a frame and adds it to the root window
frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

# the code below creates a label and displays it
investmentlabel = ttk.Label(frame, text="Monthly Investment:")
investmentlabel.pack()

# the code below creates a text entry field and binds it to a STringVar object
investmentvarText = tk.StringVar()
investmentEntry = ttk.Entry(frame, width=25, textvariable=investmentvarText)
investmentEntry.pack()

#the code below creates a lable and displays it
futurevaluelabel = ttk.Label(frame, text="Future Value:")
futurevaluelabel.pack()

#the code below creates a read only text entry field and binds it to a StringVar object
fvText = tk.StringVar()
fventry = ttk.Entry(frame, width=25, textvariable=fvText, state="readonly")
fventry.pack()

investment = investmentvarText.get()
fvText.set("$2,000.00")
root.mainloop()