package recursion

import (
	"testing"
)

func TestCountItems(t *testing.T) {
	assertCorrectMessage := func(t *testing.T, got, want int) {
		t.Helper()
		if got != want {
			t.Errorf("got %d, want %d, ", got, want)
		}
	}

	t.Run("count items in an empty list", func(t *testing.T) {
		got := CountItems([]int{})
		want := 0
		assertCorrectMessage(t, got, want)
	})

	t.Run("count items in an list with 1 item", func(t *testing.T) {
		got := CountItems([]int{1})
		want := 1
		assertCorrectMessage(t, got, want)
	})

	t.Run("count items in a list with 5 items", func(t *testing.T) {
		got := CountItems([]int{1, 2, 3, 4, 5})
		want := 5
		assertCorrectMessage(t, got, want)
	})
}
