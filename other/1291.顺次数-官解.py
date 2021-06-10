#
# @lc app=leetcode.cn id=1291 lang=python3
#
# [1291] 顺次数
#
from typing import List


# @lc code=start
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = list()
        for i in range(1, 10):
            num = i
            for j in range(i + 1, 10):
                num = num * 10 + j
                if (low <= num <= high):
                    ans.append(num)
        return sorted(ans)
# @lc code=end
