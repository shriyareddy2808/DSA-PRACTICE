class Solution(object):
    def findMaxAverage(self, nums, k):
        total = sum(nums[:k])
        maximum = total

        for i in range(k, len(nums)):
            total = total + nums[i] - nums[i-k]
            if total > maximum:
                maximum = total

        return maximum / float(k)
