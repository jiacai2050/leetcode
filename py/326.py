# https://leetcode.com/problems/power-of-three/
# https://leetcode.com/articles/power-of-three/

import sys
import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n > 0 and \
               pow(3,int(math.log(sys.maxint,3)))%n == 0)

if __name__ == '__main__':
    s = Solution()
    s.isPowerOfThree(pow(3, 34)) == True
