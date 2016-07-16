# https://leetcode.com/problems/bulb-switcher/

import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bulbs = [True] * n
        # for i in xrange(2, n+1):
        #     times = 1
        #     j = i * times
        #     while j <= n:
        #         bulbs[j-1] = False if bulbs[j-1] else True
        #         times += 1
        #         j = i * times
        # return len([i for i in bulbs if i == True])
        

        # https://discuss.leetcode.com/topic/39558/share-my-o-1-solution-with-explanation
        return int(math.sqrt(n))

if __name__ == '__main__':
    s = Solution()
    assert s.bulbSwitch(3) == 1
    assert s.bulbSwitch(4) == 2
    assert s.bulbSwitch(999999) == 999
