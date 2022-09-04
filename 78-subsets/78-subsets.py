class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        
        for i in nums:
            
            c = res[:]
            #print(c)
            for x in c:
                
                y = x[:]
                y.append(i)
                res.append(y)
                
                
                
        return res
            
            