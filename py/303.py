# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if len(nums) == 0:
            self.sums = [0]
        else:
            self.sums = [nums[0]]
            for n in nums[1:]:
                self.sums.append(self.sums[-1] + n)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i-1]

if __name__ == '__main__':
    s = NumArray([-2, 0, 3, -5, 2, -1])
    assert s.sumRange(0, 2) == 1
    assert s.sumRange(2, 5) == -1
    assert s.sumRange(0, 5) == -3
