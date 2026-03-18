class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set=set()
        left=0
        max_sum=0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left=left+1
            char_set.add(s[right])
            max_sum=max(max_sum,right-left+1)
        return max_sum