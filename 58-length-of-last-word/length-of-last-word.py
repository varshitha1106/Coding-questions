class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans=len(s.strip().split()[-1])
        return ans