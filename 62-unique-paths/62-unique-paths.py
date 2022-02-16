class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        grid = [[0 for i in range(n)]for i in range(m)]
        
        
        
        for i in range(n):
            grid[0][i] = 1
            
        for i in range(m):
            grid[i][0] = 1
            
        for row in range(1,m):
            for col in range(1,n):
                grid[row][col] = grid[row-1][col]+grid[row][col-1]
                
        return grid[m-1][n-1]