class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        
        
        
        
        su = []
        
        for i in range(len(gas)):
            
            
            
            su.append(gas[i]-cost[i])
            
            
        if sum(su) <0:
            return -1
        
        start = 0
        check = 0
        for l in range(len(gas)):
            
            check+= su[l]
            if check<0:
                start=l+1
                
                check = 0
            
        return start
                
                
            
            
            
       
            
        
            
            
            
        
            
        
        
        
        
            
        
        
        
        
        