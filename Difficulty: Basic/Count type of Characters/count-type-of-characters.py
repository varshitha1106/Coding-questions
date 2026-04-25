#User function Template for python3

class Solution:
    def count (self,s):
        # your code here
        ucnt=0
        lcnt=0
        ncnt=0
        scnt=0
        for ch in s:
            if ch.isupper():
                ucnt+=1
            elif ch.islower():
                lcnt+=1
            elif ch.isdigit():
                ncnt+=1
            else:
                scnt+=1
        return ucnt, lcnt, ncnt, scnt