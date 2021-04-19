def insertionSort(arr):
    for i in range(len(arr) - 1):
        if(arr[i] > arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]

        for j in range(i):
            if(arr[j] > arr[i]):
                arr[j], arr[i] = arr[i], arr[j]

    return arr


arr = [8, 5, 3, 1, 4, 6, 9, 7, 2, 11, 0, 17, 16, 993]

print(insertionSort(arr))
