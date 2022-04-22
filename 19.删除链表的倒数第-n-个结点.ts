/*
 * @lc app=leetcode.cn id=19 lang=typescript
 *
 * [19] 删除链表的倒数第 N 个结点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {

  const findFromEnd = (head: ListNode, k: number) => {
    let ahead: ListNode = head, behind: ListNode = head

    for (let i = 0; i < k; i++) {
      ahead = ahead.next
    }

    while (ahead) {
      behind = behind.next
      ahead = ahead.next
    }

    return behind
  }

  let dummy = new ListNode(-1);

  dummy.next = head

  const x = findFromEnd(dummy, n + 1)

  x.next = x.next.next

  return dummy.next

};
// @lc code=end

