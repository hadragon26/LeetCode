class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        
        heap = [0]
        
        coords = []
        
        
        for ele in buildings:
            coords.append((ele[0],-ele[-1]))
            coords.append((ele[1],ele[-1]))
            
        coords.sort()
        
        
        
        
        result = []
        
        
        
        
        for i in coords:
            prevMax = heap[0]
            
            if i[1]>0:
                heap.remove(-i[1])
                heapify(heap)
            
            
            
            else:
                heappush(heap,i[1])
                
                
            if prevMax!=heap[0]:
                result.append([i[0],-heap[0]])
                
            
                
                
        return result