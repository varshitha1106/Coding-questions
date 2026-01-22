# Return true if s is binary, else false
class Solution:
    def isBinary(self, s):
        #code here
        for i in s:
            if i!='1' and i!='0':
                return False
        return True