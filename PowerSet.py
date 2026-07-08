class Solution:
	def powerSet(self, s):
		# Code here
		ans=[]
		def solve(index,curr):
		    if index==len(s):
		        ans.append(curr)
		        return
		    solve(index+1,curr+s[index])
		    solve(index+1,curr)
		solve(0,"")
		ans.sort()
		return ans
