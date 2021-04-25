#
# @lc app=leetcode.cn id=344 lang=python3
# [344] 反转字符串
#
from typing import List
# @lc code=start


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        while(j > i):
            s[j], s[i] = s[i], s[j]
            j -= 1
            i += 1
        print(s)
# @lc code=end
so = Solution()
so.reverseString(['k','o','r','m','o','n','d','o'])
