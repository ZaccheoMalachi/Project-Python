import numpy as np
import matplotlib.pyplot as mp
# mp.plot([1,2,10,2,3,4,1,5,6,8,1,15],linewidth=2,color='red',marker='o')
# mp.title('MONTHLY SALES')
# mp.xlabel('Days')
# mp.ylabel('Sales')
# mp.show()
# x=[1,4,5,2,6]
y=np.array([4,2,6,1,8])
label=['Apple','Mango','Banana','Kiwi','Watermelon']
color=['red','orange','yellow','limegreen','green']
# mp.scatter(x,y)
# mp.barh(x,y)
mp.pie(y,labels=label,colors=color)
mp.show()
