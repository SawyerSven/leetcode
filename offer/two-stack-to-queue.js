module.exports = class Queue {
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
