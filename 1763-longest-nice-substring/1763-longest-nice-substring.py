class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_nice(sub):
            return all(ch.lower() in sub and ch.upper() in sub for ch in set(sub))
        
        longest = ""
        n = len(s)
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                substr = s[i:j]
                if is_nice(substr) and len(substr) > len(longest):
                    longest = substr
        
        return longest
