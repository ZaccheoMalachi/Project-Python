import matplotlib.pyplot as mp
import pandas as ps
import seaborn as sb
data=sb.load_dataset('iris')
# sb.catplot(x='sex',y='total_bill',data=data,kind='violin',hue='size')
# mp.show()
print(data.shape)
sb.catplot(x='species',y='petal_width',data=data,kind='violin')
mp.show()