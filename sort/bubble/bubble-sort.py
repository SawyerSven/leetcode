from typing import List


class Solution:
    def bubble(self, arr: List[int], sortFlag: bool) -> List[int]:
        for i in range(0, len(arr) - 1):
            complete = True
            for j in range(0, len(arr) - 1 - i):
                if(sortFlag):
                    if(arr[j] > arr[j+1]):
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                        complete = False
                else:
                    if(arr[j] < arr[j+1]):
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                        complete = False
            if(complete):
                break
        print(arr)

so = Solution()

so.bubble([29, 10, 14, 37, 13, 7, 18, 21, 9, 11, 3], True)

#  时间复杂度：O(n^2)
#  空间复杂度：O(1)
