class Solution:
	def binaryToDecimal(self, b):
		# code here
		n=0
		for i in b:
		    n=n*2+int(i)
		return n
