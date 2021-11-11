class Solution:
    def canPartition(self, nums: List[int]) -> bool:
            
        total = sum(nums)
        limit = total//2
        
        
        if total %2 == 1:
            return False
        
        d = set()
        
        d.add(0)
        
        for i in nums:
            new = set()
            for x in d:
                if x+i == limit:
                    return True
                new.add(x)
                new.add(x+i)
            d = new
                
                
        return False
        
        
        
        
        