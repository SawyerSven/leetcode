const numRescueBoats = require('../../double-pointer/881.boats-to-save-people');

describe('881.救生艇', () => {
  it('测试用例[1,2,3,3,4,5],limit=6', () => {
    const num = numRescueBoats([1, 2, 2, 3, 3, 4, 5], 6);
    expect(num).toBe(4);
  });
  it('测试用例[1,3,3,4,5,5],limit=6', () => {
    const num = numRescueBoats([1, 3, 3, 4, 5, 5], 6);
    expect(num).toBe(4);
  });
  it('超重测试 - 测试用例[1,4,4,5,6,7,8],limit=6',()=>{
    const num = numRescueBoats([1,4,4,5,6,7,8],6);
    expect(num).toBe(4)
  });
  it('非法输入控制',()=>{
    expect(numRescueBoats([1,2,3,4,5])).toBeNull()
    expect(numRescueBoats([])).toBeNull()
    expect(numRescueBoats(null,6)).toBeNull()
  })
});
