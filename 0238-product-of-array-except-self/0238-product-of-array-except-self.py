class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # Initialize the output array with 1s
        output = [1] * n
        
        # Calculate prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        # Calculate suffix products and finalize the result
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output
