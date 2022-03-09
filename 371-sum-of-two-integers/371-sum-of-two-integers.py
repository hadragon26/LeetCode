class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xFFFFFFFF
        
        
        while b != 0:
            
            temp = (b & a) 
            a = (b^a) & mask
            
            b = temp << 1 & mask
            
        max_int = 0x7FFFFFFF
        if a < max_int:
            return a
        else:
            
            result = a ^ mask
            result = ~result
            return result
        
        return  a