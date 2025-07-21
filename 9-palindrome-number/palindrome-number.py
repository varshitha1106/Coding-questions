class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        '''numstr=str(x)
        rev_string=numstr[ : :-1]
        if(numstr==rev_string):
            return True
        else:
            return False'''
        
        if(x<0):
            return False

        rev=0
        original=x
        while(x!=0):
            lastdigit=x%10
            rev=(rev*10)+lastdigit
            x=x//10
        return(original==rev)
            
        