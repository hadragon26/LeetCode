class Solution:
    def maxArea(self, height: List[int]) -> int:
       
        start = 0 
        
        end = len(height) -1 
        
        dist = end - start 
        area = min(height[start],height[end])*dist
        
        while end > start:
            
            if height[end]>height[start]:
                
                
                start += 1 
                dist -=1 
                    
            else:
            
                end -= 1 
                dist -=1 
                    
            area = max(area,min(height[start],height[end])*dist)
            
            
        return area
        
        
            
            
            
        