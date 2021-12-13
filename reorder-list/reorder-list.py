# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        fast = slow = head 
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            
        nxt = None
        while slow:
            
            node = slow.next
            slow.next = nxt 
            nxt = slow
            slow = node
        
        dummy = head
        n =0
        while nxt and dummy:
            n+=1
            if n%2 ==1:
                x = dummy.next
                dummy.next = nxt
                dummy = dummy.next
                nxt = nxt.next
            else:
                dummy.next = x
                dummy = dummy.next
            
            
            
            
            
            
            
        
        
        