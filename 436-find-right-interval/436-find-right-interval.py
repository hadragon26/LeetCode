class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        start_list1 = []
        end_list = []
        dic ={}
        ans= []
        for index,ele in enumerate(intervals):
            end_list.append(ele[1])
            heapq.heappush(start_list1,ele[0])
            dic[ele[0]] = index
        start_list = []
        while start_list1:
            start_list.append(heappop(start_list1))
        print(start_list)
        print(end_list)
        print(dic)
                  
        def searh(ele):
            left = 0 
            right = len(start_list)-1
            
            while right>= left:
                mid = (right + left)//2
                
                if start_list[mid] == ele:
                    return dic[start_list[mid]]
                elif ele > start_list[mid]:
                    left = mid+1
                elif ele < start_list[mid]:
                    right = mid-1
            return dic[start_list[left]]
        
        for i in end_list:
            if i < start_list[0]:
                ans.append(mid[start_list[0]])
            elif i>start_list[-1]:
                ans.append(-1)
            else:
                ans.append(searh(i))
                
        return ans
                
        
            
    
        