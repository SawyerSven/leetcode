def generateNumber():
  for i in range(1,10):
    num = i
    for j in range(i+1,10):
      num = num * 10 + j

generateNumber()