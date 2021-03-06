# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.pointer = 0 
        self.lst = []
        
        def inorder(root):
            
            if not root:
                return 
            inorder(root.left)
            self.lst.append(root.val)
            
            
            inorder(root.right)
            
        inorder(root)
        
        self.length = len(self.lst)
        
        

    def next(self) -> int:
        
        self.pointer +=1 
        
        return self.lst[self.pointer-1]
        
        
        

    def hasNext(self) -> bool:
        if self.pointer <self.length:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()