class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        sec = len(secondList)
        fir = len(firstList)
        ans = []
        
        if not secondList or not firstList:
            return ans
        
        t_sec = 0 
        t_fir = 0 
        
        while t_fir<fir and t_sec<sec:
            
            lo = max(secondList[t_sec][0],firstList[t_fir][0])
            hi = min(secondList[t_sec][1],firstList[t_fir][1])
            
            
            if lo<=hi:
                ans.append([lo,hi])
                
            if secondList[t_sec][1]<firstList[t_fir][1]:
                t_sec+=1
            else:
                t_fir+=1
                
        return ans
            
        
        
        
        
        
        
        
        
        
        