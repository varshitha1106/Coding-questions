#User function Template for python3
import math
class Solution:
	def distance(self, x1, y1, x2, y2):
		# Code here
		d=((x2-x1)**2)+((y2-y1)**2)
		res=math.sqrt(d)
		return round(res)
	   