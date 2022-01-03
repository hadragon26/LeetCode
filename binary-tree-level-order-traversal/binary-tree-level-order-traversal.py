# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        from collections import deque as queue
        
        if not root:
            return []
        
        q= queue()
        
        q.append([root])
        ans= [[root.val]]
        while q:
            node_list = q.popleft()
            new =[]
            val = []
            
            for i in node_list:
                if i.left:
                    new.append(i.left)
                    val.append(i.left.val)
                if i.right:
                    new.append(i.right)
                    val.append(i.right.val)
            
            if new:
                q.append(new)
                ans.append(val)
        return ans
                
            
            
        
        
        
        
            
        
            
            
            