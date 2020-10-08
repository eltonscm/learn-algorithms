package recursion

func Sum(slice []int) int {
	if len(slice) == 0 {
		return 0
	}
	if len(slice) == 1 {
		return slice[0]
	}
	return slice[0] + Sum(slice[1:])
}
