# https://leetcode.com/problems/nim-game/

# Tips:
# The one who are left with 4 stones are doomed to failed,

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if m == n % 4:
            return False
        else:
            return True

if __name__ == '__main__':
    s = Solution()
    assert s.canWinNim(4) == False
    assert s.canWinNim(5) == True
