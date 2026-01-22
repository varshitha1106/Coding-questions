#User function Template for python3

class Solution:
    def sumOfMatrix(self,N,M,Grid):
        #code here
        Sum=0
        for N in Grid:
            for M in N:
                Sum=Sum+M
        return Sum