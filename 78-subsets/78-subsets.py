class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ls = [[]]
       
        for num in nums:
            
            ls += [i+[num]for i in ls]
        return ls
                
            