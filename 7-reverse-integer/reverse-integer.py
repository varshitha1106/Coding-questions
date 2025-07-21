class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN,INT_MAX=-2**31,2**31+1
        sign=-1 if x<0 else 1
        x=abs(x)
        rev=0
        while(x!=0):
            lastdigit=x%10
            rev=(rev*10)+lastdigit
            x=x//10
        if((rev<INT_MIN) or (rev>INT_MAX)):
            return 0
        return sign*rev
        