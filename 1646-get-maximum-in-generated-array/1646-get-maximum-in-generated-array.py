class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        
        if n ==0:
            return 0 
        if n ==1 :
             return 1 
        lst = [0 for i in range(n+1)]
        
        lst[0],lst[1] = 0 ,1 
        
        ma = 1 
        
        t = 2 
        
        while t<= n:
            if t%2 == 0:
                lst[t] = lst[t//2]
            else:
                lst[t] = lst[t//2] + lst[(t//2)+1]
                
            ma = max(ma,lst[t])
            
            t+=1
            
        return ma