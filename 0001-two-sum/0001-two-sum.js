/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    op = [];
    for (i = 0; i < nums.length; i++) {
        for (j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                op.push(i);
                op.push(j);
                return op;
            }
        }
    }
    
};