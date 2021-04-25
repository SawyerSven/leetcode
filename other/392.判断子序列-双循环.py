#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            for j in range(len(t)):
                if(t[j] == i):
                    t = t[j+1:]
                    break
            else:
                return False
        return True


# @lc code=end
so = Solution()

print(so.isSubsequence('aaaaaa', 'bbaaaa'))
