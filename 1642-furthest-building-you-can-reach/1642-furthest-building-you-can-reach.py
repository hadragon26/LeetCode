class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
         
        
        
        min_lst =  []
        
        
        for index,ele in enumerate(heights):
            
            
            if index == 0:
                continue
                
            diff = ele - heights[index-1]
            
            
            
            if diff<=0:
                continue
                
            else:
                heappush(min_lst,diff)
                
                
            if len(min_lst)>ladders:
                
                track = heappop(min_lst)
                
                bricks -= track
                 
                
            if bricks <0:
                return index-1
            
        return len(heights)-1
            
                    
                
                
            