# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        else:
            right = self.invertTree(root.left)
            left = self.invertTree(root.right)
            root.right = right
            root.left = left
            return root

if __name__ == '__main__':
    pass
