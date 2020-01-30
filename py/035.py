# https://leetcode.com/problems/search-insert-position/


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = int((low + high) / 2)
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
        return low


if __name__ == '__main__':
    s = Solution()
    assert s.searchInsert([1], 0) == 0
    assert s.searchInsert([1, 3, 5, 6, 9], 8) == 4
    assert s.searchInsert([1, 3, 5], 4) == 2
