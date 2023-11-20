/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    var output = [];
    for (i = left; i <= right; i++){
        if (SDN(i) === true){
            output.push(i)
        }
    }
    return output;
};

function SDN(number) {
    const numStr = number.toString();
    
    for (let i = 0; i < numStr.length; i++) {
        const digit = parseInt(numStr[i]);
        
        if (digit === 0 || number % digit !== 0) {
            return false;
        }
    }
    
    return true;
}