class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        lst = []
        
        temp = 0
        
        for num in nums:
            temp ^= num
            
        for num in nums:
            if temp^num in nums:
                lst.append(num)
        return lst