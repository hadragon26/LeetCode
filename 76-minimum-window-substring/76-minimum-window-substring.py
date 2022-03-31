class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        if len(t) > len(s):
            return ""
        left = 0 
        minleft = float('-inf')
        end  = len(t)
        dic1 = {}
        right = float('inf')
        
        
        for i in t:
            if i not in dic1:
                dic1[i] = 1
            else:
                dic1[i]+=1
                
        window = s[left:end]
        
        
        dic2 = {}
        
        for i in window:
            if i not in dic2:
                dic2[i] = 1
            else:
                dic2[i]+=1
                
        def same(dic):
            for i in dic1:
                if i not in dic:
                    return False
                elif i in dic:
                    if dic1[i] > dic[i]:
                        return False
                
            return True
        
        if same(dic2):
            return window
        
        
        
        while end<len(s):
            if not same(dic2):
                
                if s[end] in dic2:
                    dic2[s[end]]+=1
                else:
                    dic2[s[end]] = 1
                    
                end+=1
                
                #print(True)
    
                
                    
            else:
                #print(False)
                while same(dic2):
                    
                    if end-left< right - minleft:
                        minleft = left 
                        right = end
                    
                    dic2[s[left]]-=1
                    if dic2[s[left]] == 0:
                        del dic2[s[left]]
                    left +=1
                
                
        print(dic2) 
        while same(dic2):
                    
            if end-left< right - minleft:
                minleft = left 
                right = end

            dic2[s[left]]-=1
            if dic2[s[left]] == 0:
                del dic2[s[left]]
            left +=1
                    
        if right!= float('inf'):
            return s[minleft:right]
        return ''
                    
            
        
        
        
        