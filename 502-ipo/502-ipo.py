class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        h_profit = [] 
        h_capital = []
        number = 0 
        
        for i in range(len(profits)):
            
            heappush(h_capital,(capital[i],profits[i]))
            
        
            
        while number<k and number<len(profits):
            if h_capital and  h_capital[0][0]> w:
                if not h_profit:
                    break
                y = heappop(h_profit)
                w+= -y[0]
            else:
                while h_capital and h_capital[0][0]<= w:
                    x = heappop(h_capital)
                    heappush(h_profit,(-x[1],x[0]))
                
            
                y = heappop(h_profit)
                
                w+= -y[0]
            number += 1
            
        return w
        
            
        