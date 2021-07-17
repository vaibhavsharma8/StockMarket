'''
This is the CLI version file of the stock market analyser. The programs takes input in the CLI
and generates appropriate output based on user selection.
'''
#--------------------------------------------------------------------------------------------------------
'''
All the necessary libraries to create different functions and perform required operations
and enable calculations and potting of results
'''
#---------------------------------------------------------------------------------------
import pandas as pd
import Descriptive_Analysis as DA
import Predictive_Analysis as PA
import datetime
import pandas_datareader as web
import matplotlib.pyplot as plt
from pandas_datareader._utils import RemoteDataError
#---------------------------------------------------------------------------------------
'''
As python shows some warnings which do not impact the output it's important to hide 
the warnings for users as the warning do not concern them.
'''
#---------------------------------------------------------------------------------------
import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
warnings.filterwarnings("ignore", message="Numerical issues were encountered ")

plt.style.use('dark_background')
#---------------------------------------------------------------------------------------
'''
From protecting the program to terminate and run again if wrong input is provided by 
the input variables are set to None so that while error handling the program runs from the point
where wrong input was provided. 
'''
#---------------------------------------------------------------------------------------
stock_name = None
startdate=None
enddate= None
Prediction_Days2 = None
selection = None
MA_Days = None
price_input = None
regressionType = None
trainingData_input = None
trainingData = None
#---------------------------------------------------------------------------------------
'''
ERROR HANDLING of inputs provided by the user.
'''
#---------------------------------------------------------------------------------------
while startdate is None:
    try :
        startdate = input('Enter start date (YYYY-MM--DD):  ')
        datetime.datetime.strptime(startdate,'%Y-%m-%d')
    except ValueError:
        print("Entered date is wrong. Please re-enter")
        startdate=None
while enddate is None:
    try :
        enddate = input('Enter end date (YYYY-MM--DD):  ')
        datetime.datetime.strptime(enddate,'%Y-%m-%d')
    except ValueError:
        print("Entered date is wrong. Please re-enter")
        enddate=None
while stock_name is None:
    try :
        stock_name = input('Enter the Stock Symbol: ')
        start = datetime.datetime.strptime(startdate, '%Y-%m-%d').date()
        end = datetime.datetime.strptime(enddate, '%Y-%m-%d').date()
        #using pandas datareader and consuming the yahoo api for NYSE and NASDAQ stocks
        # a dataframe df is created
        df = web.DataReader(stock_name, 'yahoo', start, end)

    except RemoteDataError as RemoteData:
        print("Wrong Stock Symbol. Please re-enter")
        stock_name=None
while Prediction_Days2 is None:
    try:
        Prediction_Days2 = int(input('Enter the number of days for prediction: '))
    except ValueError:
        print('Prediction Days entered is wrong. Please enter again.')
        Prediction_Days2 = None
while MA_Days is None:
    try:
        MA_Days = int(input('Enter the number of days for MA: '))
    except ValueError:
        print('MA days entered is wrong. Please enter again.')
        MA_Days = None
while MA_Days is None:
    try:
        MA_Days = int(input('Enter the number of days for MA: '))
    except ValueError:
        print('MA days entered is wrong. Please enter again.')
        MA_Days = None
while price_input is None:
    try:
        price_input = int(input('Price selection; enter 1 for Close, 2 for High, 3 for Low, 4 for Open : '))
    except ValueError:
        print('Selection entered is wrong. Please enter again.')
        price_input = None
while trainingData_input is None:
    try:
        trainingData_input = int(input('fraction of training data for prediction; enter 1 for 0.25, 2 for 0.30, 3 for 0.50: '))
    except ValueError:
        print('Fraction Selection entered is wrong. Please enter again.')
        trainingData_input = None
while regressionType is None:
    try:
        regressionType = int(input('Regression Selection; enter 1 for Linear Regression, 2 for Decision Tree Regression: '))
    except ValueError:
        print('Regression Selection entered is wrong. Please enter again.')
        regressionType = None
while selection is None:
    try:
        selection = int(input('Display selection; enter 1 for Descriptive Analysis,2 for Stock Information \n 3 for Predictive Analysis, 4 for Series Graph \n 5 for Candlestick Chart : '))
    except ValueError:
        print('Selection entered is wrong. Please enter again.')
        selection = None
#---------------------------------------------------------------------------------------
'''
As per the user inputs we assign the value of inputs taken in integer for the ease of use
the below code assignes the value to the variables. 
'''
#---------------------------------------------------------------------------------------
if price_input == 1:
    price = 'Close'
elif price_input == 2:
    price = 'High'
elif price_input == 3:
    price = 'Low'
elif price_input == 4:
    price = 'Open'
else:
    price = 'Close'

if trainingData_input == 1:
    trainingData == 0.25
elif trainingData_input == 2:
    trainingData == 0.30
elif trainingData_input == 3:
    trainingData == 0.50
else:
    trainingData == 0.25

Price = [price]
#---------------------------------------------------------------------------------------
'''
Redefining the dataframe and giving names to columns and resetting the index for structure.
'''
#---------------------------------------------------------------------------------------
df1 = pd.DataFrame(df, columns=['High','Low','Open','Close','Volume','Adj Close'])
df1 = df1.reset_index()
pd.options.display.max_columns = None
#---------------------------------------------------------------------------------------
'''
Defining some functions to unit test the length of dataframe created and last element of the dataframe.
'''
#---------------------------------------------------------------------------------------
def data_check_unittest(stockname_unit,start_unit,end_unit):
    data_check = web.DataReader(stockname_unit, 'yahoo', start_unit, end_unit)
    return(data_check)

def data_check_last(stockname_unit,start_unit,end_unit):
    data_last = web.DataReader(stockname_unit, 'yahoo', start_unit, end_unit)
    data_last_element = pd.DataFrame(data_last)
    return(data_last_element)


#---------------------------------------------------------------------------------------
'''
As per user selection of what type of analysis user wants to see a function is created 
where other inputs are passed.
'''
#---------------------------------------------------------------------------------------
def run():
    if selection == 2:
        DA.stock_Info(df1,stock_name,Price,price)

    elif selection == 1:
        DA.Descriptive_Analysis_Terminal(df1,Price)

    elif selection == 5:
        DA.candlestick_Chart(df1)

    elif selection == 4:
        DA.series_graphs(12,26,MA_Days,df1,Price,price,stock_name)

    elif selection == 3 and regressionType == 1:
        PA.linear_Regression_Terminal(df1,Price,price,stock_name,Prediction_Days2,trainingData)
    elif selection == 3 and regressionType == 2:
        PA.decisionTree_Regression_Terminal(df1,Price,price,stock_name,Prediction_Days2,trainingData)

    else:
        print('Thank you for using the program, please run again for alternative analysis')
run()
#-------------------------------------
'''
END OF MODULE
'''
#-------------------------------------














