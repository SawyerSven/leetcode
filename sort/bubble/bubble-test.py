def bubbleSort(ans):
    for i in range(len(ans)):
        for j in range(len(ans) - 1 - i):
            if(ans[j] > ans[j+1]):
              ans[j],ans[j+1] = ans[j+1],ans[j]
    return ans

arr = [8, 5, 3, 1, 2, 7, 9, 4, 6]

print(bubbleSort(arr))
