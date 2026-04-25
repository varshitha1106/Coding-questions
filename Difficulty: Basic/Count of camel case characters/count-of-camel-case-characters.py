#User function Template for python3

class Solution:
    def countCamelCase (self,s):
        # your code here
        cnt=0
        for ch in s:
            if ch.isupper():
                cnt+=1
        return cnt