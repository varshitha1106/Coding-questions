#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        temp=n
        l=len(str(n))
        Sum=0
        while(temp>0):
            ld=temp%10
            Sum+=pow(ld,l)
            temp=temp//10
        return Sum==n