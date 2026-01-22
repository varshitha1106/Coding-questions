class Solution:
    def sumOfDigits(self, n):
        # code here
        Sum=0
        while(n>0):
            digit=n%10
            Sum=Sum+digit
            n=n//10
        return Sum
        