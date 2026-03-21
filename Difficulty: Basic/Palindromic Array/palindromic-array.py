# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    # Code here
    for i in arr:
        if not is_Palindrome(i):
            return False
    return True
    
def is_Palindrome(n):
    temp=n
    rev=0
    while(n>0):
        ld=n%10
        rev=(rev*10)+ld
        n//=10
    return temp==rev
    
