class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        length = len(prices)
        
        p = 0 
        for i in range(length-1):
            
            
            if prices[i] <= prices[i+1]:
                d= prices[i+1] - prices[i]
                p+= d
        return p
                
                