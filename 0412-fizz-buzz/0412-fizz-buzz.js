/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    var arr2 = [];
    for(var i = 1; i<=n; i++){
        if (i % 3 === 0 && i % 5 === 0){
            arr2.push('FizzBuzz');
        }else if (i % 5 === 0){
            arr2.push('Buzz');
        }else if (i % 3 === 0){
            arr2.push('Fizz');
        }else {
            arr2.push(i.toString());
        }
    }
    return(arr2);
};