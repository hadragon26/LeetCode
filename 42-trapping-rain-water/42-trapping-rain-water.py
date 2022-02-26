class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        l = 0
        r = len(height) -1
        su = 0 
        ma_l = 0
        ma_r = height[-1]
        
        while l<=r:
            
            
            while ma_l<= ma_r and l<=r:
                
                if ma_l - height[l] >0:
                    su+= ma_l - height[l]
                
                
                ma_l= max(ma_l,height[l])
                l+= 1 
                
            while ma_r < ma_l and l<=r:
                if ma_r- height[r]>0:
                    su+= ma_r- height[r]
                
                ma_r = max(ma_r,height[r])
                r-=1
        
        return su
                
                
            
            
            
            
        
        