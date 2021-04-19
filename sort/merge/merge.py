def merge(front, end):
    temp = []
    while(len(front) and len(end)):
        if(front[0] < end[0]):
            temp.append(front.pop(0))
        else:
            temp.append(end.pop(0))
    while(len(front)):
        temp.append(front.pop(0))
    while(len(end)):
        temp.append(end.pop(0))
    return temp

def mergeSort(ans):
  if(len(ans) < 2):
    return ans
  mid = len(ans) // 2
  front = ans[:mid]
  end = ans[mid:]
  return merge(mergeSort(front),mergeSort(end))

arr = [59, 43, 42, 31, 8, 48, 20, 79, 53, 53, 94, 63, 29, 59, 27, 38, 10, 72, 64, 69]

print(mergeSort(arr))