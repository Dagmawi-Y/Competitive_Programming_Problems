class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        rank = {}
        
        # Create a dictionary to store the rank of each number
        for i, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = i
        
        # Build the result list using the rank dictionary
        return [rank[num] for num in nums]
