# Linear Regression Example
# This script demonstrates how to perform a simple linear regression using Python.

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('common-resources/data/example-data.csv')

# Define variables
X = data[['IndependentVariable']].values
y = data['DependentVariable'].values

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Plot results
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Fitted Line')
plt.xlabel('Independent Variable')
plt.ylabel('Dependent Variable')
plt.title('Linear Regression Example')
plt.legend()
plt.show()
