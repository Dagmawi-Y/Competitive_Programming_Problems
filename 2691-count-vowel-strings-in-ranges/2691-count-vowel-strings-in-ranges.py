class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        def is_vowel_word(word):
            return word[0] in vowels and word[-1] in vowels
        
        valid_words = [is_vowel_word(word) for word in words]
        
        prefix_sum = [0] * (len(words) + 1)
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + valid_words[i - 1]
        
        result = []
        for li, ri in queries:
            result.append(prefix_sum[ri + 1] - prefix_sum[li])
        
        return result