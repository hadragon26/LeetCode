class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        maxh = []
        
        minh = []
        
        median = [] 
        
        
        n = 0 
        
        
        while n<k:
            
            heappush(maxh,-heappushpop(minh,nums[n]))
            
            if len(maxh) > len(minh):
                heappush(minh,-heappop(maxh))
            n+=1
            
        
                
                
        def med(maxh,minh):
            if len(maxh) == len(minh):
                median.append((-maxh[0] + minh[0])/2)
                
            else:
                median.append(minh[0])                 
                    
        med(maxh,minh)
            
        def remove(heap,ele):
            i = heap.index(ele)
            heap[i] = heap[-1]
            del heap[-1]
            
            if i < len(heap):
                heapq._siftup(heap, i)
                heapq._siftdown(heap, 0, i)
            
            
        def check(ele):
            
            if ele<minh[0]:
                remove(maxh,-ele)
            else:
                remove(minh,ele)
        
        
        while n<len(nums):
            check(nums[n-k])
            heappush(maxh,-heappushpop(minh,nums[n]))
            
            if len(maxh) > len(minh):
                heappush(minh,-heappop(maxh))
                
            med(maxh,minh)
            
            n+=1
            
            
        return median
            

                
                    
                    
                    
            
            
        
        
        
        
        
        
            
            
        
            
        
        