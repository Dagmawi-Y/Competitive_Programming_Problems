class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = 0
        for word in words:
            if len(pref) > len(word):
                continue
            for i in range(len(pref)):
                if pref[i] != word[i]:
                    break
            else:
                n += 1
        return n
            
          