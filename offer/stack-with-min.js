module.exports = class MinStack {
  constructor() {
    this.stack = [];
    this.minStack = [];
  }
  push(item) {
    if (!this.minStack.length || this.min() >= item) {
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