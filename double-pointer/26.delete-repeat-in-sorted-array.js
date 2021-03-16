var removeDuplicates = function (nums) {
  if (nums.length == 0) return [];
  let i = 0;
  for (let j = 1; j < nums.length; j++) {
    if (nums[i] !== nums[j]) {
      i++;
      nums[i] = nums[j];
    }
  }
  return i + 1;
};

let nums = [1, 2, 3, 4, 5, 6];
console.log(removeDuplicates(nums));
