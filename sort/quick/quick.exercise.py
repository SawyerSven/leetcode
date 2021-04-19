def quickSort(ans):
    if(len(ans) < 2):
        return ans
    left = []
    right = []
    target = ans[0]
    for i in ans[1:]:
        if(i > target):
            right.append(i)
        else:
            left.append(i)
    return quickSort(left) + [target] + quickSort(right)


arr = [6, 8, 1, 3, 7, 4, 5, 2, 9, 7, 7, 7, 8, 4, 3, 2]

print(quickSort(arr))
