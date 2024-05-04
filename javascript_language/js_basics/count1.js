#!/usr/bin/node

let count = 0;

while (count <= 9) {
	if (count == 5) {
		count++;
		continue;
	}
	console.log("The count is " + count);
	count++;
}
