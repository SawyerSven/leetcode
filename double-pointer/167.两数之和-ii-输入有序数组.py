#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while(j > i):
            if(numbers[j] + numbers[i] > target):
                j -= 1
                continue
            elif(numbers[j] + numbers[i] < target):
                i += 1
                continue
            else:
                return [i+1,j+1]

# @lc code=end

so = Solution()

print((so.twoSum([-1,0], -1)))