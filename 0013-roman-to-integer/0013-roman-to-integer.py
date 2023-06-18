class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        n = len(s)

        for i in range(n):
            value = roman_values[s[i]]

            if i < n - 1 and value < roman_values[s[i + 1]]:
                # If the current value is less than the next value, subtract it
                result -= value
            else:
                result += value

        return result