# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return
        dummy = ListNode(0,head)
        
        #find length:
        length = 0
        dic = {}
        while head:
            dic[length] = head 
            length += 1
            
            last = head
            head = head.next
            
            
        number = k%length
        first = dummy.next 
        
        if number == 0:
            return dummy.next
        new_first = dic[length - number]
        
        latter =dic[length-number-1]
        print(new_first)
        dummy.next = new_first
        last.next = first
        latter.next = None 
        return dummy.next
        
        