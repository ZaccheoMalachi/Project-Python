import numpy as np
from random import *
# number=[]
# for i in range(6):
#     number.append(randint(1,10))
# print(type(number))
# print(type(np.random.randint(1,11,6)))
number=(np.random.randint(1,11,size=(5,6,7)))
print(number)
# print(number.ndim)
# print(number.shape)
# print(number.size)
# number2=np.array([1,2,3,4,5])
# print(number2)
# number3=np.ones((7,7))
# print(number3)
# print(np.arange(0,11,2))
# print(np.linspace(0,5,num=17))
print(number[4,0,3:6])