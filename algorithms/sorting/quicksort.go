package sorting

func Quicksort(slice []int) []int {
	size := len(slice)

	if size < 2 {
		return slice
	}

	pivot := slice[size / 2]

	left := Filter(slice, func(item int) bool { return item < pivot})
	middle := Filter(slice, func(item int) bool { return item == pivot})
	right := Filter(slice, func(item int) bool { return item > pivot})

	return append(
		append(Quicksort(left), middle...),
		Quicksort(right)...
	)
}

func Filter(slice []int, cond func(int) bool) []int {
	result := []int{}
	for _, item := range slice {
		if cond(item) {
			result = append(result, item)
		}
	}
	return result
}
