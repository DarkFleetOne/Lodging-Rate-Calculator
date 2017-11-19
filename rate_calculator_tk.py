# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 21:16:10 2017

@author: William
"""


# %%
import tkinter
from tkinter import ttk
import sys
import ctypes


# %%
def clear_fields():
    for child in main_window.winfo_children():
        if isinstance(child, ttk.Entry):
            child.delete(0, tkinter.END)


# %%
def configure_constants():
    


# %%
if 'win' in sys.platform:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)


# %%
root = tkinter.Tk()
root.title("Rate Calculator")
root.option_add('*tearoff', False)


# %%
menubar = tkinter.Menu(root)
root['menu'] = menubar
menu_configure = tkinter.Menu(menubar)
menubar.add_cascade(menu=menu_configure, label='Configure')
menu_configure.add_command(label='Constants')  # command=configure_constants)


# %%
main_window = ttk.Frame(root, padding=(3, 3, 12, 12))


# %%
# Create Labels
rate_label = ttk.Label(main_window, text="Rate")
total_label = ttk.Label(main_window, text="Total")
rack_label = ttk.Label(main_window, text="RACK")
aaa_label = ttk.Label(main_window, text="AAA")
lbws_label = ttk.Label(main_window, text="LBWS")
soe_label = ttk.Label(main_window, text="SOE")


# %%
# Create entry (text) fields
rack_rate_entry = ttk.Entry(main_window)
rack_total_entry = ttk.Entry(main_window)
aaa_rate_entry = ttk.Entry(main_window)
aaa_total_entry = ttk.Entry(main_window)
lbws_rate_entry = ttk.Entry(main_window)
lbws_total_entry = ttk.Entry(main_window)
soe_rate_entry = ttk.Entry(main_window)
soe_total_entry = ttk.Entry(main_window)


# %%
# Create Buttons
clear_button = ttk.Button(main_window, text="Clear", command=clear_fields)
calculate_button = ttk.Button(main_window, text="Calculate")


# %%
# Divide the main window into an arbitrary size grid,
# streched to all four corners
main_window.grid(column=0, row=0,
                 sticky=(tkinter.N, tkinter.S, tkinter.E, tkinter.W))

# %%
# Place Headings into the grid, centered on the bottom edge
# and with padding below to divide from entry field placement
rate_label.grid(column=2, row=1, sticky=tkinter.S, pady=5)
total_label.grid(column=3, row=1, sticky=tkinter.S, pady=5)

# Labels are arranged along the outermost left edge of the grid
rack_label.grid(column=1, row=2)
aaa_label.grid(column=1, row=3)
lbws_label.grid(column=1, row=4)
soe_label.grid(column=1, row=5)


# %%
# Rate entries along the left under the Rate Label
# Total entries along the right under the Total Label
rack_rate_entry.grid(column=2, row=2)
rack_total_entry.grid(column=3, row=2)

aaa_rate_entry.grid(column=2, row=3)
aaa_total_entry.grid(column=3, row=3)

lbws_rate_entry.grid(column=2, row=4)
lbws_total_entry.grid(column=3, row=4)

soe_rate_entry.grid(column=2, row=5)
soe_total_entry.grid(column=3, row=5)


# %%
# Buttons placed at the bottom right of the grid, anchored
clear_button.grid(column=3, row=6, sticky=(tkinter.S, tkinter.E))
calculate_button.grid(column=4, row=6, sticky=(tkinter.S, tkinter.W))


# %%
# Shortcut to assign common settings
# Labels for each entry field are centered along the right edge
# Entries are streched to the length of the grid cell and padded horizontally
# Buttons are padded horizontally
for child in main_window.winfo_children():

    if isinstance(child, ttk.Label) and not(rate_label or total_label):
        child.grid_configure(sticky=(tkinter.E, tkinter.S), padx=5)

    elif isinstance(child, ttk.Entry):
        child.grid_configure(sticky=(tkinter.W, tkinter.S, tkinter.E), padx=5)

    elif isinstance(child, ttk.Button):
        child.grid_configure(padx=5)


# %%
# Relative weights for stretching and resizing various elements of the window
# are set
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=2)
main_window.columnconfigure(2, weight=3)
main_window.columnconfigure(3, weight=3)
main_window.columnconfigure(4, weight=3)
main_window.rowconfigure(1, weight=2, pad=5)
main_window.rowconfigure(2, weight=3, pad=5)
main_window.rowconfigure(3, weight=3, pad=5)
main_window.rowconfigure(4, weight=3, pad=5)
main_window.rowconfigure(5, weight=3, pad=5)
main_window.rowconfigure(6, weight=3, pad=5)

root.mainloop()
