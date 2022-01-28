class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        for num in nums:
            
            if len(self.heap)<k:
                heappush(self.heap,num)
            else:
                if num>self.heap[0]:
                    heappop(self.heap)
                    heappush(self.heap,num)
                    
    def add(self, val: int) -> int:
        
        if self.heap and val>self.heap[0] and len(self.heap)>=self.k:
            heappop(self.heap)
            heappush(self.heap,val)
        elif len(self.heap)<self.k:
            heappush(self.heap,val)
        
        return self.heap[0]
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)