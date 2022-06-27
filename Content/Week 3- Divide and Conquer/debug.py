def merge(array, p, q, r):
    nLeft = q - p + 1
    nRight = r - q
    leftarray = [0] * nLeft
    rightarray = [0] * nRight

    for i in range(0, nLeft):
        leftarray[i] = array[p + i]

    for j in range(0, nRight):
        rightarray[j] = array[q + 1 + j]

    # print(leftarray)
    # print(rightarray)

    left = 0
    right = 0
    dest = p

    while left < nLeft and right < nRight:
        if leftarray[left] < rightarray[right]:
            array[dest] = leftarray[left]
            left += 1
        else:
            array[dest] = rightarray[right]
            right = right + 1
        dest += 1

    while left < nLeft:
        array[dest] = leftarray[left]
        left += 1
        dest += 1
    while right < nRight:
        array[dest] = rightarray[right]
        right += 1
        dest += 1


def mergesort_recursive(array, p, r):
    if p < r:
        q = (p + r) // 2
        mergesort_recursive(array, p, q)
        mergesort_recursive(array, q + 1, r)
        merge(array, p, q, r)


def mergesort(array):
    return mergesort_recursive(array, 0, len(array) - 1)


input_array = [5, 2, 4, 7, 1, 3, 2, 6]
mergesort(input_array)
print(input_array)