class Solution:
    def longest(self, arr):
        # code here
        max_word=arr[0]
        
        for i in arr:
            if len(max_word)<len(i):
                max_word=i
        return max_word
                
                
            