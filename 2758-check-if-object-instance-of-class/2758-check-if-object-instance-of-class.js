/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj == null || typeof classFunction !== 'function') {
        return false;
    }
    if (typeof obj === 'object' || typeof obj === 'function') {
        return obj instanceof classFunction;
    }
    // For primitive types, use a different approach
    switch (classFunction) {
        case Number:
            return typeof obj === 'number';
        case String:
            return typeof obj === 'string';
        case Boolean:
            return typeof obj === 'boolean';
        case Symbol:
            return typeof obj === 'symbol';
        case BigInt:
            return typeof obj === 'bigint';
        case Object:
            // All primitive types can be wrapped into their object equivalents
            return true;
        default:
            return false;
    }
};

class Animal {}
class Dog extends Animal {}
const dog = new Dog();

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */