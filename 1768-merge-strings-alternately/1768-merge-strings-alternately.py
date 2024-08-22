class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)
        
        # Alternate merging for the common length
        for i in range(min_len):
            merged.append(word1[i])
            merged.append(word2[i])
        
        # Append the remaining part of the longer string
        merged.extend(word1[min_len:])
        merged.extend(word2[min_len:])
        
        return ''.join(merged)
