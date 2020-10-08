package recursion

import "errors"

func Max(slice []int) (int, error) {
	if len(slice) == 0 {
		return 0, errors.New("Can't find maximum in an empty list")
	}

	x := slice[0]
	y, _ := Max(slice[1:])

	if x > y {
		return x, nil
	}

	return y, nil
}
