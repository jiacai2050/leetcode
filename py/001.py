# https://leetcode.com/problems/two-sum/

class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        val_index_dict = {}
        for i, n in enumerate(nums):
            remaining = target - n
            if remaining in val_index_dict.keys():
                list_j = val_index_dict.get(remaining)
                for j in list_j:
                    if j == i:
                        continue
                    else:
                        return [j, i]

            if n in val_index_dict.keys():
                val_index_dict[n].append(i)
            else:
                val_index_dict[n] = [i]


if __name__ == '__main__':
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([0, 4, 3, 0], 0) == [0, 3]
