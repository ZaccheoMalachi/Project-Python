import pandas as p
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
data=p.read_csv('machine/WH.csv')
data.rename(columns={'Height(Inches)':'Height(cm)','Weight(Pounds)':'Weight(kg)'},inplace=True)
data['Weight(kg)']=data['Weight(kg)']*0.453592
data['Height(cm)']=data['Height(cm)']*2.54
data2=data.fillna(data.mean())
# print(data2.isnull().sum())
w=data2.drop("Height(cm)",axis='columns')
h=data2.drop("Weight(kg)",axis='columns')
w=w.drop("Gender",axis='columns')
h=h.drop("Gender",axis='columns')
print(h.shape)
X_train, X_test,y_train,y_test = train_test_split(h,w, test_size = 0.2)
print(X_train.shape)
lr=LinearRegression()
lr.fit(X_train,y_train)
height=int(input('HEIGHT(cm):'))
m=lr.coef_
c=lr.intercept_
weight=m*height+c
print('Your estimated weight is',weight)
w_pred=lr.predict(X_test)
# print(lr.score(X_test,y_test))
joblib.dump(lr, "student_weight_predictor.pkl")