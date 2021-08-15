from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

traffic=pd.read_csv('slot1.csv')

X=traffic['to_minutes'].values
Y=traffic['Car6'].values

X=X.reshape(-1,1)
Y=Y.reshape(-1,1)
X_train, X_test,y_train,y_test = train_test_split(X,Y, test_size =0.3, random_state=42)

reg=LinearRegression()

reg.fit(X_train,y_train)

y_pred=reg.predict(X_test)
    



