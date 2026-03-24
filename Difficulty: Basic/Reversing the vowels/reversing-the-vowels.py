#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        vowels="aeiou"
        rev=""
        for ch in s:
            if ch in vowels:
                rev+=ch
        rev=rev[::-1]
        res=""
        j=0
        
        for ch in s:
            if ch in vowels:
                res+=rev[j]
                j+=1
            else:
                res+=ch
        return res
        
        
                