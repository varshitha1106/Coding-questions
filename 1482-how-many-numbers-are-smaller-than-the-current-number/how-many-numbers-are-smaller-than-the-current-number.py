class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n=len(nums)
        count=[0]*101
        for i in nums:
            count[i]=count[i]+1
        for i in range(1,101):
            count[i]=count[i]+count[i-1]
        res=[]
        for i in nums:
            if(i==0):
                res.append(0)
            else:
                res.append(count[i-1])
        return res
        

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        