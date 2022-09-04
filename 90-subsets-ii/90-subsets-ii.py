class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        
        lst = [[]]
        nums.sort()
        
        for i in nums:
            
            
            lst1 = lst[:]
            
            for c in lst1:
                
                x = c[:]
                x.append(i)
                if x not in lst:
                    lst.append(x)
                    
        return lst
                    
            