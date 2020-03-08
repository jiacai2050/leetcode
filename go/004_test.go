// https://leetcode.com/problems/median-of-two-sorted-arrays/

package leetcode

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	nums3 := make([]int, 0, len(nums1)+len(nums2))

	i, j := 0, 0
	for i < len(nums1) && j < len(nums2) {
		if nums1[i] < nums2[j] {
			nums3 = append(nums3, nums1[i])
			i += 1
		} else {
			nums3 = append(nums3, nums2[j])
			j += 1
		}
	}
	for ; i < len(nums1); i++ {
		nums3 = append(nums3, nums1[i])
	}
	for ; j < len(nums2); j++ {
		nums3 = append(nums3, nums2[j])
	}
	length := len(nums3)
	if length%2 == 0 {
		mid := length / 2
		return float64(nums3[mid]+nums3[mid-1]) / 2
	}

	return float64(nums3[length/2])
}

const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

func findMedianSortedArrays2(nums1 []int, nums2 []int) float64 {
	maxInt := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	minInt := func(x, y int) int {
		if x > y {
			return y
		}
		return x
	}

	n := len(nums1)
	m := len(nums2)
	if n > m {
		return findMedianSortedArrays2(nums2, nums1)
	}
	odd := (m+n)%2 == 1
	half := int((n + m + 1) / 2)
	min, max := 0, n
	for min <= max {
		parX := int((min + max) / 2)
		parY := half - parX

		maxLeftX := MinInt
		if parX > 0 {
			maxLeftX = nums1[parX-1]
		}
		minRightX := MaxInt
		if parX < n {
			minRightX = nums1[parX]
		}
		maxLeftY := MinInt
		if parY > 0 {
			maxLeftY = nums2[parY-1]
		}
		minRightY := MaxInt
		if parY < m {
			minRightY = nums2[parY]
		}

		if maxLeftX <= minRightY && maxLeftY <= minRightX {
			if odd {
				return float64(maxInt(maxLeftX, maxLeftY))
			}
			return float64(maxInt(maxLeftX, maxLeftY)+minInt(minRightX, minRightY)) / 2
		} else if maxLeftX < minRightY {
			min = parX + 1
		} else {
			max = parX - 1
		}

	}
	return 0
}

func TestFindMedianSortedArrays(t *testing.T) {
	cases := []struct {
		input    [][]int
		expected float64
	}{
		{
			input: [][]int{
				[]int{1, 3},
				[]int{2, 4},
			},
			expected: 2.5,
		},
		{
			input: [][]int{
				[]int{1},
				[]int{1},
			},
			expected: 1.0,
		},
	}
	for _, c := range cases {
		t.Run(fmt.Sprintf("%v", c.input), func(t *testing.T) {
			assert.Equal(t, c.expected, findMedianSortedArrays(c.input[0], c.input[1]))
			assert.Equal(t, c.expected, findMedianSortedArrays2(c.input[0], c.input[1]))
		})
	}
}
