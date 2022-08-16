# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        t = dummy 
        track = 0
        length = 0
        
        while head:
            head = head.next
            length +=1
        
        while t:
            if track == length-n:
                t.next= t.next.next
                break
            #print(t)
            t =t.next
            track +=1
            
        
        return dummy.next
            
            
            
        
        
        