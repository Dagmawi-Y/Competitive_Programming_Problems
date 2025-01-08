class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = ''.join(char.lower() for char in s if char.isalnum())
        
        return filtered_string == filtered_string[::-1]