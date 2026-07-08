class Solution:
    def noOfWays(self, m,n,x):
        # code here
        dp=[[-1]*(x+1) for _ in range(n+1)]
        def solve(dice,target):
            if dice==0:
                return 1 if target==0 else 0
            if target <0:
                return 0
            if dp[dice][target]!=-1:
                return dp[dice][target]
            ways=0
            for face in range(1,m+1):
                ways+=solve(dice-1,target-face)
            dp[dice][target]=ways
            return ways
        return solve(n,x)
        
