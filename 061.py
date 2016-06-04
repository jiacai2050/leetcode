# coding=utf-8
# https://leetcode.com/problems/rotate-list/

# 解题思路：
# 首先，因为ListNode为单向链表，所以把右转移转为左转移，便于遍历
# 然后用两个指针（一前一后）去遍历链表，找到左转移后的新 head 与 tail

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head

        p = head
        size = 1
        while p.next is not None:
            size += 1
            p = p.next

        if size == 1:
            return head

        tail = p
        left_rotate_num = size - k % size

        if left_rotate_num == 0:
            return head
        else:
            front = head
            behind = None
            while left_rotate_num > 0:
                front = front.next
                if behind is None:
                    behind = head
                else:
                    behind = behind.next
                left_rotate_num -= 1

            if front is None:
                return head
            else:
                tail.next = head
                behind.next = None
                head = front
                return head

    def getListVal(self, head):
        ret = []
        while head is not None:
            ret.append(head.val)
            head = head.next
        return ret

if __name__ == '__main__':
    s = Solution()
    head = None
    for i in xrange(5,0,-1):
        new_node = ListNode(i)
        new_node.next = head
        head = new_node

    assert s.getListVal(s.rotateRight(head, 2)) == [4,5,1,2,3]

    head = None
    for i in xrange(5,3,-1):
        new_node = ListNode(i)
        new_node.next = head
        head = new_node

    assert s.getListVal(s.rotateRight(head, 1)) == [5,4]

    head = None
    for i in xrange(5,3,-1):
        new_node = ListNode(i)
        new_node.next = head
        head = new_node
    assert s.getListVal(s.rotateRight(head, 0)) == [4,5]

    head = None
    for i in xrange(5,4,-1):
        new_node = ListNode(i)
        new_node.next = head
        head = new_node

    assert s.getListVal(s.rotateRight(head, 1)) == [5]
