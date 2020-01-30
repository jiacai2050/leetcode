# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution(object):
    def hasRepeatChar(self, s):
        return len(set(s)) < len(s)

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_max_length = 0
        s_len = len(s)
        for i, char in enumerate(s):
            least_j = current_max_length + i + 1
            if least_j <= s_len:
                acc = s[i:least_j]
                if self.hasRepeatChar(acc):
                    continue
                else:
                    for j in xrange(least_j, s_len):
                        if s[j] in acc:
                            break
                        else:
                            acc += s[j]

                current_max_length = len(acc)

            else:
                break

        return current_max_length


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLongestSubstring('') == 0
    assert s.lengthOfLongestSubstring('b') == 1
    assert s.lengthOfLongestSubstring('ab') == 2
    assert s.lengthOfLongestSubstring('bbbbb') == 1
    assert s.lengthOfLongestSubstring('abcabcbb') == 3
    assert s.lengthOfLongestSubstring('pwwkew') == 3
    assert s.lengthOfLongestSubstring("wslznzfxojzd") == 6
