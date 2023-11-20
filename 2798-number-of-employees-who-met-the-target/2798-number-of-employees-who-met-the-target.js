/**
 * @param {number[]} hours
 * @param {number} target
 * @return {number}
 */
var numberOfEmployeesWhoMetTarget = function(hours, target) {
    return hours.reduce((acc, curr) => acc + (curr >= target ? 1 : 0), 0);
};
