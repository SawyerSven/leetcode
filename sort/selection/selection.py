import random as ran


def selection(ans):
    for i in range(len(ans)-1):
        targetIndex = i
        for j in range(i+1, len(ans)):
            targetIndex = j if ans[j] < ans[targetIndex] else targetIndex
        if(targetIndex != i):
            ans[targetIndex], ans[i] = ans[i], ans[targetIndex]
    return ans


arr = []

for integer in range(0, 20):
    arr.append(round(ran.random() * 100))


assert sorted(arr) == selection(arr)
