class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        left_sum = 0
        valid_splits = 0
        for i in range(n - 1):
            left_sum += nums[i]
            right_sum = total - left_sum

            if left_sum >= right_sum:
                valid_splits += 1
        return valid_splits