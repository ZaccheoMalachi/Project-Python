import numpy as np
from random import *
# number=[]
# for i in range(6):
#     number.append(randint(1,10))
# print(type(number))
# print(type(np.random.randint(1,11,6)))
number=(np.random.randint(1,11,size=(7,3)))
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
# print(number[4,0,3:6])
# print(number[:2,:4]) SUB ARRAY WITH 2 ROWS AND 4 COLUMNS
# print(number[:4,::2]) SUB ARRAY WITH 4 ROWS AND EVEN COLUMNS
#print(number[::-1,::-1]) #SUB ARRAY WITH REVERSE ROWS AND COLUMNS]
subArray=number[:3,1:4].copy()
print(subArray)
subArray[0,1]=17
print(subArray)
print(number)
print(number.transpose())
print(number.reshape(3,7))
print(np.concatenate([number.transpose()[2],number.reshape(3,7)[2]]).max())
print(np.concatenate([number.transpose()[2],number.reshape(3,7)[2]]).min())
print(np.concatenate([number.transpose()[2],number.reshape(3,7)[2]]).sum())