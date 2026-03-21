#User function Template for python3


class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
        S=0
        while(n>0):
            ld=n%10
            S+=ld
            n//=10
        temp=S
        rev=0
        while(S>0):
            ld=S%10
            rev=(rev*10)+ld
            S//=10
        return rev==temp
        
        