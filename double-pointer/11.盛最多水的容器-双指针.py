#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# 左(i)右(j)指针分别指向数组的左右两端
# 容水量公式：
# ? min(i,j) * (j - i)
# 移动指针逻辑：
# * 如果两个指针大小不同，则移动较小的指针
# * 如果两个指针大小相同，则随便移动其中一个指针
# ? 双指针代表什么？
# 双指针代表的是 可以作为容器边界的所有位置的范围。
# 在一开始，双指针指向数组的左右边界，表示 数组中所有的位置都可以作为容器的边界
# 之后，每次将 对应的数字较小的那个指针 往 另一个指针 的方向移动一个位置
# 表示我们认为 这个指针不可能再作为容器的边界
# ? 为什么对应的数字较小的那个指针不可能再作为容器边界
# 假设当前左指针和右指针指向的数分别为 x 和 y,我们假设 x < y。同时两个指针之间的距离为t
# * 他们组成的容器的容量为: min(x,y) * t = x * t
# 如果我们保持左指针不变，右指针无论在哪，这个容器的容量都不会超过x*t
# ! 这里右指针只能向左移动，因为我们考虑的是第一步，也就是指针还指向数组的左右边界的时候
#

from typing import List
# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while(i < j):
            curr = min(height[i], height[j]) * (j - i)
            if(curr > max_area):
                max_area = curr
            if(height[i] > height[j]):
                j -= 1
            else:
                i += 1
        return max_area
# @lc code=end


so = Solution()
so.maxArea([2, 4, 5, 3, 1, 5, 5, 2, 6, 5, 4])
