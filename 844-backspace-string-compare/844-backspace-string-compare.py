class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        ps, pt = len(s)-1, len(t)-1
        i, j = 0, 0
        
        while ps > -1 and pt > -1:
            if i==0 and j==0 and s[ps]!='#' and t[pt]!='#':
                if s[ps] != t[pt]:
                    return False
                ps -= 1
                pt -= 1
            
            while ps > -1 and (i or s[ps]=='#'):
                if s[ps] != '#':
                    i -= 1
                else:
                    i += 1
                ps -= 1
            
            while pt > -1 and (j or t[pt]=='#'):
                if t[pt] != '#':
                    j -= 1
                else:
                    j += 1
                pt -= 1
        
        return ps<0 and pt<0