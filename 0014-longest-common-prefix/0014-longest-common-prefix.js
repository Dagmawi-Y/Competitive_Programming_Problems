/**
 * @param {string[]} strs
 * @return {string}
 */
function longestCommonPrefix(strs) {
    if (strs.length === 0) {
        return "";
    }
    
    let longestPrefix = strs[0]; // Assume the first string is the initial longest common prefix
    
    for (let i = 1; i < strs.length; i++) {
        while (strs[i].indexOf(longestPrefix) !== 0) {
            // Reduce the assumed prefix until it matches or becomes empty
            longestPrefix = longestPrefix.substring(0, longestPrefix.length - 1);
            if (longestPrefix === "") {
                return "";
            }
        }
    }
    
    return longestPrefix;
}
