"""
Honey Production

Now that you have learned how linear regression works, let’s try it on an example of real-world data.

As you may have already heard, the honeybees are in a precarious state right now. You may have seen articles about the decline of 
the honeybee population for various reasons. You want to investigate this decline and how the trends of the past predict the 
future for the honeybees.

Note: All the tasks can be completed using Pandas or NumPy. Pick whichever one you prefer
"""
import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")
print(df.head())

prod_per_year=df.groupby('year').totalprod.mean().reset_index()

X=prod_per_year['year']
X=X.values.reshape(-1,1)

y=prod_per_year['totalprod']

plt.scatter(X,y)
plt.show()

regr=linear_model.LinearRegression()
regr.fit(X,y)
print(regr.coef_,regr.intercept_)
y_predict=regr.predict(X)
plt.scatter(X,y_predict)
plt.show()

X_future=np.array(range(2013,2051))
X_future=X_future.reshape(-1,1)

future_predict=regr.predict(X_future)

plt.clf()
plt.scatter(X_future,future_predict)
plt.show()
