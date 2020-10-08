package recursion

import (
	"testing"
)

func TestMax(t *testing.T) {
	assertCorrectMessage := func(t *testing.T, got, want int) {
		t.Helper()
		if got != want {
			t.Errorf("got %d, want %d, ", got, want)
		}
	}

	assertHasErrorMessage := func(t *testing.T, err error) {
		t.Helper()
		if err == nil {
			t.Errorf("expected an error, got nil")
		}
	}

	t.Run("get max in an empty list", func(t *testing.T) {
		_, err := Max([]int{})
		assertHasErrorMessage(t, err)
	})

	t.Run("get max in list with 1 item", func(t *testing.T) {
		got, _ := Max([]int{1})
		want := 1
		assertCorrectMessage(t, got, want)
	})

	t.Run("get max in list with 2 item", func(t *testing.T) {
		got, _ := Max([]int{1, 2})
		want := 2
		assertCorrectMessage(t, got, want)
	})

	t.Run("get max in list with multiple items", func(t *testing.T) {
		got, _ := Max([]int{1, 2, -1, 3, 4, 0})
		want := 4
		assertCorrectMessage(t, got, want)
	})
}
