class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        half = len(nums) / 2
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i in freq:
            if freq[i] > half:
                return i
        