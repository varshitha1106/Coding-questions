#User function Template for python3

class Solution:
	def diagonalSum(self, mat):
		# Code here
		n=len(mat)
		Sum=0
		for i in range(n):
		    Sum+=mat[i][i]
		    Sum+=mat[i][n-i-1]
		return Sum