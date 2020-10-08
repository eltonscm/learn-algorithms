package sorting

import (
	"reflect"
	"testing"
)

func TestSelectionSort(t *testing.T) {
	assertCorrectMessage := func(t *testing.T, got, want []int) {
		t.Helper()
		if !reflect.DeepEqual(got, want) {
			t.Errorf("got %v, want %v, ", got, want)
		}
	}

	t.Run("sorting unsorted list", func(t *testing.T) {
		got := SelectionSort([]int{2, 3, 1, 5, 6, 4})
		want := []int{1, 2, 3, 4, 5, 6}
		assertCorrectMessage(t, got, want)
	})

	t.Run("sorting already sorted list", func(t *testing.T) {
		got := SelectionSort([]int{1, 2, 3})
		want := []int{1, 2, 3}
		assertCorrectMessage(t, got, want)
	})

	t.Run("sorting empty list", func(t *testing.T) {
		got := SelectionSort([]int{})
		want := []int{}
		assertCorrectMessage(t, got, want)
	})
}
