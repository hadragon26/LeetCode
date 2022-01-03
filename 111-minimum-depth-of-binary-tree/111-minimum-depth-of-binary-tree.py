# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        from collections import deque as queue
        
        if not root:
            return 0
        q = queue()
        q.append([root])
        l = 0
        
        while q:
            node = q.popleft()
            temp = []
            
            for i in node:
                if not i.right and not i.left:
                    return l+1
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            q.append(temp)
            l +=1
        
                
        
        
        
        
        