class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        lst = []
        
        for i in nums:
            if len(lst)<k:
                heappush(lst,i)
            else:
                if i>lst[0]:
                    heappushpop(lst,i)
                    
        return lst[0]