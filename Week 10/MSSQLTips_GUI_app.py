#Kyp Schoon
#02NOV2026
#1 Imports the tkinter module.
import tkinter
from tkinter import ttk
import MSSQLTips_GUI_backend as backend

#2 Creates a main GUI window.
#2.1 Defines the main window
root = tkinter.Tk()
root.title('MSSQLtips Finance')
# root.iconbitmap('SSQLtips.ico') 
root.geometry('420x460+300+300')
root.resizable(0,0)

#3 Adds widgets to the window.
#3.1 Creates frames.
greeting_frame = tkinter.Frame(root)
textbox_frame = tkinter.Frame(root)
radio_frame = tkinter.LabelFrame(root, text='Select a dataset')
combobox_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
treeview_frame = tkinter.Frame(root)

#3.2 Arrange frames.
greeting_frame.pack()
textbox_frame.pack()
radio_frame.pack()
combobox_frame.pack()
button_frame.pack()
treeview_frame.pack()

#3.3 Uses the greeting frame to organize widgets.
#3.3.1 Adds a label to the greeting frame.
greeting_label = tkinter.Label(greeting_frame, text='Welcome to MSSQLTips')

#3.3.2 Arranges the label.
greeting_label.pack(pady=(10,5))

#3.4 Arrange the textbox frame
#3.4.1 Adds a label to the textbox frame.
entry_label = tkinter.Label(textbox_frame, text='Stock Ticker Symbol:')

#3.4.2 Adds a text box to the textbox frame and set the initial value.
text_entry = tkinter.Entry(textbox_frame)
initial_value = 'GOOG'
text_entry.insert(0, initial_value)

#3.4.3 Defines the frame layout.
entry_label.grid(row=0, column=0, padx=(10,0), pady=5)
text_entry.grid(row=0, column=1, padx=5, pady=5)

#3.4.4 Bind to the event
text_entry.bind("<ButtonPress-1>", lambda event, initial_message = initial_value: backend.entry_click(event, initial_value))

#3.5 Arranges the radio frame.
#3.5.1 Set initial value.
number = tkinter.IntVar()
number.set(1)

#3.5.2 Adds radio buttons to the radio frame. On selection we can display the value using one Label.
radio_historical_data = tkinter.Radiobutton(radio_frame, text = 'Historical Data', value = 1, variable = number,command = lambda:backend.make_selection(tree, number, period_combobox, interval_combobox))
radio_institutional_holders = tkinter.Radiobutton(radio_frame, text='Institutional Holders', value=2, variable = number,command = lambda:backend.make_selection(tree, number, period_combobox, interval_combobox))

#3.5.3 Defines the frame layout.
radio_historical_data.grid(row=0, column=0, pady=5)
radio_institutional_holders.grid(row=0, column=1, pady=5)

#3.6 Arranges the combobox frame.
#3.6.1 Add labels, comboboxes and the get button to the frame.
period_label = tkinter.Label(combobox_frame, text='Period:', width = 6, anchor='e')
period_combobox = ttk.Combobox(combobox_frame, value=['1d','5d','1mo'], width=8, justify='center', state="readonly")
interval_label = tkinter.Label(combobox_frame, text='Interval:', width = 6, anchor='e')
interval_combobox = ttk.Combobox(combobox_frame, value=['15m','30m','1h'], width=8,justify='center', state="readonly")

#3.6.2 Set default selection.
period_combobox.current(0)
interval_combobox.current(0)

#3.6.3 Define the frame layout
period_label.grid(row=0, column=0, padx=(5,0), pady=5)
period_combobox.grid(row=0, column=1, padx=(0,5), pady=5)
interval_label.grid(row=0, column=2, padx=(5,0), pady=5)
interval_combobox.grid(row=0, column=3, padx=(0,5), pady=5)

#3.7 Arrange the button frame.
#3.7.1 Adds a button to the button frame.
get_button = tkinter.Button(button_frame, text = "Get Data",command = lambda:backend.get_data(tree, text_entry, number, period_combobox, interval_combobox),width = 34, borderwidth = 3)

#3.7.2 Defines the frame layout.
get_button.pack()

#3.8 Arrange the treeview frame.
#3.8.1 Adds a treeview to the treeview frame.
columns = ['col0','col1','col2']
col_width = [190, 90, 110]
default_headings = ['Datetime', 'Open', 'Close']
tree = ttk.Treeview(treeview_frame, columns = columns, show = 'headings', height = 12)
# assigns the column width and headings
for index, col in enumerate(columns):
    tree.column(col, width = col_width[index], anchor = 'center')
    tree.heading(col, text=default_headings[index])

#3.8.2 Add a scrollbar to the treeview frame.
scrollbar = ttk.Scrollbar(treeview_frame, orient = tkinter.VERTICAL, command = tree.yview)
tree.configure(yscroll = scrollbar.set)

#3.8.3 Defines the frame layout.
tree.grid(row = 0, column = 0, sticky = 'nsew', padx = (5,0), pady = 5)
scrollbar.grid(row = 0, column = 1, sticky = 'ns', padx = (0,5), pady = 5)

#4 Runs the window's main loop.
root.mainloop()