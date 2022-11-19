class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        
        dic ={0:1}
        
        su = 0 
        
        ans = 0
        for num in nums:
            su+=num
            rem = su%k
            
            if rem not in dic:
                dic[rem] =1 
                
            elif rem in dic:
                ans+= dic[rem]
                dic[rem]+=1
                
                
                
        return ans
            
            
            
            