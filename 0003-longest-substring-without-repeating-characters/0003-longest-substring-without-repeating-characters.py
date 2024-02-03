class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        longest_length = 0

        for i in s:
            if i not in substring:
                substring += i
                longest_length = max(longest_length, len(substring))
            else:
                substring = substring[substring.index(i) + 1:] + i

        return longest_length