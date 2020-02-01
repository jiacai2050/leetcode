// https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

package leetcode

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func lengthOfLongestSubstring(s string) int {

	ret := 0
	length := len(s)
	i, j := 0, 0
	substr := map[byte]int{}
	for ; j < length; j++ {
		if idx, ok := substr[s[j]]; ok {
			if idx > i {
				i = idx
			}
		}
		substr[s[j]] = j + 1
		if current := j - i + 1; current > ret {
			ret = current
		}

	}
	return ret
}

func TestLengthOfLongestSubstring(t *testing.T) {
	cases := []struct {
		input    string
		expected int
	}{
		{
			input:    "abba",
			expected: 2,
		},
		{
			input:    "pwwkew",
			expected: 3,
		},
		{
			input:    "tmmzuxt",
			expected: 5,
		},
	}

	for _, c := range cases {
		t.Run(c.input, func(t *testing.T) {
			assert.Equal(t, c.expected, lengthOfLongestSubstring(c.input))
		})
	}
}
