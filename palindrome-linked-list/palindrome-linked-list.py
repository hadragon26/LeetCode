# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        from collections import deque
        
        q = deque()
        
        dummy = head 
        
        while dummy.next:
            q.append(dummy.val)
            dummy = dummy.next
        
        x = dummy.val
        length = len(q)
        
        while q and x == q[0]:
            q.popleft()
            if q:
                x = q.pop()
            
        
        return len(q) == 0
        
        
        