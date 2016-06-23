# https://leetcode.com/problems/3sum/

# FIX: have duplicate triplets

class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        val_index_dict = {}
        for i, n in enumerate(nums):
            if n in val_index_dict:
                val_index_dict[n].append(i)
            else:
                val_index_dict[n] = [i]

        ret = []
        for x, target in enumerate(nums):
            for y, m in enumerate(nums):
                remaining = -target - m
                if remaining in val_index_dict.keys():
                    for z in val_index_dict.get(remaining):
                        if x < y < z:
                            ret.append([target, m, remaining])
                        else:
                            continue

        return ret


if __name__ == '__main__':
    s = Solution()
    print s.threeSum([-1, 0, 1, 2, -1, -4])
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
