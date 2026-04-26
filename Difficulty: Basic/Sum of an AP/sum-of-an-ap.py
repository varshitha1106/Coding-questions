#User function Template for python3

class Solution:
	def sum_of_ap(self, n, a, d):
		# Code here
		Sum=0
		i=0
		while i<n:
		    Sum=Sum+a
		    a=a+d
		    i=i+1
		return Sum