class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        mpp={}
        for i in range(n):
            number=nums[i]
            x=target-number
            if x not in mpp:
                mpp[number]=i
            else:
                return [mpp[x],i]
        return [-1,-1]
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        