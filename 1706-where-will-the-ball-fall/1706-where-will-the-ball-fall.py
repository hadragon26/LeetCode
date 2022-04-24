class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        ma = len(grid[0])
        dic = {}
        
        def dfs(row,col):
            
            if (row,col) in dic:
                return dic[(row,col)]
            
            if col<0:
                return -1
            if col>= ma:
                return -1
            if row >= len(grid):
                return col
            
            
            if col+1<ma and grid[row][col] == 1:
                if grid[row][col+1] == -1:
                    dic[(row,col)] = -1
                    return -1
            
                
                dic[(row,col)] = dfs(row+1,col+1)
            else:
                if col -1 >=0 and grid[row][col-1] == 1:
                    dic[(row,col)] = -1
                    return -1
                dic[(row,col)] = dfs(row+1,col-1)
                
            return dic[(row,col)]
                
        ans = []
        
        for col in range(ma):
            ans.append(dfs(0,col))
            
        return ans 
        
        
        
                
        
            
            
            
            