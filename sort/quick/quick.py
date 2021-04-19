from typing import List


def quickSort(ans: List[int])-> List[int]:
    if(len(ans) < 2):
        return ans
    target = ans[0]
    left = []
    right = []
    for i in ans[1:]:
        if(i < target):
            left.append(i)
        else:
            right.append(i)
    return quickSort(left)+[target]+quickSort(right)

arr = [59, 43, 42, 31, 8, 48, 20, 79, 53, 53, 94, 63, 29, 59, 27, 38, 10, 72, 64, 69]

print(quickSort(arr))