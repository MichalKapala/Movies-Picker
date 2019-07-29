from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

data = pd.read_csv('train.csv', header=None)
X = data.iloc[:, [1,2,3,4,5,6,7,8,9, 10]]
y = data.iloc[:, 0]
X_test = pd.read_csv('test.csv', header=None)

#sc = StandardScaler()
#X = sc.fit_transform(X)
#X_test = sc.transform(X_test)


lr = LinearRegression()
lr.fit(X, y)
y_pred = lr.predict(X_test)
print(y_pred)