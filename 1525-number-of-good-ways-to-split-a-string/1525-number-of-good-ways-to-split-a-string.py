class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) == 1:
            return 0
        
        s1 = s[0:1]
        s2 = s[1:]
        
        
        l1 = 1
        
        track = set()
        
        for i in s2:
            track.add(i)
            
        l2 =len(track)
        
        ans = 0
        if l2==l1:
            ans +=1
        
        
        while len(s2)>0:
            ele = s2[0]
            s2 = s2[1:]
            if ele not in s2:
                l2-=1 
            if ele not in s1:
                l1+=1
            s1=s1+ele
            
            if l2 == l1:
                ans+=1 
                
        return ans
                
            