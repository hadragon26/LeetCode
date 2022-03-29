class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        dic = {}
        
        
        for i in nums3:
            for x in nums4:
                su = i+x
                if su in dic:
                    dic[su]+=1
                else:
                    dic[su]=1
                    
        ans = 0 
                    
        for c in nums1:
                for d in nums2:
                    su = c+d
                    if -su in dic:
                        ans+=dic[-su]
        return ans
        
        
        
        
                        
                        
                
                
                