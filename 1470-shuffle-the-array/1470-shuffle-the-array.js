/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    return nums.slice(0, n).flatMap((num, index) => [num, nums[n + index]]);
};
