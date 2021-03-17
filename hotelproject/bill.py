import tkinter as tk
from tkinter import ttk
from manuCard import Menu
from userInfo import UserInfo
import mysql.connector

connector = mysql.connector.connect(
    host='localhost', database='hotelms', user='hotelms', password='password')
mycusor = connector.cursor()


class Bill(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__()

        menu_text = ttk.Label(master=parent)
        user_text = ttk.Label(master=parent)
        
        def refresher():
            menu_text.configure(text=f'Menu total {Menu.give_data()}')
            user_text.configure(text=f'User details {UserInfo.give_data()}')
            menu_text.grid()
            user_text.grid()

        refresh = ttk.Button(master=parent, text='refresh', command=refresher)
        refresh.grid()
