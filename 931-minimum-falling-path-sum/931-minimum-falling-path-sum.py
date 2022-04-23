class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        dic = {}
        l = len(matrix)
        c = len(matrix[0])
        
        
        def dfs(row,col):
            
            if (row,col) in dic:
                return dic[(row,col)]
            
            if row<0 or row >= l:
                return 0
            
            
            
            if col-1 <0:
                dic[(row,col)] = min(dfs(row+1,col) , dfs(row+1,col+1)) + matrix[row][col]
                
            elif col+1>=l:
                dic[(row,col)] = min(dfs(row+1,col), dfs(row+1,col-1)) + matrix[row][col]
            
            else:
                dic[(row,col)] = min(dfs(row+1,col), dfs(row+1,col-1) , dfs(row+1,col+1)) + matrix[row][col]
            
            return dic[(row,col)]
            
        mi = float('inf')
            
        for i in range(c):
            mi = min(mi,dfs(0,i))
            
        return mi
            
            