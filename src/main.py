import pandas as pd
import numpy as np

def get_data():
    # read data from csv file
    data = pd.read_csv('data.csv', index_col=0)
    return data

def get_return(data):
    # calculate the return of each stock
    return data.pct_change()

def get_covariance(data):
    # calculate the covariance matrix
    return data.cov()

def get_correlation(data):
    # calculate the correlation matrix
    return data.corr()

def get_mean(data):
    # calculate the mean of each stock
    return data.mean()

def get_portfolio(data, weight):
    # calculate the return of each stock
    return_data = get_return(data)
    # calculate the covariance matrix
    cov = get_covariance(return_data)
    # calculate the mean of each stock
    mean = get_mean(return_data)
    # calculate the portfolio return
    portfolio_return = np.dot(weight, mean)
    # calculate the portfolio variance
    portfolio_variance = np.dot(np.dot(weight, cov), weight.T)
    # calculate the portfolio standard deviation
    portfolio_std = np.sqrt(portfolio_variance)
    return portfolio_return, portfolio_std
