#!/usr/bin/node

let userName = prompt('What is your name?');

if (userName) {
	console.log(`Hello, ${userName}! Welcome.`);
} else {
	console.log('Hello! Welcome.');
}
