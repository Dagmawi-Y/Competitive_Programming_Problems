class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2:
            return False
        balance = 0
        available = 0
        
        for i in range(n):
            if locked[i] == '1':
                if s[i] == '(':
                    balance += 1
                else:
                    balance -= 1
            else:
                available += 1
            if balance + available < 0:
                return False
        balance = 0
        available = 0
        
        for i in range(n-1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    balance += 1
                else:
                    balance -= 1
            else:
                available += 1

            if balance + available < 0:
                return False
        
        return True