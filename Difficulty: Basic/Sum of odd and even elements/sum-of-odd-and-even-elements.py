#User function Template for python3

class Solution:
	def findSum(self, n):
		# Code here
		even=n//2
		odd=n-even
		ESum=even*(even+1)
		OSum=odd*odd
		return OSum, ESum
	
