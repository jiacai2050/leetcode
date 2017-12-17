# https://leetcode.com/problems/simplify-path/

class Stack(object):
    def __init__(self):
        self.elements = []

    def push(self, e):
        self.elements.append(e)

    def pop(self):
        if self.size() > 0:
            return self.elements.pop()

    def seek(self):
        return self.elements[-1]

    def size(self):
        return len(self.elements)

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = Stack()
        for e in path.split("/"):
            if e == '.' or e == '':
                continue
            elif e == '..':
                stack.pop()
            else:
                stack.push(e)

        return '/' + '/'.join(stack.elements)


if __name__ == '__main__':
    s = Solution()
    assert s.simplifyPath("/a/./b/../../c/") == "/c"
    assert s.simplifyPath("/home/") == "/home"
    assert s.simplifyPath("//") == "/"
    assert s.simplifyPath("/") == "/"
    assert s.simplifyPath("/home//bar") == "/home/bar"
    assert s.simplifyPath("/../") == "/"
