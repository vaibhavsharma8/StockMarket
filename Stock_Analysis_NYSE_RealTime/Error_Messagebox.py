'''
This is the module which contains all functions required for error handling of inputs provided by users
These functions display error boxes to users using tkinter GUI.
'''
#---------------------------------------------------------------------------------------
'''
All the necessary libraries to create different functions and perform required operations
for error handling on tkinter GUI
'''
#---------------------------------------------------------------------------------------
from tkinter import messagebox
import tkinter as tk
#---------------------------------------------------------------------------------------
'''These are the functions which create error message boxes wand are called in GUI file while 
error handling is performed
'''
#---------------------------------------------------------------------------------------
def error_message_date():
    tk.messagebox.showerror("Error",
                                "Date Entered in wrong format. Please enter date in 'YYYY-MM-DD' ")
def error_message_datatype():
    tk.messagebox.showerror("Error",
                                "Please enter a valid number in prediction days/ moving average days")
def error_message_datatype2():
    tk.messagebox.showerror("Error",
                                "Please enter a valid number for MA days")
def error_message_stocksymbol():
    tk.messagebox.showerror("Error",
                                "Please enter valid stock symbol")


#-------------------------------------
'''
END OF MODULE
'''
#-------------------------------------