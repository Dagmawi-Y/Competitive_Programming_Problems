class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)
        
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        j = 0
        for i in range(n):
            if chars[i] != ' ' or (j > 0 and chars[i-1] != ' '):
                chars[j] = chars[i]
                j += 1
        
        if j > 0 and chars[j-1] == ' ':
            j -= 1
        
        reverse(chars, 0, j-1)
        
        start = 0
        for end in range(j):
            if end == j-1 or chars[end+1] == ' ':
                reverse(chars, start, end)
                start = end + 2
        
        return ''.join(chars[:j])
