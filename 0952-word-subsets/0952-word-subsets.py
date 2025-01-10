class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count_freq(word):
            freq = {}
            for char in word:
                freq[char] = freq.get(char, 0) + 1
            return freq

        freq_b = {}
        for word in words2:
            word_freq = count_freq(word)
            for char, count in word_freq.items():
                freq_b[char] = max(freq_b.get(char, 0), count)
        
        result = []

        for word in words1:
            freq_a = count_freq(word)
            if all(freq_a.get(char, 0) >= freq_b[char] for char in freq_b):
                result.append(word)

        return result
