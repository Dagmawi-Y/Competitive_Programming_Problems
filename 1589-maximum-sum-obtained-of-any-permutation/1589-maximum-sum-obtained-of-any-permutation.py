class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        freq = [0] * (n + 1)
        
        for start, end in requests:
            freq[start] += 1
            if end + 1 < n:
                freq[end + 1] -= 1
        
        for i in range(1, n):
            freq[i] += freq[i - 1]
        
        freq = freq[:-1]
        
        freq.sort()
        nums.sort()
        
        max_sum = 0
        for f, num in zip(freq, nums):
            max_sum = (max_sum + f * num) % MOD
        
        return max_sum
