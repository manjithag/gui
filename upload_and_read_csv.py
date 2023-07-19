import tkinter as tk
import pandas as pd
from tkinter import filedialog
# read csv files through tkinter dialog window
from tkinter import *
from tkinter.ttk import *

from tkinter.filedialog import askopenfile
import pandas as pd

root = Tk()
root.geometry('600x600')

var = 'Attri'

attribute = Label(root, text = var )
attribute.pack(pady=10, padx=10)

listbox = Listbox(root)


listbox.pack()

def open_file():
    file = askopenfile(mode='r', filetypes = [('csv files', '*.csv')])
    if file is not None:
        content = pd.read_csv(file)
        print(content.head()) # this will print in the terminal
        var = list(content.head(1))

        for i in var:
            listbox.insert(1, i)
        print(var)

btn = Button(root, text='open', command = open_file)
btn.pack(side = TOP, pady = 10)





mainloop()