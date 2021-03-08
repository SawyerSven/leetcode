# 用两个栈实现队列

> 出处： 剑指Offer-面试题7

### 题目

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数appendTail和deleteHad,分别完成在队列尾部插入节点和队列头部删除节点的功能。

### 思路

- A栈存储入队元素
- 出队时,如果B栈不为空，则B栈栈顶元素即为队首元素
- 如果B栈为空，则对A栈依次次出栈，同时将出栈的元素依次压入B栈中,然后执行上一步。

两个栈，A栈存储入队数据。出队时将A队列的数据依次出栈并入栈到B栈，B栈进行依次出栈操作即弹出了要出队的数据。

### 解法

```js
 class Queue {
  constructor() {
    this.stack1 = [];
    this.stack2 = [];
  }

  appendTail(item) {
    this.stack1.push(item);
  }
  deleteHead() {
    if (!this.stack2.length) {
      while (this.stack1.length) {
        this.stack2.push(this.stack1.pop());
      }
    }
    return this.stack2.pop();
  }
  get queue() {
    let res = Array.from(this.stack2);
    return res.reverse().concat(this.stack1);
  }
};

```