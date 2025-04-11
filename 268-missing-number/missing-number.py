class Solution(object):
    def missingNumber(self, nums):
        '''n=len(nums)
        for i in range(0,n+1):
            flag=0
            for j in range(0,n):
                if(nums[j]==i):
                    flag=1
                    break  
            if(flag==0):
                return i
                '''
        n=len(nums)
        total=n*(n+1)//2
        ans=total-sum(nums)
        return ans

        """
        :type nums: List[int]
        :rtype: int
        """
        