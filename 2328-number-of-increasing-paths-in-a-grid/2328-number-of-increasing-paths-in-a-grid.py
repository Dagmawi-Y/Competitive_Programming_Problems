class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]  # Dynamic programming array
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible movement directions

        def dfs(row, col):
            if dp[row][col] != 0:
                return dp[row][col]
            dp[row][col] = 1
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] > grid[row][col]:
                    dp[row][col] += dfs(new_row, new_col)
            return dp[row][col]

        total_paths = 0
        for i in range(rows):
            for j in range(cols):
                total_paths += dfs(i, j)
        
        return total_paths % (10**9 + 7)
        