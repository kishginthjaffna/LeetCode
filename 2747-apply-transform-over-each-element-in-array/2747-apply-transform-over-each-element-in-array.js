/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const newArray = arr.map((n, index) => fn(n, index));
    return newArray;
};