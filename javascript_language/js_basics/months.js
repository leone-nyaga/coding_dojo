#!/usr/bin/node

const month = 6;
let monthName;

if (month == 1) {
	monthName = "Jan";
} else if (month == 2) {
	monthName = "Feb";
} else if (month == 3) {
	monthName = "Mar";
} else if (month == 4) {
	monthName = "April";
} else if (month == 5) {
	monthName = "May";
} else if (month == 6) {
	monthName = "June";
} else if (month == 7) {
	monthName = "July";
} else if (month == 8) {
	monthName = "Aug";
} else if (month == 9) {
	monthName = "sept";
} else if (month == 10) {
	monthName == "Oct";
} else if (month == 11) {
	monthName == "Nov";
} else if (month == 12) {
	monthName = "Dec";
} else {
	monthName = "Invalid Month";
}

console.log(monthName);
