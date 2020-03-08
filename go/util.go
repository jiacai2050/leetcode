package leetcode

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

type testcase struct {
	input    interface{}
	expected interface{}
}

// https://stackoverflow.com/questions/54744850/type-func-with-interface-parameter-incompatible-error
// Some type systems and types support covariance and contravariance, but Go's interfaces do not.
func runTests(t *testing.T, tc []testcase, fn func(interface{}) interface{}) {
	for _, c := range tc {
		t.Run(fmt.Sprintf("%v", c.input), func(t *testing.T) {
			assert.Equal(t, c.expected, fn(c.input))
		})
	}
}
