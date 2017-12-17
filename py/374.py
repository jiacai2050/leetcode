# https://leetcode.com/problems/guess-number-higher-or-lower/

# It seems guess function return opposite result as it says:
# return -1 if my number is lower, 1 if my number is higher, otherwise return 0

def guess(n):
    return 6 - n


class Solution(object):
                
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        x = guess(n)

        upper_num, lower_num = n, 1

        while lower_num <= upper_num:
            mid = (upper_num-lower_num)/2 + lower_num
            x = guess(mid)
            if x == 0:
                return mid
            elif x > 0:
                lower_num = mid + 1
            else:
                upper_num = mid


if __name__ == "__main__":
    s = Solution()
    assert s.guessNumber(10) == 6
