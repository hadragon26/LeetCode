class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        
        
        dic ={}
        
        
        for index,i in enumerate(nums):
            
            if i not in dic:
                dic[i] =index
            else:
                if index - dic[i]<=k:
                    return True
                else:
                    dic[i] = index
                    
                    
        return False
            
            