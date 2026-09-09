# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    m=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def hei(r):
            if not r:
                return 0
            l=hei(r.left)
            ri=hei(r.right)
            self.m=max(self.m,l+ri)
            return max(l,ri)+1
        hei(root)
        return self.m