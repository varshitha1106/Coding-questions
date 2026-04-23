#User function Template for python3

class Solution:
    def countDivisors(self, n):
        # code here
        cnt=0
        for i in range(1,n+1):
            if n%i==0 and i%3==0:
                cnt+=1
        return cnt
                
            