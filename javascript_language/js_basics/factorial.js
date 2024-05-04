#!/usr/bin/node

//Function to calculate the factorial of a number
function factorial(num) {
	let result = 1;
	let i = 1;

// Using a while loop to calculate the factorial
while (i <= num) {
	result *= i; // Multiply result by i
	i++; // Increment i
}
return result;
}
// Calculate and display the factorial of 5
console.log("Factorial of 5:", factorial(5)); // Output: 120
