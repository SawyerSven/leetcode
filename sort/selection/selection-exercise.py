def selectionSort(arr):
    for i in range(len(arr)):
        targetIndex = i
        for j in range(i+1, len(arr)):
            if(arr[targetIndex] > arr[j]):
                targetIndex = j
        arr[targetIndex],arr[i] = arr[i],arr[targetIndex]
    return arr

arr = [5, 3, 6, 7, 1, 4, 2, 9, 8]

selectionSort(arr)
