# https://leetcode.com/problems/3sum-closest/

# FIX: TLE
import sys

class Solution(object):
    def iter(self, nums, remaining, target):
        if len(nums) < 1:
            return sys.maxint
        if remaining == 0:
            if abs(self.close) > abs(target):
                return target
            else:
                return sys.maxint

        r1 = self.iter(nums[1:], remaining, target)
        r2 = self.iter(nums[1:], remaining-1, target-nums[0])

        if abs(r1) < abs(r2):
            return r1
        else:
            return r2

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.close = sys.maxint
        return target - self.iter(nums, 3, target)

if __name__ == '__main__':
    s = Solution()
    assert s.threeSumClosest([-1, 2, 1, 4], 1) == 2
    arr = [-11,-2,17,-16,1,-5,-5,-5,-20,7,10,-2,3,-7,-17,-13,-19,-15,-8,-7,6,-6,-8,-4,12,-12,9,-17,-13,4,-5,-15,-9,-18,-17,1,-15,-8,14,8,20,-3,-11,17,-18,10,-16,5,-9,-18,2,-3,4,-18,2,20,0,-6,18,-12,0,-17,3,-19,-20,15,12,-17,-7,8,16,7,-5,5,-13,16,-18,-7,-9,-8,-17,6,-18,0,-15,10,-13,7,9,20,7,-13,3,0,0,19,8,0,-5,-9,6,8,16,14,3,-4,5,9,-12,-19,16,6]
    assert s.threeSumClosest(arr, -48) == -48
