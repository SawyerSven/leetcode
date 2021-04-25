#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            try:
                index = t.index(s[i])
            except ValueError:
                return False
            t = t[index+1:]
        return True

# @lc code=end
so = Solution()

print(so.isSubsequence('acb', 'ahbgdc'))
