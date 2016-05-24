# coding: utf-8
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# 解题思路：
# 同 349 题


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.repeated = 0


class Solution(object):
    def bst_insert(self, root, val):
        if root is None:
            root = TreeNode(val)
            return root

        if val == root.val:
            root.repeated += 1
            return root
        elif val > root.val:
            root.right = self.bst_insert(root.right, val)
        else:
            root.left = self.bst_insert(root.left, val)

        return root

    def bst_search(self, root, val):
        if root is None:
            return False

        if root.val == val:
            if root.repeated >= 0:
                root.repeated -= 1
                return True
            else:
                return False
        elif root.val > val:
            return self.bst_search(root.left, val)
        else:
            return self.bst_search(root.right, val)

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        root = None
        for i in nums1:
            root = self.bst_insert(root, i)

        return [j for j in nums2 if self.bst_search(root, j)]


if __name__ == '__main__':
    s = Solution()
    assert s.intersect([1, 2, 2, 1], [2, 2, 3]) == [2, 2]
    assert s.intersect([1, 2, 2, 1], [2, 3]) == [2]
    assert s.intersect([1], [1, 1]) == [1]
    assert s.intersect([1, 3], [2, 3]) == [3]
    assert s.intersect([1, 3], []) == []
    assert s.intersect([], []) == []
