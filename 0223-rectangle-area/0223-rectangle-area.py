class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        
        rect1 = (ax2-ax1)*(ay2-ay1)
        rect2 = (bx2-bx1)*(by2-by1) 
        
        
        
        

        if bx1>=ax2 or ax1>=bx2:
            return rect1+rect2
        if by1>=ay2 or ay1 >= by2:
            return rect1+rect2
        else:
            x_range = (max(ax1,bx1),min(ax2,bx2))
            y_range = (max(ay1,by1),min(by2,ay2))
            
            area = (x_range[-1]-x_range[0])*(y_range[-1]-y_range[0])
            return rect1+rect2-area