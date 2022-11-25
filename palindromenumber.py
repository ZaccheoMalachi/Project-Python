def isPalindrome(x: int) -> bool:
    result=0
    if x==0:
        return True
    elif x==1:
        return True
    elif x<0:
        return False
    elif x<10:
        return True
    elif x%10==0:
        return False
    while(x>result):
        result=int(result*10+x%10)
        x=int(x/10)
    if x==result:
        return True
    elif x==int(result/10):
        return True
    else:
        return False
print(isPalindrome(1221))