class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        if k>len(s):
            return 0
        if k == 0 or k ==1:
            return len(s)
        
        n = len(s)
        
        
        
        def get(l,r):
            if k>r-l or l==r:
                return 0
            if k == 0 or k ==1:
                return len(s)
            
            
            
            dic = {}
            for i in range(l,r):
                if s[i] in dic:
                    dic[s[i]]+=1
                else:
                    dic[s[i]] =1 
            
            x= l;        
            while l<r and dic[s[l]] >= k:
                l+=1 
            if l==r:
                return r-x
            
            #print('s1')
            #print(dic)
            #print(x)
            #print(l)
            s1 = get(x,l)
            l+=1
            
            while l<r and dic[s[l]]<k:
                l+=1
                
            #print('s2')
            #print(l)
            
            print(r)
            
            if l == r:
                s2 = 0
            else:
                s2 = get(l,n)
            
            
            return max(s1,s2)
        
        
        return get(0,n)
                
            
            
            
        
        
        
        
        
        
        

