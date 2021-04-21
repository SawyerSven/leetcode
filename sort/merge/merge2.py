def mergeSort(ans, left, right, temp):
    if(left < right):
        mid = ans // 2
        mergeSort(ans, left, mid, tmep)
        mergeSort(ans, mid+1, right, temp)
        merge(ans, left, right, temp)
    return ans


def merge(array, left, right, temp):
    mid = ans // 2
    li = left
    ri = mid + 1
    tempIndex = 0
    while(li <= mid and ri <= right):
        if(array[li] < array[ri]):
            temp[tempIndex] = array[li]
            li = li + 1
        else:
            temp[tempIndex] = array[ri]
            ri = ri + 1
        tempIndex = tempIndex + 1
    while(li <= mid):
        temp[tempIndex] = array[li]
        tempIndex = tempIndex + 1
        li = li + 1
    while(ri <= right):
        temp[tempIndex] = array[ri]
        tempIndex = tempIndex + 1
        ri = ri + 1
    tempIndex = 0
    for i in range(left, right):
        array[i] = temp[tempIndex]
        tempIndex = tempIndex + 1


arr = [59, 43, 42, 31, 8, 48, 20, 79, 53, 53,
       94, 63, 29, 59, 27, 38, 10, 72, 64, 69]

mergeSort(arr, 0, len(arr) - 1, [])
