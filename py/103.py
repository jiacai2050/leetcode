# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []

        l = len(nums)
        i = 0

        nums.sort()
        while i < l - 2:

            j = i + 1
            k = l - 1
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    a = [nums[i], nums[j], nums[k]]
                    ret.append(a)
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
            i += 1

        return ret


if __name__ == '__main__':
    s = Solution()
    # we got [[-1, -1, 2], [-1, 0, 1]], but accepted.
    # ret = s.threeSum([-1, 0, 1, 2, -1, -4])
    # assert ret == [[-1, 0, 1], [-1, -1, 2]], ret

    ret = s.threeSum([0, 0, 0, 0])
    assert ret == [[0, 0, 0]], ret

    ret = s.threeSum([-2, 0, 1, 1, 2])
    assert ret == [[-2, 0, 2], [-2, 1, 1]], ret

    print("done")
