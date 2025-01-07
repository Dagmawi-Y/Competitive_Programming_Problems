class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        count = 0
        moves = 0
        
        for i in range(n):
            answer[i] += moves
            if boxes[i] == '1':
                count += 1
            moves += count
        count = 0
        moves = 0
        
        for i in range(n-1, -1, -1):
            answer[i] += moves
            if boxes[i] == '1':
                count += 1
            moves += count
        
        return answer