const { expect } = require('@jest/globals');
const Queue = require('../../offer/two-stack-to-queue');

let queue = new Queue();

const init = () => {
  for (let i = 1; i < 6; i++) {
    queue.appendTail(i);
  }
};

beforeEach(() => {
  queue = new Queue();
  init();
});

describe('two stack to queue', () => {
  it('Queue的appendTail方法', () => {
    expect(queue.queue).toEqual([1, 2, 3, 4, 5]);
  });
  it('Queue的deleteHead方法', () => {
    queue.deleteHead();
    expect(queue.queue).toEqual([2, 3, 4, 5]);
    queue.deleteHead();
    expect(queue.queue).toEqual([3, 4, 5]);
  });
  describe('Queue组合方法', () => {
    it('先删除后添加', () => {
      queue.deleteHead();
      queue.deleteHead();
      queue.appendTail(6);
      expect(queue.queue).toEqual([3, 4, 5, 6]);
    });
    it('边界测试', () => {
      while (queue.queue.length) {
        queue.deleteHead();
      }
      expect(queue.deleteHead()).toBe(undefined);
    });
    it('组合测试', () => {
      queue.appendTail(6);
      queue.deleteHead();
      queue.appendTail(7);
      queue.appendTail(8);
      queue.deleteHead();
      queue.deleteHead();
      queue.deleteHead();
      queue.appendTail(10086);
      expect(queue.queue).toEqual([5, 6, 7, 8, 10086]);
    });
  });
});
