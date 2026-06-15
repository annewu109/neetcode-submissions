# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(a, b):
            if not a and not b:
                return True
            elif a and b and a.val == b.val:
                return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)
            else:
                return False
            
        if not subRoot:
            return True
        elif not root and subRoot:
            return False
        elif root and subRoot: 
            if root.val == subRoot.val and isSameTree(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        