class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        
        dp = [[0 for i in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        ans = 0
        
        for row in range(1,len(matrix)+1):
            for col in range(1,len(matrix[0])+1):
                
                if matrix[row-1][col-1] =="1":
                    dp[row][col] = min(dp[row-1][col],dp[row][col-1],dp[row-1][col-1])+1
                
                
                ans = max(ans,dp[row][col])
                
        return ans*ans
        
        
        