package recursion

func CountItems(slice []int) int {
	if len(slice) == 0 {
		return 0
	}
	return 1 + CountItems(slice[1:])
}
