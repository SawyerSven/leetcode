def merge(front, end):
    temp = []
    while(len(front) and len(end)):
        if(front[0] < end[0]):
            temp.append(front.pop(0))
        else:
            temp.append(end.pop(0))
    if(len(front)):
        temp.extend(front)
    if(len(end)):
        temp.extend(end)
    return temp


def mergeSort(arr):
    if(len(arr) < 2):
        return arr
    mid = len(arr) // 2
    start = arr[:mid]
    end = arr[mid:]
    return merge(mergeSort(start), mergeSort(end))


arr = [5, 8, 1, 3, 7, 4, 2, 6, 9, 2, 2, 3, 4, 5, 12, 312, 415, 124, 123]

print(mergeSort(arr))
