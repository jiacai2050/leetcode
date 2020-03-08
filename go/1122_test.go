package leetcode

import (
	"fmt"
	"sort"
	"testing"

	"github.com/stretchr/testify/assert"
)

// https://leetcode.com/problems/relative-sort-array/

func relativeSortArray(arr1 []int, arr2 []int) []int {
	i := 0
	for _, e := range arr2 {
		for j := i; j < len(arr1); j++ {
			if arr1[j] == e {
				if i != j {
					tmp := arr1[i]
					arr1[i] = arr1[j]
					arr1[j] = tmp
				}
				i++
			}
		}
	}

	sort.Sort(sort.IntSlice(arr1[i:]))
	return arr1
}

func TestRelativeSortArray(t *testing.T) {
	cases := []struct {
		input    [][]int
		expected []int
	}{
		{
			input: [][]int{
				[]int{2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19},
				[]int{2, 1, 4, 3, 9, 6},
			},
			expected: []int{2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19},
		},
	}
	for _, c := range cases {
		t.Run(fmt.Sprintf("%v", c.input), func(t *testing.T) {
			assert.Equal(t, c.expected, relativeSortArray(c.input[0], c.input[1]))
		})
	}
}
