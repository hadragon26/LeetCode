# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        
        heap = []
        
        
        for lst in lists:
            
            while lst:
                
                heappush(heap,lst.val)
                lst = lst.next
                
        dummy = ListNode(0)
        
        curr = dummy
        
        while heap:
            curr.next= ListNode(heappop(heap))
            curr = curr.next
            
        return dummy.next
            
            