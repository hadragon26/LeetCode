class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxh = []
        
        minh = []
        
        med = []
        n = 0
        
        while n<k:
            
            
            heappush(maxh,-heappushpop(minh,nums[n]))
            
            if len(maxh)>len(minh):
                heappush(minh,-heappop(maxh))
            n+=1
            
        def get():
            if len(maxh) == len(minh):
                med.append((-maxh[0]+ minh[0])/2)
            else:
                 med.append(minh[0])
            
        get()
        
        def remove(ele,heap):
            i = heap.index(ele)
            heap[i] = heap[-1]
            del heap[-1]
            
            if i < len(heap):
                heapq._siftup(heap, i)
                heapq._siftdown(heap, 0, i)
                
        def check(ele):
            if ele < minh[0]:
                remove(-ele,maxh)
            else:
                remove(ele,minh)
                
        while n<len(nums):
            check(nums[n-k])
            heappush(maxh,-heappushpop(minh,nums[n]))
            
            if len(maxh) > len(minh):
                heappush(minh,-heappop(maxh))
            
            n+=1 
            get()
            
        return med
                
        
                
            
            
                
