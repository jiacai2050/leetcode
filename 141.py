# https://leetcode.com/problems/linked-list-cycle/

# very classical exercise.
# Tips:
# set two points, one of which moves one step once and the other moves two steps
# If the list have circle, then the two points will meet at some time

 一个一次走两步，另一个一次走一步，如果如环，那么在某一时刻这两个指针会相遇
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        else:
            slow = fast = head
            while fast is not None:
                fast = fast.next
                if fast is None:
                    return False
                else:
                    fast = fast.next
                slow = slow.next

                if fast == slow:
                    return True

            return False

if __name__ == '__main__':
    s = Solution()
    head = ListNode(0)
    tail = head
    for i in xrange(1,5):
        new_node = ListNode(i)
        new_node.next = head
        head = new_node
    assert s.hasCycle(head) == False
    tail.next = head
    assert s.hasCycle(head) == True
    # debug
    # while head is not None:
    #     print head.val
    #     head = head.next
