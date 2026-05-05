#User function Template for python3
class Solution:
    def checkPerfectSquare (ob,N):
        # code here 
        if N<0:
            return 0
        odd=1
        while N>0:
            N-=odd
            odd+=2
        if N==0:
            return 1
        else:
            return 0
            