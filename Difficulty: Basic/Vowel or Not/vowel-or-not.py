class Solution:
    def isVowel(self, ch: str) -> bool:
        # code here
        vowel="aeiouAEIOU"
        if ch in vowel:
            return True
        else:
            return False
