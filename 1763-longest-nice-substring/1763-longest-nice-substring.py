class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_nice(sub):
            lower = set()
            upper = set()
            for ch in sub:
                if ch.islower():
                    lower.add(ch)
                elif ch.isupper():
                    upper.add(ch)
            return all(ch.upper() in upper for ch in lower) and all(ch.lower() in lower for ch in upper)

        max_len = 0
        longest = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if is_nice(substr) and len(substr) > max_len:
                    max_len = len(substr)
                    longest = substr

        return longest
