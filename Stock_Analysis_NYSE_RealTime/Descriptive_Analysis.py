'''
This is the module which contains all functions required for descriptive analysis of selected inputs by the user.
These functions are called as per users requirement in the CLI as well as GUI file.
'''
#---------------------------------------------------------------------------------------
'''
All the necessary libraries to create different functions and perform required operations
and enable calculations and potting of results.
'''
#---------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mpdates
from tabulate import tabulate
from tkinter import messagebox
import tkinter as tk

#Defiing the property of matplot charts to set the black background theme.
plt.style.use('dark_background')

#This function is called in the CLI file when user wants to see descriptive analysis like mean, median etc.
def Descriptive_Analysis_Terminal(df1,Price):
    df1_describe = df1[Price].describe().reset_index().replace(
        {'25%': 'Q1', '50%': 'Q2', '75%': 'Q3'}).set_index('index')
    df1_describe.loc["Range"] = df1_describe.loc['max'] - df1_describe.loc['min']
    df1_describe.loc["IQR"] = df1_describe.loc['Q3'] - df1_describe.loc['Q1']
    descriptivedf = pd.DataFrame(df1_describe)
    print(tabulate(descriptivedf))

#This function is called in the GUI file when user wants to see descriptive analysis like mean, median etc.
def descriptive_analysis_message(df1,Price,stock_name):
    df1_describe = df1[Price].describe().reset_index().replace(
        {'25%': 'Q1', '50%': 'Q2', '75%': 'Q3'}).set_index('index')
    df1_describe.loc["Range"] = df1_describe.loc['max'] - df1_describe.loc['min']
    df1_describe.loc["IQR"] = df1_describe.loc['Q3'] - df1_describe.loc['Q1']
    descriptivedf = pd.DataFrame(df1_describe)
    Table = tabulate(descriptivedf) #Converting the dataframe into a table using tabulate function from tabluate library.
    tk.messagebox.showinfo("Desciptive Analysis",
                            Table) #This displays the analysis in a tkinter GUI message box

#---------------------------------------------------------------------------------------
'''
This function is called to see stock related information in the from of charts and contains time series chart,volume 
bar chart, daily return chart of the stock and linear trend chart for the time period selected.
'''
#---------------------------------------------------------------------------------------

def stock_Info(df1,stock_name,Price,price):
    #Plotting the time series chart for all prices
    fig, ax = plt.subplots(nrows=2, ncols=2)
    fig.canvas.set_window_title('Stock Information')
    fig.set_size_inches(16, 8, forward=True)
    ax[0,0].plot(df1['Date'],df1['Open'], color='red', label='open')
    ax[0,0].plot(df1['Date'],df1['Close'], color='green', label='close')
    ax[0,0].plot(df1['Date'],df1['Low'], color='blue', label='low')
    ax[0,0].plot(df1['Date'],df1['High'], color='orange', label='high')
    ax[0,0].set_title(stock_name + ' Price Chart', fontsize = 9)
    ax[0,0].set_xlabel('Date',fontsize = 8)
    ax[0,0].set_ylabel('price',fontsize = 8)
    ax[0,0].legend(loc='best')
    plt.setp(ax[0, 0].xaxis.get_majorticklabels(), rotation=90)
    plt.setp(ax[0, 0].xaxis.get_majorticklabels(), fontsize=6)
    plt.setp(ax[0, 0].yaxis.get_majorticklabels(), fontsize=6)


    #Plotting the volume bar chart of selected stock for defined range of dates.
    ax[0,1].bar(df1['Date'],df1['Volume'], color='white', label='volume')
    ax[0,1].set_title(stock_name+ ' Volume',fontsize = 9)
    ax[0,1].set_xlabel('Date',fontsize = 8)
    ax[0,1].set_ylabel('volume',fontsize = 8)
    ax[0,1].legend(loc='best')
    plt.setp(ax[0, 1].xaxis.get_majorticklabels(), rotation=90)
    plt.setp(ax[0, 1].xaxis.get_majorticklabels(), fontsize=6)
    plt.setp(ax[0, 1].yaxis.get_majorticklabels(), fontsize=6)

    #Plotting the daily return chart using percentage change in price
    df1['Daily Return'] = df1[Price].pct_change()
    ax[1, 0].plot(df1['Date'], df1['Daily Return'],linestyle='--', marker='o', color = 'green',label ='Daily Return' )
    ax[1, 0].set_title("Daily Return",fontsize = 9)
    ax[1, 0].set_xlabel('Date', fontsize=6)
    ax[1, 0].set_ylabel('Daily Return', fontsize=6)
    ax[1, 0].legend(loc='best')
    plt.setp(ax[1, 0].xaxis.get_majorticklabels(), rotation=90)
    plt.setp(ax[1, 0].xaxis.get_majorticklabels(), fontsize=6)
    plt.setp(ax[1, 0].yaxis.get_majorticklabels(), fontsize=6)
    #Linear trend graph creation
    x = mpdates.date2num(df1['Date'])
    y = df1[Price]
    ax[1, 1].scatter(x, y, label=price)
    z = np.polyfit(x, y, 1)
    z = np.squeeze(z)
    p = np.poly1d(z)
    xx_xx = np.linspace(x.min(), x.max(), 100)
    dd_dd= mpdates.num2date(xx_xx)
    ax[1, 1].plot(dd_dd, p(xx_xx), "r--", label='Trend')
    ax[1, 1].set_title("Linear Trend", fontsize=9)
    ax[1, 1].set_xlabel('Date', fontsize=6)
    ax[1, 1].set_ylabel(price, fontsize=6)
    ax[1, 1].legend(loc='best')
    plt.setp(ax[1, 1].xaxis.get_majorticklabels(), rotation=90)
    plt.setp(ax[1, 1].xaxis.get_majorticklabels(), fontsize=6)
    plt.setp(ax[1, 1].yaxis.get_majorticklabels(), fontsize=6)
    fig.tight_layout() #setting a close layout of subplots to fit them in one window for user ease.

    plt.show()


#Plotting the Cadlestick chart for a stock
def candlestick_Chart(df1):
    plt.style.use('dark_background')
    df1 = df1[['Date', 'Open', 'High',
             'Low', 'Close']]
    # convert into datetime object to create candlwstick
    df1['Date'] = pd.to_datetime(df1['Date'])
    # apply map function to map the converted column of dates to date column in dataframe
    df1['Date'] = df1['Date'].map(mpdates.date2num)
    fig, ax = plt.subplots()
    # plotting the data as per users selection
    candlestick_ohlc(ax, df1.values, width=0.6,
                     colorup='green', colordown='red',
                     alpha=0.8)
    #Displayong the grid as candlestick chart needs focused view
    ax.grid(True)
    #Printing the labels of the chart
    ax.set_xlabel('Date')
    ax.set_ylabel('Close')
    plt.title('Candle Stick Chart')
    #Converting the dates converted to numerical format previously back to date format for plotting
    date_format = mpdates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    fig.tight_layout()
    plt.show()

#Creating series graphs such as Moving average, weighted MA, MACD and raw time series as per users input
def series_graphs(a,b,MA_Days,df1,Price,price,stock_name):
    #raw time series graph
    plt.style.use('dark_background')
    fig, ax = plt.subplots(nrows=2, ncols=2)
    fig.canvas.set_window_title('Descriptive Analysis Charts')
    fig.set_size_inches(16,8,forward=True)
    ax[0, 0].plot(df1['Date'], df1[Price])
    ax[0, 0].set_title('Time Series Graph of ' + stock_name,fontsize= 9)
    plt.setp(ax[0,0].xaxis.get_majorticklabels(), rotation=90)
    plt.setp(ax[0,0].xaxis.get_majorticklabels(), fontsize=6)
    plt.setp(ax[0, 0].yaxis.get_majorticklabels(), fontsize=6)
    ax[0, 0].set_xlabel('Date', fontsize=8)
    ax[0, 0].set_ylabel(price + ' Price', fontsize=8)
    #moving average graph
    ax[0, 1].plot(df1['Date'], df1['Close'], label=price)
    ax[0, 1].plot(df1['Date'],df1[Price].rolling(MA_Days).mean(), label='MA ' + str(MA_Days) + ' days')
    ax[0, 1].plot(df1['Date'],df1[Price].rolling(2 * MA_Days).mean(), label='MA ' + str(2 * MA_Days) + ' days')
    ax[0, 1].plot(df1['Date'],df1[Price].rolling(3 * MA_Days).mean(), label='MA ' + str(3 * MA_Days) + ' days')
    ax[0, 1].legend(loc='best')
    ax[0, 1].set_title(stock_name + ' Moving Average',fontsize=9)
    plt.setp(ax[0, 1].xaxis.get_majorticklabels(), rotation=90)
    plt.setp(ax[0, 1].xaxis.get_majorticklabels(), fontsize=6)
    plt.setp(ax[0, 1].yaxis.get_majorticklabels(), fontsize=6)
    ax[0,1].set_xlabel('Date', fontsize=8)
    ax[0,1].set_ylabel(price + ' Price', fontsize=8)
    #Weighted Moving Average Graph
    ax[1,0].plot(df1['Date'], df1[Price], label=price)
    ax[1,0].plot(df1['Date'],df1[Price].ewm(span=MA_Days).mean(), label='WMA ' + str(MA_Days) + ' days')
    ax[1,0].plot(df1['Date'],df1[Price].ewm(span=2 * MA_Days).mean(), label='WMA ' + str(2 * MA_Days) + ' days')
    ax[1,0].plot(df1['Date'],df1[Price].ewm(span=2 * MA_Days).mean(), label='WMA ' + str(3 * MA_Days) + ' days')
    ax[1,0].legend(loc='best')
    ax[1,0].set_xlabel('Date', fontsize=8)
    ax[1,0].set_ylabel(price + ' Price', fontsize=8)
    plt.setp(ax[1,0].xaxis.get_majorticklabels(), rotation=90)
    plt.setp(ax[1,0].xaxis.get_majorticklabels(), fontsize=6)
    plt.setp(ax[1,0].yaxis.get_majorticklabels(), fontsize=6)
    ax[1,0].set_title(stock_name + ' Weighted Moving Average',fontsize= 9)
    #MACD Graph
    ax[1,1].plot(df1['Date'], df1[Price], label=price)
    ax[1,1].plot(df1['Date'], df1[Price].ewm(span=a, min_periods=a).mean(), label='MA Fast')
    ax[1,1].plot(df1['Date'], df1[Price].ewm(span=b, min_periods=b).mean(), label='MA Slow')
    ax[1,1].plot(df1['Date'],
             (df1[Price].ewm(span=a, min_periods=a).mean()) - (df1[Price].ewm(span=b, min_periods=b).mean()),
             label='MACD')
    ax[1,1].plot(df1['Date'],
             ((df1[Price].ewm(span=a, min_periods=a).mean()) - (df1[Price].ewm(span=b, min_periods=b).mean())).ewm(
                 span=MA_Days, min_periods=MA_Days).mean(), label='Signal')
    ax[1,1].legend(loc='best')
    ax[1,1].set_title(stock_name + ' MACD Chart',fontsize = 9)
    plt.setp(ax[1, 1].xaxis.get_majorticklabels(), rotation=90)
    plt.setp(ax[1, 1].xaxis.get_majorticklabels(), fontsize=6)
    plt.setp(ax[1, 1].yaxis.get_majorticklabels(), fontsize=6)
    ax[1, 1].set_xlabel('Date', fontsize=8)
    ax[1, 1].set_ylabel(price + ' Price', fontsize=8)
    fig.tight_layout()
    plt.show()


#-------------------------------------
'''
END OF MODULE
'''
#-------------------------------------