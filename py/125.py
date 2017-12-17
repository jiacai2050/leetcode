# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isChar(self, c):
        return c.isalpha() or c.isdigit()

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        else:
            low = 0
            high = len(s) - 1
            while low < high:
                while self.isChar(s[low]) is False:
                    if low == high:
                        return True
                    else:
                        low += 1
                while self.isChar(s[high]) is False:
                    if low == high:
                        return True
                    else:
                        high -= 1

                if low < high:
                    if s[low].lower() != s[high].lower():
                        return False
                else:
                    return True

                low += 1
                high -= 1

            return True

if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") == True
    assert s.isPalindrome("race a car") == False
    assert s.isPalindrome("a:b:a") == True
    assert s.isPalindrome("a0") == True
