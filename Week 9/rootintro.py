import tkinter as tk
from tkinter import ttk

def click_button1():
    root.title("You clicked the button!")

def click_button2():
    root.destroy()  # This will close the application when button2 is clicked
    
# the code below creates a root window and sets its title and size
root = tk.Tk()
root.title("Future Value Calculator")
root.geometry("300x150")

# the code below creates a frame and adds it to the root window
frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

# this code bellow creats two buttonss and adds them to the frame
button1 = ttk.Button(frame, text="Click Me!",
                     command=click_button1)
button2 = ttk.Button(frame, text="No, click Me!",
                     command=click_button2)

button1.pack(side=tk.LEFT, padx=5)
button2.pack(side=tk.LEFT, padx=5)
root.mainloop()