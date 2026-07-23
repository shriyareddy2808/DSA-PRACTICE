class Solution:
    def reverseSubArray(self, arr, l, r):
        l -= 1
        r -= 1

        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return arr
