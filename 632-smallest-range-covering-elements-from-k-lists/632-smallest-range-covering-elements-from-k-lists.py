import math 

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        heap = []
        
        s = -math.inf 
        
        l = math.inf
        
        max_num = -math.inf
        for lst in nums:
            heappush(heap,(lst[0],0,lst))
            max_num = max(lst[0],max_num)
            
        
        while heap:
            
            
            ele,index,ref = heappop(heap)
            
            
            if max_num - ele < l -s:
                l = max_num
                s = ele
                
            if index+1 < len(ref):
                
                heappush(heap,(ref[index+1],index+1,ref))
                max_num = max(max_num,ref[index+1])
            
            elif index+1 >= len(ref):
                break
            
                
                
        return [s,l]
        
        
        
        
                
            
                
            