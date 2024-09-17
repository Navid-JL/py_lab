def binary_search(seq: list, key: int):
    low = 0
    high = len(seq) - 1

    while low <= high:
        mid = (high + low) // 2

        if key == seq[mid]:
            return mid
        elif key > seq[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def linear_search(seq: list, key: int):
    for i in range(len(seq)):
        if seq[i] == key:
            return i
    return -1
