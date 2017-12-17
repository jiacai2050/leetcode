# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels += [i.upper() for i in vowels]
        s = [i for i in s]
        low = 0
        high = len(s) - 1
        while low < high:
            while s[low] not in vowels and low < high:
                low += 1
            while s[high] not in vowels and low < high:
                high -= 1

            if low < high:
                s[low], s[high] = s[high], s[low]
                low += 1
                high -= 1
            else:
                break

        return ''.join(s)

if __name__ == '__main__':
    s = Solution()
    assert s.reverseVowels("leetcode") == "leotcede"
    assert s.reverseVowels("hello") == "holle"
    assert s.reverseVowels("") == ""
    assert s.reverseVowels("abc") == "abc"
    assert s.reverseVowels("aA") == "Aa"
