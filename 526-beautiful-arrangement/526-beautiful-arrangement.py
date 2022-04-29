class Solution:
    def countArrangement(self, n: int) -> int:
        
        self.count = 0 
        track = [False for i in range(n+1)]
        print(track)
        
        def calc(n,pos):
            if pos>n:
                self.count+=1
            for i in range(1,n+1):
                if not track[i] and (pos%i==0 or i%pos == 0):
                    track[i] = True
                    calc(n,pos+1)
                    track[i]=False
                    
        calc(n,1)
        
        
        return self.count
                    
            
                    
                    
        
            
            