#User function Template for python3

class Solution:
    def areMatricesidentical(self,N,Grid1,Grid2):
        #code here
        for i in range(N):
            for j in range(N):
                if(Grid1[i][j]!=Grid2[i][j]):
                    return "0"
        return "1"