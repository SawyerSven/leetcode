#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
import re
# @lc code=start


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        i, j = 0, len(s)-1
        while(i < j):
            if(s[i] != s[j]):
                return False
            i += 1
            j -= 1
        return True
# @lc code=end


so = Solution()

print(so.isPalindrome('A man, a plan, a canal: Panama'))
