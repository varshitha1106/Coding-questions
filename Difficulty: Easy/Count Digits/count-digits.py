class Solution:
    def countDigits(self, n):
        count=0
        while(n>0):
            digit=n%10
            count=count+1
            n=n//10
        return count