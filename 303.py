# https://leetcode.com/problems/range-sum-query-immutable/

# FIX: Time Limit Exceeded

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = []
        len_nums = len(nums)
        for i, n in enumerate(nums):
            row = [0] * i
            row.append(n)
            j = i + 1
            while j < len_nums:
                row.append(row[j-1] + nums[j])
                j += 1
            self.sums.append(row)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[i][j]


if __name__ == '__main__':
    s = NumArray([-2, 0, 3, -5, 2, -1])
    assert s.sumRange(0, 2) == 1
    assert s.sumRange(2, 5) == -1
    assert s.sumRange(0, 5) == -3

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
