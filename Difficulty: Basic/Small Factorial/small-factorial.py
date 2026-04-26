#User function Template for python3

class Solution:
	def find_fact(self, n):
		# Code here
		if n==0 or n==1:
		    return 1
		fact=1
		for i in range(1,n+1):
		    fact=fact*i
		return fact