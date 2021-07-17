'''
This is the GUI version file of the stock market analyser. The programs takes input in the tkinter enabled GUI
and generates appropriate output based on user selection.
'''
#--------------------------------------------------------------------------------------------------------
'''
All the necessary libraries to create different functions and perform required operations
and enable calculations and potting of results.
'''
#---------------------------------------------------------------------------------------
import pandas as pd
import datetime
import Descriptive_Analysis as DA
import Predictive_Analysis as PA
import Error_Messagebox as EMB
import pandas_datareader as web
from pandas_datareader._utils import RemoteDataError
import tkinter as tk
from tkinter import *
import warnings
#---------------------------------------------------------------------------------------
'''
As python shows some warnings which do not impact the output it's important to hide 
the warnings for users as the warning do not concern them.
'''
#---------------------------------------------------------------------------------------
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
warnings.filterwarnings("ignore", message="Numerical issues were encountered ")


'''
This function is called when submit button is clicked after the user enters all the inputs
in the GUI input window. The purpose of the function is to obtain the value of inputs and
handle errors if any.
'''
def run_on_submit():

    global stock_name, price, Price, start, end, Prediction_Days,Prediction_Days2, df1, MA_Days,start1,end1,trainingData
    price = v.get()
    selection=v2.get()
    regressionType = v3.get()
    trainingData = v4.get()
    Price = [price]
    #These try and catch blocks handle the errors in the input.(if any)
    try:
        start1 = startDate_input.get()
        start = datetime.datetime.strptime(start1, '%Y-%m-%d').date()
        end1 = endDate_input.get()
        end = datetime.datetime.strptime(end1, '%Y-%m-%d').date()
    except ValueError as dateError:
        EMB.error_message_date()
        pass
    try:
        Prediction_Days = int(Prediction_Days_input.get())
        MA_Days = int(Moving_Average_Days.get())
        check_integer = int(Prediction_Days)
        check_integer2= int(MA_Days)
    except ValueError as dateError:
        EMB.error_message_datatype()
        pass

    try:
        stock_name = stock_name_input.get()
        df = web.DataReader(stock_name, 'yahoo', start, end)
    except RemoteDataError as RemoteData:
        EMB.error_message_stocksymbol()
    else:
        df1 = pd.DataFrame(df, columns=['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'])
        df1 = df1.reset_index()
        pd.options.display.max_columns = None
        '''
        The below if else logical conditions which return the result as per users selection of
        the type of analysis user wants to see.
        '''
        if selection == "Stock Information":
            DA.stock_Info(df1,stock_name,Price,price)

        elif selection == "Descriptive Analyisis":
            DA.descriptive_analysis_message(df1,Price,stock_name)

        elif selection == "CandleStick Chart":
            DA.candlestick_Chart(df1)

        elif selection == "Series Graphs":
            DA.series_graphs(12,26,MA_Days,df1,Price,price,stock_name)

        elif selection == "Predictive Analysis" and regressionType == "Linear Regression":
            PA.linear_Regression(df1,Price,price,stock_name,Prediction_Days,trainingData)
        elif selection == "Predictive Analysis" and regressionType == "Decision Tree Regression":
            PA.decisionTree_Regression(df1,Price,price,stock_name,Prediction_Days,trainingData)

        else:
            print("Thankyou for using the program.")




'''
Here a main GUI window is created for taking the user inputs and displaying the analysis selected.
The properties of the winow are defined here.
'''
GUI = tk.Tk()
GUI.title("Stock Analysis by Vaibhav Sharma")
GUI.geometry('1200x250')
GUI.config(bg='steel blue')
'''
The main function is called firstly when the program runs. It is responsible for creating the entities of the input window
and enables user to easily enter the inputs and choose the analysis user wants to see.
'''
def main():
    global stock_name_input,startDate_input, endDate_input, price_input ,selection_input,Prediction_Days_input, v,v2,v3,v4,Moving_Average_Days
    #creation of labels for entry boxes and radio buttons and defining their position and display properties
    tk.Label(GUI, text="Enter start date for analysis(yyyy-mm-dd): ",bg = 'sky blue',font=('bold',9)).grid(row=0)
    tk.Label(GUI, text="Enter end date for analysis(yyyy-mm-dd): ",bg = 'sky blue',font=('bold',9)).grid(row=1)
    tk.Label(GUI, text="Enter symbol of the stock you need to analyze: ",bg = 'sky blue',font=('bold',9)).grid(row=2)
    tk.Label(GUI, text="Enter Number of Days for prediction: ",bg = 'sky blue',font=('bold',9)).grid(row=3)
    tk.Label(GUI, text="Enter Number of Days for Moving Average (Recommended=9): ",bg = 'sky blue',font=('bold',9)).grid(row=4)
    tk.Label(GUI, text="Select the Price: ",bg = 'sky blue',font=('bold',9)).grid(row=5)
    tk.Label(GUI, text="Select the display option: ",bg = 'sky blue',font=('bold',9)).grid(row=6)
    tk.Label(GUI, text="Select the prediction method (for predictive analysis): ",bg = 'sky blue',font=('bold',9)).grid(row=7)
    tk.Label(GUI, text="Select fraction of training data for prediction: ",bg = 'sky blue',font=('bold',9)).grid(row=8)

    #here we set the variables 'v,v2,v3,v4' for the radio button inputs provided by the user and set the default value
    v = tk.StringVar()
    v.set('Close')
    v2=tk.StringVar()
    v2.set('Stock Information')
    v3=tk.StringVar()
    v3.set('Linear Regression')
    v4=tk.DoubleVar()
    v4.set(0.25)

    #Creation of radio boxes for easy user selection.
    tk.Radiobutton(GUI,
                   text="High",
                   padx=5,
                   variable=v,
                   value="High",
                   bg = 'gold',font=('bold',9),relief =RAISED).grid(row=5,column=1)
    tk.Radiobutton(GUI,
                   text="Open",
                   padx=5,
                   variable=v,
                   value='Open',
                   bg = 'gold',font=('bold',9),relief =RAISED).grid(row=5, column=2)
    tk.Radiobutton(GUI,
                   text="Low",
                   padx=5,
                   variable=v,
                   value="Low",
                   bg = 'gold',font=('bold',9),relief =RAISED).grid(row=5, column=3)
    tk.Radiobutton(GUI,
                   text="Close",
                   padx=5,
                   variable=v,
                   value='Close',
                   bg = 'gold',font=('bold',9),relief =RAISED).grid(row=5, column=4)
    tk.Radiobutton(GUI,
                   text="Descriptive Analyisis",
                   padx=5,
                   variable=v2,
                   value="Descriptive Analyisis",
                   bg = 'gold',font=('bold',9),relief =RAISED).grid(row=6, column=1)
    tk.Radiobutton(GUI,
                   text="Stock Information",
                   padx=20,
                   variable=v2,
                   value='Stock Information',
                   bg = 'gold',font=('bold',9),relief =RAISED).grid(row=6, column=2)
    tk.Radiobutton(GUI,
                   text="Predictive Analysis",
                   padx=20,
                   variable=v2,
                   value="Predictive Analysis",
                   bg = 'gold',font=('bold',9),relief =RAISED).grid(row=6, column=3)
    tk.Radiobutton(GUI,
                   text="CandleStick Chart",
                   padx=20,
                   variable=v2,
                   value='CandleStick Chart',
                   bg = 'gold',font=('bold',9),relief =RAISED).grid(row=6, column=4)
    tk.Radiobutton(GUI,
                   text="Series Graphs",
                   padx=20,
                   variable=v2,
                   value='Series Graphs',
                   bg = 'gold',font=('bold',9),relief =RAISED).grid(row=6, column=5)
    tk.Radiobutton(GUI,
                   text="Linear Regression",
                   padx=20,
                   variable=v3,
                   value='Linear Regression',
                   bg = 'gold',font=('bold',9),relief =RAISED).grid(row=7, column=1)
    tk.Radiobutton(GUI,
                   text="Decision Tree Regression",
                   padx=20,
                   variable=v3,
                   value='Decision Tree Regression',
                   bg = 'gold',font=('bold',9),relief =RAISED).grid(row=7, column=2)
    tk.Radiobutton(GUI,
                   text="0.25",
                   padx=20,
                   variable=v4,
                   value=0.25,
                   bg = 'gold',font=('bold',9),relief =RAISED).grid(row=8, column=1)
    tk.Radiobutton(GUI,
                   text="0.30",
                   padx=20,
                   variable=v4,
                   value=0.30,
                   bg = 'gold',font=('bold',9),relief =RAISED).grid(row=8, column=2)
    tk.Radiobutton(GUI,
                   text="0.50",
                   padx=20,
                   variable=v4,
                   value=0.50,
                   bg = 'gold',font=('bold',9),relief =RAISED).grid(row=8, column=3)
    #Obtaining the value of entry boxes as an input by the user.
    startDate_input = tk.Entry(GUI)
    endDate_input = tk.Entry(GUI)
    stock_name_input = tk.Entry(GUI)
    Prediction_Days_input = tk.Entry(GUI)
    Moving_Average_Days = tk.Entry(GUI)
    #Defining the position of entry boxes
    startDate_input.grid(row=0, column=1)
    endDate_input.grid(row=1, column=1)
    stock_name_input.grid(row=2, column=1)
    Prediction_Days_input.grid(row=3, column=1)
    Moving_Average_Days.grid(row=4, column = 1)
    #Creation of the submit button and passing the input values by calling the run_on_submit function created on top.
    tk.Button(GUI,
              text='Submit', command=run_on_submit,font=('bold',12),relief =RAISED,bg = 'green').grid(row=10,
                                                          column=1,
                                                          sticky=tk.W,
                                                          pady=8)

    #packing all the input boxes and buttons into the main tkinter GUI window.
    GUI.mainloop()

if __name__ == "__main__":
    main()

#-------------------------------------
'''
END OF MODULE
'''
#-------------------------------------










