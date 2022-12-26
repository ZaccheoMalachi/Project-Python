class Solution:
    def isprime(self,number):
        if number<2:
            return False
        for i in range(2,number):
            if number%i==0:
                return False
        return True
    def ispalindrome(self,number):
        text=str(number)
        if text==text[::-1]:
            return True
        else:
            return False
    def primePalindrome(self, n: int) -> int:
        theprime=n
        while True:
            if self.ispalindrome(theprime):
                if self.isprime(theprime):
                    return theprime
            theprime+=1