# 最小高度树

### 题目

给定一个有序整数数组，元素**各不相同且按升序排列**，编写一个算法，创建一棵**高度最小**的二叉搜索树。

示例:

```text
给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

          0 
         / \ 
       -3   9 
       /   / 
     -10  5
```

题解：

[醉翁、酒仙](https://leetcode-cn.com/u/zui-weng-jiu-xian/)

高度最小、保持高度平衡 - 左右子树节点的个数应该尽可能相近:

1. 用nums数组的中间值mid作为根节点，根据mid划分左子数组和右子数组。左子数组构建左子树

   右子数组构建右子树。

2. 以构建左子树为例：为了保持高度平衡，继续采用1中的划分方法，划分出新的左子数组和新的右子数组
3. 当左子数组/右子数组为空时，返回null。

右子数组的构建过程与上述相同



![](https://pic.leetcode-cn.com/a9ca164bafb3c69de8c5cdb87f4496b9213b794f964a38a158025f9561861507-image.png)

 图片来自醉翁、酒仙的题解、侵删

## 代码实现

```typescript
/* class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}
 */
let arr = [-10, -3, 0, 5, 9];

function sortedArrayToBST(nums: number[]): TreeNode | null {
  if (!nums.length) return null;
  let mid = Math.ceil(nums.length / 2 - 1);
  let root = new TreeNode(nums[mid]);
  root.left = sortedArrayToBST(nums.slice(0, mid));
  root.right = sortedArrayToBST(nums.slice(mid + 1));
  return root;
}

```



