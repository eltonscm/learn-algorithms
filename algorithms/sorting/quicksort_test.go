package sorting

import (
	"reflect"
	"testing"
)

func TestQuicksort(t *testing.T) {
	assertCorrectMessage := func(t *testing.T, got, want []int) {
		t.Helper()
		if !reflect.DeepEqual(got, want) {
			t.Errorf("got %v, want %v, ", got, want)
		}
	}

	t.Run("sorting unsorted list", func(t *testing.T) {
		got := Quicksort([]int{2, 3, 1, 5, 6, 4})
		want := []int{1, 2, 3, 4, 5, 6}
		assertCorrectMessage(t, got, want)
	})

	t.Run("sorting unsorted list with negative numbers", func(t *testing.T) {
		got := Quicksort([]int{2, 3, 1, -1, 5, -2, 4, 0})
		want := []int{-2, -1, 0, 1, 2, 3, 4, 5}
		assertCorrectMessage(t, got, want)
	})

	t.Run("sorting already sorted list", func(t *testing.T) {
		got := Quicksort([]int{1, 2, 3})
		want := []int{1, 2, 3}
		assertCorrectMessage(t, got, want)
	})

	t.Run("sorting empty list", func(t *testing.T) {
		got := Quicksort([]int{})
		want := []int{}
		assertCorrectMessage(t, got, want)
	})
}
