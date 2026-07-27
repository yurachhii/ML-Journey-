import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression


df = pd.read_csv('Boston.csv')


features = df[['crim', 'rm', 'lstat']] # -> for inputs x
target = df['medv'] # -> target y

x_train , x_test , y_train , y_test = sklearn.model_selection.train_test_split(features,target,test_size=0.3,random_state=42)


model = LinearRegression()
model.fit(x_train, y_train)

predictions = model.predict(x_test)

def mse_value(y_test, predictions):
    n = len(y_test)
    return np.sum(np.square(y_test - predictions)) / n

print("Mean Squared Error:", mse_value(y_test, predictions))