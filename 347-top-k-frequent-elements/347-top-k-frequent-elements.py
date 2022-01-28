class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
                
        lst = sorted(dic.items(),key = lambda item:-item[1])[:k]
        
        ans = []
        
        for i in lst:
            ans.append(i[0])
        
        return ans
        
        