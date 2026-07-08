class Solution:
    def reverseexponentiation(self, n):
        # code here
        MOD=1000000007
        rev=int(str(n)[::-1])
        def power(a,b):
            result=1
            a%=MOD
            while b>0:
                if b%2==1:
                    result=(result*a)%MOD
                a=(a*a)%MOD
                b//=2
            return result
        return power(n,rev)
