class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        
        heap = []
        ans = []
        
        count  = 0
        
        
        
        
        
        for i in range(min(len(nums1),k)):
            
            for j in range(min(len(nums2),k)):
                
                num = nums1[i]
                num1 = nums2[j]
                if len(heap)< k:
            
                    heappush(heap,(-(num+num1),[num,num1]))
                else:
                    if -heap[0][0]> num1+num:
                        heappop(heap)
                        heappush(heap,(-(num+num1),[num,num1]))
                        
                        
            
            
        while heap:
            ans.append(heappop(heap)[1])
            
        return ans
            
            
        
        
        
        
        
        
        
        
        
        