# coding: utf-8
# https://leetcode.com/problems/longest-palindromic-substring/

# 解题思路：
# 从中间开始判断，逐渐逼向两端；当前位置的回文串达到理论上的最大长度时，直接返回
# 每一个位置，有三种遍历方式：
# 1. 前后同时移动一个字符，当前位置作为中心
# 2. 当前位置作为回文串后端，前端向前移动一个字符，然后再同时移动前后两端
# 3. 当前位置作为回文串前端，后端向后移动一个字符，然后再同时移动前后两端


class Solution(object):
    def currentWalk(self, current, inc_func, dec_func):
        offset = 1
        current_max = 1
        while True:
            high = inc_func(current, offset)
            low = dec_func(current, offset)
            if low < 0 or high > self.len_s - 1:
                break
            if self.s[low] == self.s[high]:
                if low != current and high != current:
                    current_max += 2
                else:
                    current_max += 1
                offset += 1
                if current_max > self.num_max:
                    self.num_max = current_max
                    self.target_s = self.s[low:high + 1]
            else:
                break

    def currentLongestPalindrome(self, current):
        self.currentWalk(current, lambda current, offset: current + offset,
                         lambda current, offset: current - offset)
        self.currentWalk(current, lambda current, offset: current + offset - 1,
                         lambda current, offset: current - offset)
        self.currentWalk(current, lambda current, offset: current + offset,
                         lambda current, offset: current - offset + 1)

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        if len_s <= 1:
            return s

        self.s = s
        self.len_s = len_s
        self.num_max = 0
        self.target_s = ""
        index = mid = int(len_s / 2)
        offset = 1
        while True:
            right_index = index + offset - 1
            if right_index < len_s:
                self.currentLongestPalindrome(right_index)
                if len(self.target_s) > (len_s - right_index) * 2:
                    return self.target_s

            left_index = index - offset
            if left_index > -1:
                self.currentLongestPalindrome(left_index)
                if len(self.target_s) > (left_index) * 2:
                    return self.target_s
            else:
                return self.target_s

            offset += 1


if __name__ == '__main__':
    s = Solution()
    assert s.longestPalindrome("abacc") == "aba"
    assert s.longestPalindrome("abacccc") == "cccc"
    assert s.longestPalindrome("a") == "a"
    assert s.longestPalindrome("aa") == "aa"
    assert s.longestPalindrome("aaa") == "aaa"
    assert s.longestPalindrome("aaaa") == "aaaa"
    test_s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
    assert s.longestPalindrome(test_s) == test_s
