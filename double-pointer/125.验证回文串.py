#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while(j > i):
            if(not s[i].isalpha() and not s[i].isdigit()):
                i += 1
                continue
            if(not s[j].isalpha() and not s[j].isdigit()):
                j -= 1
                continue
            if(s[i].lower() != s[j].lower()):
                return False
            j -= 1
            i += 1
        return True

# @lc code=end

so = Solution()

print(so.isPalindrome('race a car'))
