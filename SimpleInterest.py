def si(p,r,t):
    return p*r*t/100
def total(p,si):
    return p+si
print("welcome to bank mandiri Indonesian")
p=int(input('Principle:'))
if p<50000000:
    r=0.00
elif p<500000000:
    r=0.10
else:
    r=0.60
t=int(input('Time(month):'))/12
print('Your total money will become',total(p,si(p,r,t)))