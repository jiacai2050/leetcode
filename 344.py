# https://leetcode.com/problems/reverse-string/


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = [i for i in s]
        low = 0
        high = len(s) - 1
        while low < high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
        return ''.join(arr)


if __name__ == '__main__':
    s = Solution()
    assert s.reverseString("hello") == "olleh"
