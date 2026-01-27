#User function Template for python3
class Solution:
	def getBinaryRep(self, n):
		# code here
		res=""
		for i in range(31,-1,-1):
		    bit=(n>>i)&1
		    res+=str(bit)
		return res