class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dic = {}
        dic[1] = [1]
    
        dic[2] = [1,1]
        lst1 = []
        for i in range(1,numRows+1):
            
            if i not in dic:
                lst = [1]
                for x in range(len(dic[i-1])-1):
                    lst.append(dic[i-1][x]+dic[i-1][x+1])
                lst.append(1)
                dic[i] = lst
            
            lst1.append(dic[i])
            
        return lst1
            