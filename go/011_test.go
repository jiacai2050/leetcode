package leetcode

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func maxArea(height []int) int {
	i, j := 0, len(height)-1
	max := (j - i) * minInt(height[i], height[j])
	for i < j {
		if height[j] > height[i] {
			i++
		} else {
			j--
		}

		if curr := (j - i) * minInt(height[i], height[j]); curr > max {
			max = curr
		}

	}

	return max
}

func TestMaxArea(t *testing.T) {

	testcases := []struct {
		input    []int
		expected int
	}{
		{
			input:    []int{1, 8, 6, 2, 5, 4, 8, 3, 7},
			expected: 49,
		},
		{
			input:    []int{1, 2, 4, 3},
			expected: 4,
		},
	}

	for _, tc := range testcases {
		t.Run(fmt.Sprintf("%v", tc.input), func(t *testing.T) {
			assert.Equal(t, tc.expected, maxArea(tc.input))
		})
	}
}
