import numpy as np
from sklearn.linear_model import LinearRegression

def predict_trend(values):

    X = np.arange(len(values)).reshape(-1,1)
    y = np.array(values)

    model = LinearRegression()
    model.fit(X,y)

    future = model.predict([[len(values)+1]])

    return float(future[0])