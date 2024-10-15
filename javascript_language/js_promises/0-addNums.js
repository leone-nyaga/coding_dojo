export default function addNumbers(a, b) {
    return new Promise((resolve, reject) => {
        if (typeof a === 'number' && typeof b === 'number') {
            resolve(a + b); // If both values are numbers, return the sum
        } else {
            reject('Both arguments must be numbers'); // If any argument is not a number, reject
        }
    });
}
