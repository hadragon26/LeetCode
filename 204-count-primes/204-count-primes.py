class Solution:
    def countPrimes(self, n: int) -> int:
        
        
        prime = [True for i in range(n+1)]
        
        i =2
        while i*i<=n:
            if prime[i]:
                for p in range(i*i,n+1,i):
                    prime[p]=False
                    
            i+=1
                    
        
        su = 0
        
        for i in range(2,n):
            if prime[i]:
                su+=1 
                
        return su
        
        
        