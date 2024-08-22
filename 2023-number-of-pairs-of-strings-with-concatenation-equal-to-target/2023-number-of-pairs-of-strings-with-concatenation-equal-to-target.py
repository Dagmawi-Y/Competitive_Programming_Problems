class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        from collections import defaultdict
        
        prefix_count = defaultdict(int)
        suffix_count = defaultdict(int)
        result = 0
        
        # Count frequencies of valid prefixes and suffixes
        target_len = len(target)
        for num in nums:
            num_len = len(num)
            
            # Check if num can be a prefix
            if target.startswith(num):
                suffix = target[len(num):]
                if suffix in prefix_count:
                    result += prefix_count[suffix]
            
            # Check if num can be a suffix
            if target.endswith(num):
                prefix = target[:-len(num)]
                if prefix in suffix_count:
                    result += suffix_count[prefix]
            
            # Update counts of prefixes and suffixes
            if target_len > len(num):
                prefix_count[num] += 1
                suffix_count[num] += 1
        
        return result
