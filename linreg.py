import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import scipy.stats.linregress

# Pre processing 
dataset = pd.read_csv('dataVarFinal.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

plt.scatter(X_train, y_train, color = 'red')
# The regression line
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Energy vs Price (Training Set)')
plt.xlabel('Energy')
plt.ylabel('Price')
plt.show()

plt.scatter(X_test, y_test, color = 'black')
plt.plot(X_train, regressor.predict(X_train), color = 'red')
plt.title('Energy vs Price (Test Set)')
plt.xlabel('Energy')
plt.ylabel('Price')
plt.legend()
plt.show()
