class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums.sort()
        n=len(nums)
        res=[]
        def BinarySearch(arr,target):
            left,right=0,len(arr)-1
            while left<=right:
                mid=(left+right)//2
                if(arr[mid]==target):
                    return True
                elif(arr[mid]>target):
                    right=mid-1
                else:
                    left=mid+1
            return False
        for i in range(1,n+1):
            if not BinarySearch(nums,i):
                res.append(i)
        return res
        
                       
                    
                    
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        