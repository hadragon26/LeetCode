class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        
        n= len(matrix[0])
        
        
        count = 0
        for lst in matrix:
            heappush(heap,(lst[0],0,lst))
            
        while heap:
            
            ele,index,ref = heappop(heap)
            count +=1 
            
            if count == k:
                return ele
            
            
            if index+1<n:
                heappush(heap,(ref[index+1],index+1,ref))