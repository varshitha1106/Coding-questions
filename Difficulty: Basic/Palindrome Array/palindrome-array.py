
from typing import List


class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        # code here
        flag=0
        n=len(arr)
        for i in range(0,n//2):
            if(arr[i]!=arr[n-i-1]):
                flag=1
                break
            else:
                flag=0
        if flag==0:
            return True
        else:
            return False
        
