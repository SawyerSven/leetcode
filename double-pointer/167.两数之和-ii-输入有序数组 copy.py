#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
from typing import List
# @lc code=start


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(numbers):
            if(target-num) in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
        # @lc code=end
so = Solution()

print(so.twoSum([2, 5, 7, 8], 9))
