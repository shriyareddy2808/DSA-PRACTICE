class Solution:
	def closestPalindrome(self, num):
		# code here
		n=len(num)
		x=int(num)
		if num ==num[::-1]:
		    return num
		candidates=set()
		candidates.add(10**(n-1)-1)
		candidates.add(10**n+1)
		prefix=int(num[:(n+1)//2])
		for p in [prefix-1,prefix,prefix+1]:
		    s=str(p)
		    if n%2==0:
		        pal=int(s+s[::-1])
		    else:
		        pal=int(s+s[:-1][::-1])
		    candidates.add(pal)
	    ans=None
	    for p in candidates:
	        if ans is None:
	            ans=p
	        elif abs(p-x)<abs(ans-x):
	            ans=p
	        elif abs(p-x)==abs(ans-x) and p<ans:
	            ans=p
	    return str(ans)
	   
		  
		
		    
	
	
