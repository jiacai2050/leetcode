# coding: utf-8
# https://leetcode.com/problems/perfect-squares/

# 思路：
# 采用动态规划的思想，将原问题分拆为两个子问题
# iter 函数中的前两个判断当前子问题是否有可能成为最优解

# TODO: 降低时间复杂度，改成循环方式

import math

class Solution(object):

    def closePerfectSquares(self, n):
        return int(math.sqrt(n))

    def iter(self, current, max_close_perfact, count):
        if count >= self.best_count or max_close_perfact<1 or current < 0:
            return self.target
        if current - max_close_perfact*max_close_perfact*(self.best_count-count) > 0:
            return self.target
        if current == 0:
            self.best_count = count
            return count
        else:
            return min(self.iter(current-max_close_perfact*max_close_perfact, max_close_perfact, count+1),
                       self.iter(current, max_close_perfact-1, count))

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        else:
            self.target = n
            self.best_count = n
            return self.iter(n, self.closePerfectSquares(n), 0)


if __name__ == '__main__':
    s = Solution()
    assert s.numSquares(13) == 2
    assert s.numSquares(12) == 3
    assert s.numSquares(100) == 1
    assert s.numSquares(43) == 3
    assert s.numSquares(1) == 1
    assert s.numSquares(137) == 2
    assert s.numSquares(7168) == 4
    assert s.numSquares(19) == 3
    assert s.numSquares(9975) == 4
