/**
 * @param {number} celsius
 * @return {number[]}
 */
var convertTemperature = function(celsius) {
    var op = [];
    var k;
    var f;
    k = celsius + 273.15;
    f = (celsius * 1.80) + 32.00;
    op.push(k);
    op.push(f);
    return op;
};