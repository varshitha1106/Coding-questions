#User function Template for python3

class Solution:
    def findMean(self, arr):
        # code here 
        arrS=sorted(arr)
        n=len(arrS)
        Sum=0
        mean=0
        for i in range(0,n):
            Sum+=arrS[i]
        mean+=Sum//n
        return mean
        
            
        