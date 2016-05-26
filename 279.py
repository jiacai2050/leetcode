import math, sys

class Solution(object):
    def closePerfectSquares(self, n):
        return int(math.sqrt(n))

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        res = sys.maxint

        count = 0
        for i in xrange(self.closePerfectSquares(n), 0, -1):
            remaining = n
            for j in xrange(i, 0, -1):
                while remaining > 0:
                    remaining -= j*j
                    count += 1

                if remaining == 0:
                    if count < res:
                        res = count
                    count = 0
                    break
                else:
                    remaining += j*j
                    count -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    assert s.numSquares(13) == 2
    assert s.numSquares(12) == 3
    assert s.numSquares(100) == 1
    assert s.numSquares(43) == 3  # False now
