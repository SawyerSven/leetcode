/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
module.exports = function (people, limit) {
  if (!people || !people.length || !limit) return null;
  const sortedPeople = people.sort((x, y) => x - y);
  let first = 0;
  let last = sortedPeople.length - 1;
  let num = 0;
  while (first <= last) {
    if (sortedPeople[last] > limit) {
      last--;
      continue;
    }
    if (sortedPeople[first] + sortedPeople[last] <= limit) first++;
    last--;
    num++;
  }
  return num;
};
