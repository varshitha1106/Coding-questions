class Solution(object):
    def containsDuplicate(self, nums):
        '''n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if(nums[i]==nums[j]):
                    return True
        return False
        '''
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen_numbers=set()
        for i in nums:
            if i in seen_numbers:
                return True
            seen_numbers.add(i)
        return False