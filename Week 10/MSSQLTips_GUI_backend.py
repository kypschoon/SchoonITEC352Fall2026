#Kyp Schoon
#02NOV2026
import tkinter
import yfinance as yf
import pandas as pd

def entry_click(event, initial_message):
    if event.widget.get() == initial_message:
        event.widget.delete(0, tkinter.END)

def clear_treeview(treeView):
    for row in treeView.get_children():
        treeView.delete(row)

def make_selection(treeView, number, period_combobox, interval_combobox):
    if number.get() == 1:
        column_headings = ['Datetime', 'Open', 'Close']
        col_anchor = ['center', 'center', 'center']
        period_combobox.config(state = "readonly")
        interval_combobox.config(state = "readonly")
    elif number.get() == 2:
        column_headings = ['Holder', 'Shares', 'Date Reported']
        col_anchor = ['w', 'e', 'center']
        period_combobox.config(state = tkinter.DISABLED)
        interval_combobox.config(state = tkinter.DISABLED)
    clear_treeview(treeView)    
    for index, col in enumerate(column_headings):
        treeView.heading(index, text = col)
        treeView.column(index, anchor=col_anchor[index])

def invalid_entry(entry):
    entry.delete(0, tkinter.END)
    entry.insert(0, "*")
    entry.insert(tkinter.END, "*")

def get_data(tree, symbol_entry, number, period_combobox, interval_combobox):
    clear_treeview(tree)
    symbol = symbol_entry.get().strip().upper()
    
    if not symbol or symbol == "*":
        return invalid_entry(symbol_entry)
    
    try:
        ticket = yf.Ticker(symbol)
        
        if number.get() == 1:  # Historical Data
            period = period_combobox.get()
            interval = interval_combobox.get()
            data = ticket.history(period=period, interval=interval)
            
            if data.empty:
                return invalid_entry(symbol_entry)
            
            data = data.reset_index()
            
            # Handle both 'Date' and 'Datetime' column names
            date_col = 'Datetime' if 'Datetime' in data.columns else 'Date'
            dataset = data[[date_col, 'Open', 'Close']].copy()
            dataset.columns = ['Datetime', 'Open', 'Close']
            
            dataset['Datetime'] = dataset['Datetime'].dt.strftime("%Y-%m-%d %H:%M")
            dataset['Open'] = dataset['Open'].map(lambda x: f'{x:.4f}')
            dataset['Close'] = dataset['Close'].map(lambda x: f'{x:.4f}')
            
        elif number.get() == 2:  # Institutional Holders
            holders = ticket.institutional_holders
            if holders is None or holders.empty:
                return invalid_entry(symbol_entry)
            
            dataset = holders[['Holder', 'Shares', 'Date Reported']].copy()
            dataset['Date Reported'] = dataset['Date Reported'].dt.date
        
        # Insert rows into treeview
        for index in range(len(dataset)):
            tree.insert('', tkinter.END, values=list(dataset.iloc[index]))
            
    except Exception:
        invalid_entry(symbol_entry)