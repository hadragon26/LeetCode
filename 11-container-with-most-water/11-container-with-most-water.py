class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        
        r = len(height)-1
        
        area = (r-l)*min(height[l],height[r])
        
        while r>l:
            area = max(area,(r-l)*min(height[l],height[r]))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
                       
        return area
                
            
            
        
        
            
            
            
        