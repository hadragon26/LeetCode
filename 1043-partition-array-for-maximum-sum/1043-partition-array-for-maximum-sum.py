class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        dp = [0 for i in range(len(arr))]
        
        ma = 0 
        
        for i in range(len(arr)):
            
            if i < k:
                
                ma = max(ma,arr[i])
                
                dp[i] = ma*(i+1)
                
                
            else:
                
                ma = 0 
                for j in range(1,k+1):
                    
                    ma = max(ma,arr[i-j+1])
                    
                    tmp = ma*j+dp[i-j]
                    dp[i] = max(dp[i],tmp)
                    
                    
        return dp[-1]