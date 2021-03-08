const { afterEach, expect } = require('@jest/globals');
const { min } = require('lodash');
const MinStack = require('../../offer/stack-with-min');

let ms = new MinStack();

afterEach(() => {
  ms = new MinStack();
});

describe('stack with min', () => {
  it('用例测试[3,2,1,5,6,7,8]', () => {
    let arr = [3, 2, 1, 5, 6, 7, 8];
    arr.forEach((item) => ms.push(item));
    expect(ms.minStack).toEqual([3, 2, 1]);
    let i = 0;
    while (i < 6) {
      i++;
      ms.pop();
    }
    expect(ms.min()).toBe(3);
  });
  it('用例测试[null,null,0,1,0,null]', () => {
    let arr = [null, null, 0, 1, 0, null];
    arr.forEach((item) => ms.push(item));
    expect(ms.minStack).toEqual([null, null, 0, 0, null]);
    ms.pop();
    expect(ms.min()).toBe(null);
  });
});
