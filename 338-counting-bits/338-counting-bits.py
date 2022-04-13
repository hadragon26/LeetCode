class Solution:
    def countBits(self, n: int) -> List[int]:
        
        
        if n == 0:
            lst = [0]
            return lst
        if n == 1:
            lst = [0,1]
            
            return lst 
        
        if n ==2:
            lst = [0,1,1]
            
            return lst 
        
        lst = [0 for i in range(n+1)]
        
        lst[0],lst[1],lst[2] = 0,1,1
        
        i = 3
        big =2
        
        while i <= n :
            
            if big*2 == i:
                lst[i] = 1
                big = big*2
                
            else:
                lst[i] = lst[i - big] + lst[big]
                
            i+=1
            
        
        return lst
        
        