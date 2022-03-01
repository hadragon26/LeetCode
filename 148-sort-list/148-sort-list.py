# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        q = []
        if not head:
            return
        
        
        while head:
            heappush(q,head.val)
            head= head.next
            
            
        head = ListNode(heappop(q))
        curr =head
        
        while q:
            curr.next =  ListNode(heappop(q))
            curr =curr.next
            
            
        return head
        
            
            
            
            
            
            
            
            
            
            
            
            
            