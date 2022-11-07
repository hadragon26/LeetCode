class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [float('inf') for i in range(amount+1)]
        
        dp[0] = 0 
        
        for index in range(1,amount+1):
            for coin in coins:
                if index-coin>=0:
                    dp[index] = min(1+dp[index-coin],dp[index])
        #print(dp)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
        
        