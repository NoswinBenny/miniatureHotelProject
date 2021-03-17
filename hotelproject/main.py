from userInfo import UserInfo
from bill import *
from manuCard import Menu
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

notebook = ttk.Notebook(master=root)
notebook.grid_columnconfigure(0, weight=1)
notebook.grid_rowconfigure(0, weight=1)

user_frame = ttk.Frame(border=0)
user_frame.grid_columnconfigure(0, weight=1)

menu_frame = ttk.Frame(border=0)
menu_frame.columnconfigure(0, weight=1)
menu_frame.rowconfigure(0, weight=1)

# user_frame.rowconfigure(0, weight=1)

bill_board = ttk.Frame(border=0)

UserInfo(user_frame).grid(row=1, column=6)
Menu(menu_frame).grid()
Bill(bill_board).grid()

notebook.add(user_frame, text='User Card')
notebook.add(menu_frame, text='Menu Card')
notebook.add(bill_board, text='Bill Board')

notebook.grid(row=0, sticky='nswe')
root.mainloop()
