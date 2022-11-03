class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        
        
        compliment = {}
        
        
        
        count = {}
        dup = {}
        track = set()
        
        su = 0
        for word in words:
            
            if word not in count:
                count[word]= 0 
                
            count[word]+=1 
            
            comp = word[::-1]
            if comp != word:
                
            
                if word not in track:
                    compliment[word] = comp
                    
                track.add(word)
                track.add(comp)
            else:
                dup[word] = count[word]
                su = max(su,count[word])
                
                
        ans = 0       
        for comp in compliment:
            if compliment[comp] in count:
                ans += 4*min(count[comp],count[compliment[comp]])
            
        for key,val in dup.items():
            if val >=2:
                if val %2 == 0:
                    ans+= 2*val
                    dup[key] = 0
                else:
                    ans+=2*(val-1)
                    dup[key] = 1
                    
        for key,val in dup.items():
            if val == 1:
                ans+= 2
                break
                
        return ans
                    
                    
                