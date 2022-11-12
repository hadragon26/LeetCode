class MedianFinder:

    def __init__(self):
        
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        
        if not self.maxheap and not self.minheap:
        
            heappush(self.minheap,num)
            
        elif num > self.minheap[0]:
             heappush(self.minheap,num)
        else:
             heappush(self.maxheap,-num)
            
            
        
        
        if len(self.minheap) > len(self.maxheap)+1:
            heappush(self.maxheap,-heappop(self.minheap))
            
        elif len(self.minheap) <len(self.maxheap):
            heappush(self.minheap,-heappop(self.maxheap))
        

    def findMedian(self) -> float:
        
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0])/2
        else:
            return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()