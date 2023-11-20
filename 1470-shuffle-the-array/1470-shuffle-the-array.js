/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    var op = [];
    var nums1 = nums.slice(0, n);
    var nums2 = nums.slice(n);
    for (i = 0; i < nums1.length; i++){
        op.push(nums1[i], nums2[i]);
    }
    return op;
};