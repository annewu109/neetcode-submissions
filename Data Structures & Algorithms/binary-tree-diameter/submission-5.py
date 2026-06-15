# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        if root == None:
            return 0

        def findDepth(root: Optional[TreeNode]) -> int:
            if root == None:
                return 0

            left = findDepth(root.left)
            right = findDepth(root.right)

            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1

        findDepth(root)

        return self.diameter