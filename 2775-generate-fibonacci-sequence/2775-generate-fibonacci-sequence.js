/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let first = 0;
    let second = 1;

    yield first; 
    yield second; 

    while (true) {
        let next = first + second;
        yield next;
        [first, second] = [second, next];
    }
};

function getFibonacciNumbers(n) {
    const gen = fibGenerator();
    const result = [];
    for (let i = 0; i < n; i++) {
        result.push(gen.next().value);
    }
    return result;
}


/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */