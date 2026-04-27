#User function Template for python3

class Solution:
	def sum_of_gp(self, n, a, r):
		# Code here
		Sum=0
		nums=[]
		curr=a
		for i in range(n):
		    nums.append(curr)
		    curr*=r
		for j in nums:
		    Sum+=j
		return Sum
		    