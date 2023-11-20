/**
 * @param {number[]} hours
 * @param {number} target
 * @return {number}
 */
var numberOfEmployeesWhoMetTarget = function(hours, target) {
    var op = 0;
    for (i = 0; i < hours.length; i++){
        if (hours[i] >= target){
            op++;
        }
    }
    return op;
};