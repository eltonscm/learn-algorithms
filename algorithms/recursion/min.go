package recursion

import "errors"

func Min(slice []int) (int, error) {
	if len(slice) == 0 {
		return 0, errors.New("Can't find minimum in an empty list")
	}

	x := slice[0]
	y, err := Min(slice[1:])

	if err != nil || x < y {
		return x, nil
	}

	return y, nil
}
