import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets


def exercise():
    """
    We're going to predict the amount of a sale, so we only want rows that have a Won value for the Opportunity Result
    and then we want to drop that column from the filtered data.
    1. We need to convert the categorical data (e.g., 'Northwest', 'Pacific', etc.) into dummy variables (numbers).
    2. Use the function get_dummies() function for this purpose.
    3. our target is Opportunity Amount USD, so grab that and drop the column from the data frame.
    4. Split the remaining data into training and test data using the train_test_split() function.
    """
    data = pd.read_csv('../src/data/WA_Fn-UseC_-Sales-Win-Loss.csv')
    # print(data.head())

    # Select/Clean the data
    x = data[data['Opportunity Result'] == 'Won'].drop('Opportunity Result', axis=1)
    x = pd.get_dummies(x)
    y = x['Opportunity Amount USD']
    x = x.drop(['Opportunity Number', 'Opportunity Amount USD'], axis=1)

    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(x, y)

    # Create a DataFrame of the coefficients from the regression model
    # Sort the values
    # Display the values
    df = model.coef_
    df.sort()
    print(df)


exercise()
