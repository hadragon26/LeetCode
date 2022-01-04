# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return 
        q = deque()
        q.append(root)
        
        tail = root 
        ans = [root.val]
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if node == tail:
                if len(q)>0:
                    tail = q[-1]
                    ans.append(tail.val)
        return ans
            
