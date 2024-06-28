/**
 * @param {number} n
 * @return {Function} counter
 */

function createCounter(n) {
    let current = n;
    return function() {
        return current++;
    };
}

// Simulating the calls and printing the results
function simulateCalls(n, calls) {
    const counter = createCounter(n);
    const results = calls.map(call => counter());
    return results;
}

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */