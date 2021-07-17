'''
This is the module which contains all functions required for predictive analysis of selected inputs by the user.
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
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from tkinter import messagebox
import tkinter as tk
#Defiing the property of matplot charts to set the black background theme.
plt.style.use('dark_background')


#This functions performs the linar regression for GUI file by taking user inputs and predicts the furture price.
def linear_Regression(df1,Price,price,stock_name,Prediction_Days,trainingData):
    df1['prediction'] = df1[Price].shift(-1)
    df1['Date'] = df1['Date'].values.astype(float)
    df1.dropna(inplace=True)
    forecast_period = int(Prediction_Days)
    X = np.array(df1.drop(['prediction'], 1))
    Y = np.array(df1['prediction'])
    X = preprocessing.scale(X)
    X_prediction = X[-forecast_period:]
    x_train, x_test, y_train, y_test = train_test_split(X, Y,train_size=trainingData, test_size=Prediction_Days)
    # This function of the sk.learn library performs the Regression on the training data
    reg = LinearRegression()
    reg.fit(x_train, y_train)
    array_Prediction = (reg.predict(X_prediction))
    #Calculating the error values to obbtain the accuracy of the prediction
    MAE = metrics.mean_absolute_error(y_test,array_Prediction )
    MSE = metrics.mean_squared_error(y_test,array_Prediction )
    rmse = np.sqrt(metrics.mean_squared_error(y_test,array_Prediction ))
    Rsquarevalue = metrics.r2_score(y_test,array_Prediction)
    predictedUserPrice = array_Prediction[Prediction_Days-1]
    tk.messagebox.showinfo("Prediction (press Ok to see graph)","Predicted price after "+ str(Prediction_Days)+" days after end date is: " + str(round(predictedUserPrice,2)) +
                           "\n MAE Value is : " + str(round(MAE,3)) + "\n MSE Value is : " + str(round(MSE,3)) + "\n RMSE Value is : " + str(round(rmse,2)) + "\n R square Value is : " + str(round(Rsquarevalue,2)))
    df1['Date'] = pd.to_datetime(df1['Date'], format='%Y-%m-%d %H:%M:%S.%f')
    df1 = df1.set_index(['Date'])
    row_end = df1.tail(1)
    date1 = row_end[Price].index.date.item(0) + pd.Timedelta(str(Prediction_Days)+' day')
    series = pd.Series(pd.date_range(date1, periods=Prediction_Days, freq='D'))
    array_Prediction = pd.DataFrame(data=array_Prediction,
                                 columns=['prediction'])
    series = pd.DataFrame(series)
    format = '%Y-%m-%d %H:%M:%S'
    array_Prediction['Date'] = pd.to_datetime(series[0], format=format)
    array_Prediction = array_Prediction.set_index(pd.DatetimeIndex(array_Prediction['Date']))
    array_Prediction = array_Prediction.drop('Date', axis=1)
    predictAll = df1['prediction']
    predictAll = pd.DataFrame(predictAll)
    predictAll = pd.concat([predictAll, array_Prediction])
    plt.figure(num='Linear Regression',figsize=(16,8))
    plt.legend(loc='best')
    plt.title(stock_name + ' Prediction Chart for ' + str(Prediction_Days) + ' days', fontsize=9)
    plt.xticks(rotation=90, fontsize=6)
    plt.yticks(fontsize=6)
    plt.xlabel('Date', fontsize=8)
    plt.ylabel('Predicted Price/Close', fontsize=8)
    plt.plot(df1[Price], label = price)
    plt.plot(predictAll, label = 'Predicted Price')
    plt.show()

#This functions performs the linar regression CLI File by taking user inputs and predicts the furture price.
def linear_Regression_Terminal(df1,Price,price,stock_name,Prediction_Days2,trainingData):
    df1['prediction'] = df1[Price].shift(-1)
    df1['Date'] = df1['Date'].values.astype(float)
    df1.dropna(inplace=True)
    forecast_period = int(Prediction_Days2)
    X = np.array(df1.drop(['prediction'], 1))
    Y = np.array(df1['prediction'])
    X = preprocessing.scale(X)
    X_prediction = X[-forecast_period:]
    x_train, x_test, y_train, y_test = train_test_split(X, Y,train_size=trainingData, test_size=Prediction_Days2)
    # This function of the sk.learn library performs the Regression on the training data
    reg = LinearRegression()
    reg.fit(x_train, y_train)
    array_Prediction = (reg.predict(X_prediction))
    # Calculating the error values to obtain the accuracy of the prediction
    MAE = metrics.mean_absolute_error(y_test,array_Prediction )
    MSE = metrics.mean_squared_error(y_test,array_Prediction )
    rmse = np.sqrt(metrics.mean_squared_error(y_test,array_Prediction ))
    Rsquarevalue = metrics.r2_score(y_test,array_Prediction)
    predictedUserPrice = array_Prediction[Prediction_Days2-1]
    print("Predicted price after " + str(Prediction_Days2) + " days after end date is: " + str(
        round(predictedUserPrice, 2)) +
          "\n MAE Value is : " + str(round(MAE, 3)) + "\n MSE Value is : " + str(
        round(MSE, 3)) + "\n RMSE Value is : " + str(round(rmse, 2)) + "\n R square Value is : " + str(
        round(Rsquarevalue, 2)))
    df1['Date'] = pd.to_datetime(df1['Date'], format='%Y-%m-%d %H:%M:%S.%f')
    df1 = df1.set_index(['Date'])
    row_end = df1.tail(1)
    date1 = row_end[Price].index.date.item(0) + pd.Timedelta(str(Prediction_Days2)+' day')
    series = pd.Series(pd.date_range(date1, periods=Prediction_Days2, freq='D'))
    array_Prediction = pd.DataFrame(data=array_Prediction,
                                 columns=['prediction'])
    series = pd.DataFrame(series)
    format = '%Y-%m-%d %H:%M:%S'
    array_Prediction['Date'] = pd.to_datetime(series[0], format=format)
    array_Prediction = array_Prediction.set_index(pd.DatetimeIndex(array_Prediction['Date']))
    array_Prediction = array_Prediction.drop('Date', axis=1)
    predictAll = df1['prediction']
    predictAll = pd.DataFrame(predictAll)
    predictAll = pd.concat([predictAll, array_Prediction])
    plt.figure(num='Linear Regression',figsize=(16,8))
    plt.legend(loc='best')
    plt.title(stock_name + ' Prediction Chart for ' + str(Prediction_Days2) + ' days', fontsize=9)
    plt.xticks(rotation=90, fontsize=6)
    plt.yticks(fontsize=6)
    plt.xlabel('Date', fontsize=8)
    plt.ylabel('Predicted Price/Close', fontsize=8)
    plt.plot(df1[Price], label = price)
    plt.plot(predictAll, label = 'Predicted Price')
    plt.show()

#This functions performs the decision tree regression for GUI file by taking user inputs and predicts the furture price.
def decisionTree_Regression(df1,Price,price,stock_name,Prediction_Days,trainingData):
    df1['prediction'] = df1[Price].shift(-1)
    df1['Date'] = df1['Date'].values.astype(float)
    df1.dropna(inplace=True)
    forecast_period = int(Prediction_Days)
    X = np.array(df1.drop(['prediction'], 1))
    Y = np.array(df1['prediction'])
    X = preprocessing.scale(X)
    X_prediction = X[-forecast_period:]
    x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=trainingData, test_size=Prediction_Days)
    # This function of the sk.learn library performs the decision tree regression on the training data
    reg = DecisionTreeRegressor()
    reg.fit(x_train, y_train)
    array_Prediction = (reg.predict(X_prediction))
    # Calculating the error values to obtain the accuracy of the prediction
    MAE = metrics.mean_absolute_error(y_test, array_Prediction)
    MSE = metrics.mean_squared_error(y_test, array_Prediction)
    rmse = np.sqrt(metrics.mean_squared_error(y_test, array_Prediction))
    Rsquarevalue = metrics.r2_score(y_test, array_Prediction)
    predictedUserPrice = array_Prediction[Prediction_Days - 1]
    tk.messagebox.showinfo("Prediction (press Ok to see graph)",
                           "Predicted price after " + str(Prediction_Days) + " days after end date is: " + str(
                               round(predictedUserPrice, 2)) +
                           "\n MAE Value is : " + str(round(MAE, 3)) + "\n MSE Value is : " + str(
                               round(MSE, 3)) + "\n RMSE Value is : " + str(
                               round(rmse, 2)) + "\n R square Value is : " + str(round(Rsquarevalue, 2)))
    df1['Date'] = pd.to_datetime(df1['Date'], format='%Y-%m-%d %H:%M:%S.%f')
    df1 = df1.set_index(['Date'])
    row_end = df1.tail(1)
    date1 = row_end[Price].index.date.item(0) + pd.Timedelta(str(Prediction_Days) + ' day')
    series = pd.Series(pd.date_range(date1, periods=Prediction_Days, freq='D'))
    array_Prediction = pd.DataFrame(data=array_Prediction,
                                    columns=['prediction'])
    series = pd.DataFrame(series)
    format = '%Y-%m-%d %H:%M:%S'
    array_Prediction['Date'] = pd.to_datetime(series[0], format=format)
    array_Prediction = array_Prediction.set_index(pd.DatetimeIndex(array_Prediction['Date']))
    array_Prediction = array_Prediction.drop('Date', axis=1)
    predictAll = df1['prediction']
    predictAll = pd.DataFrame(predictAll)
    predictAll = pd.concat([predictAll, array_Prediction])
    plt.figure(num='Linear Regression', figsize=(16, 8))
    plt.legend(loc='best')
    plt.title(stock_name + ' Prediction Chart for ' + str(Prediction_Days) + ' days', fontsize=9)
    plt.xticks(rotation=90, fontsize=6)
    plt.yticks(fontsize=6)
    plt.xlabel('Date', fontsize=8)
    plt.ylabel('Predicted Price/Close', fontsize=8)
    plt.plot(df1[Price], label=price)
    plt.plot(predictAll, label='Predicted Price')
    plt.show()

def decisionTree_Regression_Terminal(df1,Price,price,stock_name,Prediction_Days2,trainingData):
    df1['prediction'] = df1[Price].shift(-1)
    df1['Date'] = df1['Date'].values.astype(float)
    df1.dropna(inplace=True)
    forecast_period = int(Prediction_Days2)
    X = np.array(df1.drop(['prediction'], 1))
    Y = np.array(df1['prediction'])
    X_prediction = X[-forecast_period:]
    x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=trainingData, test_size=Prediction_Days2)
    # This function of the sk.learn library performs the decision tree regression on the training data
    reg = DecisionTreeRegressor()
    reg.fit(x_train, y_train)
    array_Prediction = (reg.predict(X_prediction))
    # Calculating the error values to obtain the accuracy of the prediction
    MAE1 = metrics.mean_absolute_error(y_test, array_Prediction)
    MSE1 = metrics.mean_squared_error(y_test, array_Prediction)
    rmse1 = np.sqrt(metrics.mean_squared_error(y_test, array_Prediction))
    Rsquarevalue1 = metrics.r2_score(y_test, array_Prediction)
    predictedUserPrice1 = array_Prediction[Prediction_Days2 - 1]
    print("Predicted price after " + str(Prediction_Days2) + " days after end date is: " + str(
        round(predictedUserPrice1, 2)) +
          "\n MAE Value is : " + str(round(MAE1, 3)) + "\n MSE Value is : " + str(
        round(MSE1, 3)) + "\n RMSE Value is : " + str(
        round(rmse1, 2)) + "\n R square Value is : " + str(round(Rsquarevalue1, 2)))
    df1['Date'] = pd.to_datetime(df1['Date'], format='%Y-%m-%d %H:%M:%S.%f')
    df1 = df1.set_index(['Date'])
    row_end = df1.tail(1)
    date1 = row_end[Price].index.date.item(0) + pd.Timedelta(str(Prediction_Days2) + ' day')
    series = pd.Series(pd.date_range(date1, periods=Prediction_Days2, freq='D'))
    array_Prediction = pd.DataFrame(data=array_Prediction,
                                    columns=['prediction'])
    series = pd.DataFrame(series)
    format = '%Y-%m-%d %H:%M:%S'
    array_Prediction['Date'] = pd.to_datetime(series[0], format=format)
    array_Prediction = array_Prediction.set_index(pd.DatetimeIndex(array_Prediction['Date']))
    array_Prediction = array_Prediction.drop('Date', axis=1)
    predictAll = df1['prediction']
    predictAll = pd.DataFrame(predictAll)
    predictAll = pd.concat([predictAll, array_Prediction])
    plt.figure(num='Linear Regression', figsize=(16, 8))
    plt.legend(loc='best')
    plt.title(stock_name + ' Prediction Chart for ' + str(Prediction_Days2) + ' days', fontsize=9)
    plt.xticks(rotation=90, fontsize=6)
    plt.yticks(fontsize=6)
    plt.xlabel('Date', fontsize=8)
    plt.ylabel('Predicted Price/Close', fontsize=8)
    plt.plot(df1[Price], label=price)
    plt.plot(predictAll, label='Predicted Price')
    plt.show()


#-------------------------------------
'''
END OF MODULE
'''
#-------------------------------------