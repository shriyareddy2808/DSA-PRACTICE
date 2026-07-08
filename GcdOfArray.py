from math import gcd
class Solution:
    def gcd(self, n, arr):
        # code here 
        ans=arr[0]
        for i in range(1,n):
            ans=gcd(ans,arr[i])
        return ans
        
