class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

    
        
        List =sorted(intervals,key = lambda x:x[0])
        
        ans = []
        
        
        for interval in List:
            if not ans:
                ans.append(interval)
                
            if ans[-1][-1] >=interval[0]:
                ans[-1][-1] = max(ans[-1][-1],interval[1])
            else:
                ans.append(interval)
                
        return ans
    
    
    
            
        
            
                
            