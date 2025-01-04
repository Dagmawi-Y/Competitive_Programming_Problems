class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_palindromes_count = 0
        
        for char in set(s):  
            first_index = s.find(char)
            last_index = s.rfind(char)
            
            if last_index > first_index + 1:  
                middle_unique_chars = set(s[first_index + 1:last_index])
                unique_palindromes_count += len(middle_unique_chars)
        
        return unique_palindromes_count

