class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        
        dp = [[0 for i in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        
        
        su = 0
        for i in range(1,len(matrix)+1):
            for c in range(1,len(matrix[0])+1):
                
                
                
                if matrix[i-1][c-1] == 1:
                    dp[i][c] = min(dp[i][c-1],dp[i-1][c],dp[i-1][c-1])+1
                    
                su += dp[i][c]
        
        
        
        
                
        return su