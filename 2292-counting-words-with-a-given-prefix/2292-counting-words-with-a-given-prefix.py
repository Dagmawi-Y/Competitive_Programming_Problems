class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = 0
        for word in words:
            if word.startswith(pref):
                n += 1
        return n
            
          