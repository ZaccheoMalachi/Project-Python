def ctof (temp:float)->float:
    return (temp*9/5)+32
def ftoc (temp:float)->float:
    return (temp-32)*5/9
def ctok (temp:float)->float:
    return temp+273.15
def ktoc (temp:float)->float:
    return temp-273.15
def ftok (temp:float)->float:
    return ctok(ftoc(temp))
def ktof (temp:float)->float:
    return ctof(ktoc(temp))
print('pick option')
print('ctof','ftoc','ctok','ktoc','ftok','ktof')
choices=('ctof','ftoc','ctok','ktoc','ftok','ktof')
choice=input('choice:')
temp=float(input('temp:'))
if choice==choices[0]:
    print(ctof(temp))
elif choice==choices[1]:
    print(ftoc(temp))
elif choice==choices[2]:
    print(ctok(temp))
elif choice==choices[3]:
    print(ktoc(temp))
elif choice==choices[4]:
    print(ftok(temp))
elif choice==choices[5]:
    print(ktof(temp))

