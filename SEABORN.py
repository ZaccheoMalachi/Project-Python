import matplotlib.pyplot as mp
import pandas as ps
import seaborn as sb
import numpy as np
sb.set()
# x=np.linspace(0,10,1000)
# mp.plot(x,np.sin(x),x,np.cos(x))
# mp.show()
# data=sb.load_dataset('tips')
# print(data.head(10))
# sb.relplot(x='total_bill',y='tip',data=data,kind='scatter',hue='time',col='sex',style='smoker')
# mp.show()
data=sb.load_dataset('flights')
print(data.head(10))
sb.relplot(x='year',y='passengers',data=data,kind='line',hue='month')
mp.show()