import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x400")
root.title("Click to Select, WASD to Move")

active_button = None
buttons = []
keys_pressed = set()
speed = 1

def select_button(button):
    global active_button
    if active_button and active_button.winfo_exists():
        active_button.configure(style="TButton")
    active_button = button
    button.configure(style="Active.TButton")

def get_bbox(button):
    """Return (x1, y1, x2, y2) of a button"""
    if not button.winfo_exists():
        return None
    x = button.winfo_x()
    y = button.winfo_y()
    w = button.winfo_reqwidth()
    h = button.winfo_reqheight()
    return (x, y, x + w, y + h)

def boxes_overlap(b1, b2):
    """True if two bounding boxes touch or overlap"""
    if not b1 or not b2:
        return False
    return not (b1[2] <= b2[0] or b1[0] >= b2[2] or b1[3] <= b2[1] or b1[1] >= b2[3])

def clamp_and_place(button, x, y):
    """Force the button to stay fully inside the window"""
    root.update_idletasks()
    btn_w = button.winfo_reqwidth()
    btn_h = button.winfo_reqheight()
    max_x = root.winfo_width() - btn_w - 4
    max_y = root.winfo_height() - btn_h - 4
    x = max(4, min(x, max_x))
    y = max(4, min(y, max_y))
    button.place(x=x, y=y, relx=0, rely=0, anchor="nw")

def check_collisions():
    """Destroy any non-center button that the active button is touching"""
    if not active_button or not active_button.winfo_exists():
        return
    active_box = get_bbox(active_button)
    for btn in buttons[:]:
        if btn == active_button or btn == center_button or not btn.winfo_exists():
            continue
        if boxes_overlap(active_box, get_bbox(btn)):
            btn.destroy()
            if btn in buttons:
                buttons.remove(btn)

def move_loop():
    if active_button and active_button.winfo_exists():
        dx = 0
        dy = 0
        if "w" in keys_pressed or "W" in keys_pressed:
            dy -= speed
        if "s" in keys_pressed or "S" in keys_pressed:
            dy += speed
        if "a" in keys_pressed or "A" in keys_pressed:
            dx -= speed
        if "d" in keys_pressed or "D" in keys_pressed:
            dx += speed

        if dx != 0 or dy != 0:
            x = active_button.winfo_x() + dx
            y = active_button.winfo_y() + dy
            clamp_and_place(active_button, x, y)
            check_collisions()

    root.after(10, move_loop)

def on_key_press(event):
    keys_pressed.add(event.keysym)

def on_key_release(event):
    keys_pressed.discard(event.keysym)

def destroy_others():
    global active_button
    for btn in buttons[:]:
        if btn.winfo_exists():
            btn.destroy()
    buttons.clear()
    active_button = None

    exit_button = ttk.Button(root, text="DESTROY", command=root.destroy)
    exit_button.place(relx=0.5, rely=0.5, anchor="center")
    select_button(exit_button)

style = ttk.Style()
style.configure("Active.TButton", background="yellow")

# Create buttons
top_button = ttk.Button(root, text="Click Me", command=lambda: select_button(top_button))
bottom_button = ttk.Button(root, text="No, Click Me", command=lambda: select_button(bottom_button))
left_button = ttk.Button(root, text="Don't Click Me", command=lambda: select_button(left_button))
right_button = ttk.Button(root, text="Click Me Too", command=lambda: select_button(right_button))
center_button = ttk.Button(root, text="Click Me For Fun", command=destroy_others)

# Start with absolute positions
root.update_idletasks()
w = root.winfo_width()
h = root.winfo_height()

top_button.place(x=w//2 - 40, y=10)
bottom_button.place(x=w//2 - 50, y=h - 40)
left_button.place(x=10, y=h//2 - 15)
right_button.place(x=w - 120, y=h//2 - 15)
center_button.place(x=w//2 - 60, y=h//2 - 15)

buttons = [top_button, bottom_button, left_button, right_button, center_button]

root.bind_all("<KeyPress>", on_key_press)
root.bind_all("<KeyRelease>", on_key_release)

move_loop()
root.mainloop()