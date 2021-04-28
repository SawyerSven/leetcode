#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(s_list)-1
        while(i < j):
            if(s_list[i] in vowel):
                if(s_list[j] in vowel):
                    s_list[i], s_list[j] = s_list[j], s_list[i]
                    i += 1
                    j -= 1
                    continue
                else:
                    j -= 1
                    continue
            else:
                i += 1
        return "".join(s_list)

# @lc code=end


so = Solution()
print(so.reverseVowels('hello'))
