let fruits = ["Apple", "Banana", "Mango", "Pineapple"];

/* splice() is used to add, delete or replace elements
 * the syntax is array.splice(start, deleteCount, item1, item2)
 * @start: the element position to start from
 * @deleteCount: how many elements to be manipulated
 * @item1, @item2: are optional, they consist of the datathat will be replaced
 */

splicedFruits = fruits.splice(1, 3, "Kiwi", "Sugarcane", "Grapes");
console.log(fruits);
/* prints the replaced elements */
console.log(splicedFruits);
