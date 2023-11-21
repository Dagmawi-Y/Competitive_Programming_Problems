/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const reversed = parseInt(x.toString().split('').reverse('').join(''));
    if (x === reversed){
        return true;
    }
    return false;
};