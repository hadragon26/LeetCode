class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        
        dic = {0:-1}
        
        su = 0 
        for index,num in enumerate(nums):
            
            su += num
            
            rem = su%k
            
            if rem not in dic:
                dic[rem] = index
                
            elif rem in dic:
                if index - dic[rem] >1:
                    return True
                
        return False