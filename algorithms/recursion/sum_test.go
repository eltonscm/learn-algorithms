package recursion

import (
	"testing"
)

func TestSum(t *testing.T) {
	assertCorrectMessage := func(t *testing.T, got, want int) {
		t.Helper()
		if got != want {
			t.Errorf("got %d, want %d, ", got, want)
		}
	}

	t.Run("sum an empty list", func(t *testing.T) {
		got := Sum([]int{})
		want := 0
		assertCorrectMessage(t, got, want)
	})

	t.Run("sum a list with one item", func(t *testing.T) {
		got := Sum([]int{42})
		want := 42
		assertCorrectMessage(t, got, want)
	})

	t.Run("sum a list with positive numbers", func(t *testing.T) {
		got := Sum([]int{2, 10, 30})
		want := 42
		assertCorrectMessage(t, got, want)
	})

	t.Run("sum a list with negative numbers", func(t *testing.T) {
		got := Sum([]int{-2, -10, -30})
		want := -42
		assertCorrectMessage(t, got, want)
	})

	t.Run("sum a list with negative and positive numbers", func(t *testing.T) {
		got := Sum([]int{-2, 2})
		want := 0
		assertCorrectMessage(t, got, want)
	})
}
