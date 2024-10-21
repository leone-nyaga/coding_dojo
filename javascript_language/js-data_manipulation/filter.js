let fruits = [ "Apple", "Banana", "Mango", "Pineapple" ];

/* filter() is used to create a new array of elements that pass a specific test
 * syntax: array.filter(callback(element[, index[, array]])[, thisArg])
 */

/* prints the fruit with word length exceeding 5 */
let longWord = fruits.filter(word => word.length > 5);
console.log(longWord);
