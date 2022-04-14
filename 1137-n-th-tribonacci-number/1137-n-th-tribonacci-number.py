class Solution:
    def tribonacci(self, n: int) -> int:
        
        
        if n ==0:
            return 0
        if n ==1 :
            return 1 
        if n ==2 :
            return 1 
        lst = [0 for i in range(n+1)]
        lst[0],lst[1],lst[2] = 0,1,1
        
        r = 3
        
        while r <=n:
            lst[r] = lst[r-3]+lst[r-2]+lst[r-1]
            r+=1
        return lst[-1]
        