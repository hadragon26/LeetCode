class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        
        num =0 
        count = 0 
        mul = 1
        if dividend < 0 and divisor<0:
            dividend = - dividend
            divisor = - divisor
        elif dividend < 0:
            dividend = - dividend
            mul = -1
        elif divisor<0:
            divisor = - divisor
            mul =-1
        
        
        
        while dividend >=divisor:
            temp = divisor
            mu =1 
            
            while dividend >= temp:
                dividend -= temp
                count+=mu
                temp+=temp
                mu+=mu
                
                
        
                
            
            
       
            
            
        return min(max(count*mul,-2147483648),2147483647)
            
        
        
        
        