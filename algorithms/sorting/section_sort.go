package sorting

func SelectionSort(arr []int) []int {
	newArr := []int{}
	aux := append([]int(nil), arr...)

	for i := 0; i < len(arr); i++ {
		smallestIndex := FindSmallestIndex(aux)
		newArr = append(newArr, aux[smallestIndex])
		aux = RemoveFromIndex(aux, smallestIndex)
	}

	return newArr
}

func FindSmallestIndex(arr []int) int {
	smallest := arr[0]
	smallestIndex := 0

	for i := 1; i < len(arr); i++ {
		if arr[i] < smallest {
			smallest = arr[i]
			smallestIndex = i
		}
	}

	return smallestIndex
}

func RemoveFromIndex(arr []int, i int) []int {
	return append(arr[:i], arr[i+1:]...)
}
