# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:17:18 2017

@author: William
"""


# %%
from tkinter import *
from tkinter import ttk
import lodging_functions
import ctypes
import sys


# %%
def calculate(*args):
    try:
        acc = float(total.get())
        rate.set(lodging_functions.make_currency_pretty(lodging_functions.remove_tax(acc)))
    except ValueError:
        pass


# %%
# Sets text to use DPI scaling on Windows systems, much smoother text
if 'win' in sys.platform:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Draw initial frame and place into memory
root = Tk()
root.title("Remove Tax")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


# %%
# create primary input/output widgets
total = StringVar()
rate = StringVar()
total_entry = ttk.Entry(mainframe, width=7, textvariable=total)
total_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=rate).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)


# %%
# Label Widgets
ttk.Label(mainframe, text="Total").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="From").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Rate").grid(column=3, row=2, sticky=W)


# %%
# shortcut to add padding around each of the grid elements, smoothens resizing
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# cursor focus set to total_entry text field
total_entry.focus()

# Run calculate function when Enter is pressed
root.bind('<Return>', calculate)

# Initiate application
root.mainloop()
