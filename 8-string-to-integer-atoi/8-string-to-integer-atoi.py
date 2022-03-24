class Solution:
    def myAtoi(self, s: str) -> int:
        
        
        
        
        mi = -2**(31)
        
        ma = 2**(31) -1 
        
        s= s.strip()
        mul = 1
        start = 0
        if not s:
            return 0 
        
        if s[0] == '-':
            mul =-1
            start = 1
        elif s[0] == '+':
            start = 1
        
        temp = ''
        for i in (s[start:]):
            if i.isdigit():
                temp+=i
            else:
                break
        
        if not temp:
            return 0 
        
        if int(temp)*mul < mi:
            return mi
        if int(temp)*mul > ma:
            return ma
        
        
        return int(temp)*mul
                
            