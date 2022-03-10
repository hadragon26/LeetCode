class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        su = max(nums)
        
        ma,mi = 1,1
        
        for num in nums:
            
            if num == 0:
                ma,mi =1,1
                
            temp = num*ma
            
            ma = max(num*ma,num*mi,num)
            mi = min(num*mi,temp,num)
            
            su = max(su,ma)
            
        return su
        
            
                