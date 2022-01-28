class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        def calc(x):
            
            return x[0]**2 + x[1]**2
        
        
        heap = []
        ans = []
        
        for point in points:
            
            if len(heap) < k:
            
                heappush(heap,(-calc(point),point))
                
            else:
                 if -heap[0][0]>calc(point):
                        heappop(heap)
                        heappush(heap,(-calc(point),point))
                        
        for i in heap:
            
            ans.append(i[-1])
            
        return ans
            
        
                    
            
            
            
        
        