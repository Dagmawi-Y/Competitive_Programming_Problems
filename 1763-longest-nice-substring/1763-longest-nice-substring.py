class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_nice(sub):
            lower_seen = set()
            upper_seen = set()
            for ch in sub:
                if ch.islower():
                    lower_seen.add(ch)
                else:
                    upper_seen.add(ch)
            return all(ch.upper() in upper_seen for ch in lower_seen) and \
                   all(ch.lower() in lower_seen for ch in upper_seen)
        
        max_length = 0
        longest_substring = ""
        n = len(s)
        
        for start in range(n):
            for end in range(start + 1, n + 1):
                substring = s[start:end]
                if is_nice(substring) and len(substring) > max_length:
                    max_length = len(substring)
                    longest_substring = substring
        
        return longest_substring
