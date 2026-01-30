class Solution:
    def getAlternates(self, arr):
        # Code Here
        n=len(arr)
        arr1=[]
        for i in range(0,n,2):
            arr1.append(arr[i])
        return arr1