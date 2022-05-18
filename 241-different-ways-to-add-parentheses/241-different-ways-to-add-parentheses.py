class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        
        dic = {}
        
        
        def helper(s):
            
            if s in dic:
                return dic[s]
            
            if s.isdigit():
                dic[s] = [int(s)]
                return dic[s]
            
            
            tmp = []
            for i in range(len(s)):
                if s[i] in ['-','+','*']:
                    
                    left = helper(s[:i])
                    right = helper(s[i+1:])
                    
                    
                    
                    for l in left:
                        for r in right:
                            if s[i] == '-':
                                tmp.append(l-r)
                            elif s[i] == '+':
                                tmp.append(l+r)
                            elif s[i] == '*':
                                tmp.append(l*r)
                                
                                
            dic[s] = tmp
            
            return tmp
        
        return helper(expression)
                                
                                
                    
                                
            