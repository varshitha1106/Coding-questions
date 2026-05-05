class Solution:
	def isAutomorphic(self, n):
		# code here
		square=n*n
		if str(square).endswith(str(n)):
		    return "Automorphic"
		return "Not Automorphic"
