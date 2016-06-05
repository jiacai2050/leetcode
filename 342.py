# https://leetcode.com/problems/power-of-four/

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and \
               not num & (num - 1) and \
               len(bin(num)[2:]) & 1

if __name__ == '__main__':
    s = Solution()
    assert s.isPowerOfFour(16) == True
    assert s.isPowerOfFour(4*4*4*4*4) == True
    assert s.isPowerOfFour(4*4*4*4*4+4) == False
