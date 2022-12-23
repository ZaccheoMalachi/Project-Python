def isprime(number):
    if number<2:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True
num=int(input('Number:'))
if isprime(num):
    print('Number is prime')
else:
    print('Number is not prime')