class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        numstr=str(x)
        rev_string=numstr[ : :-1]
        if(numstr==rev_string):
            return True
        else:
            return False
        