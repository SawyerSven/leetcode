# 包含min函数的栈

> 剑指Offer 30.

### 题目

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

#### 示例

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
```

### 思路

- 利用一个辅助栈维护栈的最小值
- 数据进栈时，将当前数据和最小栈的栈顶元素比较，将两者比较的较小的元素再次压进最小栈中
- 出栈时主栈和辅助栈同步出栈

### 解法

```js

class MinStack {
  constructor() {
    this.stack = [];
    this.minStack = [];
  }
  push(item) {
    const minStackItem =
      this.minStack.length && item > this.minStack[this.minStack.length - 1]
        ? this.minStack[this.minStack.length - 1]
        : item;
    this.minStack.push(minStackItem);
    this.stack.push(item);
  }
  pop() {
    this.stack.pop();
    this.minStack.pop();
  }
  top() {
    return this.stack[this.stack.length - 1];
  }
  min() {
    return this.minStack[this.minStack.length - 1];
  }
}

```

优化

```js

class MinStack {
  constructor() {
    this.stack = [];
    this.minStack = [];
  }
  push(item) {
    if (!this.minStack.length || this.min() > item) {
      this.minStack.push(item);
    }
    this.stack.push(item);
  }
  pop() {
    if (this.stack[this.stack.length - 1] === this.min()) {
      this.minStack.pop();
    }
    this.stack.pop();
  }
  top() {
    return this.stack[this.stack.length - 1];
  }
  min() {
    return this.minStack[this.minStack.length - 1];
  }
}



```