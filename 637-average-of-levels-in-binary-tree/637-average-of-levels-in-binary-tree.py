# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        from collections import deque as que
        
        if not root:
            return []
        
        q = que()
        q.append([root])
        ans = [root.val]
        
        while q:
            node = q.popleft()
            node_list = []
            val = []
            
            for i in node:
                if i.left:
                    node_list.append(i.left)
                    val.append(i.left.val)
                if i.right:
                    node_list.append(i.right)
                    val.append(i.right.val)
                    
            if val:
                q.append(node_list)
                ans.append(sum(val)/len(val))
                
        return ans