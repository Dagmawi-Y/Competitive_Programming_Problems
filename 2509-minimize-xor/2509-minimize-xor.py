class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt = bin(num2).count('1')
        bin_num1 = bin(num1)[2:].zfill(32)
        result = ['0'] * 32
        
        for i in range(32):
            if cnt > 0 and bin_num1[i] == '1':
                result[i] = '1'
                cnt -= 1
                
        if cnt > 0:
            for i in range(31, -1, -1):
                if cnt > 0 and result[i] == '0':
                    result[i] = '1'
                    cnt -= 1
                    
        return int(''.join(result), 2)