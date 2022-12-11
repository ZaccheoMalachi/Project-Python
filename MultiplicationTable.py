multiplicationtable=[]
number=float(input('Number:'))
start=int(input('Start:'))
stop=int(input('Stop:'))
def generatemultiplication(num,start,stop):
    result=[]
    for i in range(start,stop+1):
        result.append(num*i)        
    return result
multiplicationtable=generatemultiplication(number,start,stop)
print(multiplicationtable)
even=[]
odd=[]
for i in multiplicationtable:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)