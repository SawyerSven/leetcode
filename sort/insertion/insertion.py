import random

def insertion(ans):
  for i in range(len(ans) - 1):
    if(ans[i] > ans[i + 1]):
      ans[i],ans[i+1] = ans[i+1],ans[i]
    curr = i
    while(curr > 0):
      if(ans[curr] < ans[curr - 1]):
        ans[curr],ans[curr - 1] = ans[curr-1],ans[curr]
        curr = curr - 1
      else:
        break
  return ans

arr = []

for integer in range(0,20):
  arr.append(round(random.random() * 100) )

assert sorted(arr) == insertion(arr)