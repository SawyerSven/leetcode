from typing import List


def quick(array: List[int], start: int, end: int) -> List[int]:
    if(end - start < 1):
        return
    target = array[start]
    l = start
    r = end
    while(l < r):
        while(l < r and array[r] >= target):
            r = r - 1
        array[l] = array[r]
        while(l < r and array[l] < target):
            l = l + 1
        array[r] = array[l]
    array[l] = target
    quick(array, start, l - 1)
    quick(array, l+1, end)
    return array


arr = [59, 43, 42, 31, 8, 48, 20, 79, 53, 53,
       94, 63, 29, 59, 27, 38, 10, 72, 64, 69]

print(quick(arr, 0, len(arr) - 1))
