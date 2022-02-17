class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        rows = len(grid)
        cols = len(grid[0])
        
        
        for i in range(1,cols):
            grid[0][i] += grid[0][i-1]
            
        for i in range(1,rows):
            grid[i][0]+= grid[i-1][0]
            
        for row in range(1,rows):
            for col in range(1,cols):
                
                grid[row][col] = min(grid[row-1][col]+grid[row][col],grid[row][col-1]+grid[row][col])
                
        return grid[rows-1][cols-1]
                
                
                
                
                
                
        
        
        
        
        