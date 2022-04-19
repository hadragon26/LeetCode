class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        
        d = 1 
        
        
        lst = [n]
        lst1 = [0]
        
        while n-d>0 :
            
            lst.append(n-d)
            lst1.append(d)
            n = n-d
            d+=1
        
        total = len(lst)
        ma = total
        
        
        for i in range(1,total):
            
            
            ma = max(ma,total-1+lst1[i])
            
            total -=1 
            
        return(ma)
            