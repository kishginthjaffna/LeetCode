/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    if (this.length === 0) {
        return -1; // Returning -1 if the array is empty
    }
    return this[this.length - 1]; // Returning the last element
};

// Custom function instead of a constructor
function logLastElement(array) {
    console.log(array.last());
}
/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */