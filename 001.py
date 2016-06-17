# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            j = i + 1
            for m in nums[j:]:
                if n + m == target:
                    return [i, j]

                j += 1

if __name__ == '__main__':
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
