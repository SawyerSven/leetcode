/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var getKthFromEnd = function (head, k) {
  let curr = head;
  let nodeK = head;
  while (k > 1 && nodeK.next) {
    nodeK = nodeK.next;
    k--;
  }
  while (nodeK && nodeK.next) {
    nodeK = nodeK.next;
    curr = curr.next;
  }
  return curr;
};
