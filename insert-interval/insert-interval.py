class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        lst = []
        if not intervals:
            return [newInterval]
        
        playing = True
        
        
        for interval in intervals:
            if playing == True and newInterval[0] < interval[0]:
                lst.append(newInterval)
                playing = False
            
            
            if not lst or lst[-1][-1]< interval[0]:
                lst.append(interval)
                
            
            
            if playing == True and lst[-1][-1] >= newInterval[0]:
                lst[-1][-1] = max(newInterval[1],lst[-1][-1])
                playing = False 
            
            if lst[-1][-1] >= interval[0]:
                lst[-1][-1] = max(interval[1],lst[-1][-1])
        
        if playing == True:
            lst.append(newInterval)
                
        return lst