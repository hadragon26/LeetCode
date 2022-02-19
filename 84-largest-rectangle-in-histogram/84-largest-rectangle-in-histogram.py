class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        area  = 0
        length = len(heights)
        
        stack = []
        
        for index,height in enumerate(heights):
            
            
            if not stack:
            
                stack.append((index,height))
            else:
                top = stack[-1][-1]
                
                if height>= top:
                    stack.append((index,height))
                    
                else:
                    print(True)
                    start = index
                    
                    while stack and stack[-1][1] > height:
                        
                        index1,height1 = stack.pop()
                        
                        area = max(area,height1*(index-index1))
                        
                        start = index1
                        
                    
                        
                    stack.append((start,height))
                    
        
        for ele in stack:
            area = max(area,ele[-1]*(length-ele[0]))
            
        return area
            
            
                        
                        
                        
                    
                
                
        
        
        
                
            
            
            