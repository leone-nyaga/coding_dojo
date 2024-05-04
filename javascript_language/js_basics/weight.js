#!/usr/bin/node

let weight = 80.1;
let height = 1.75;

let bmi = weight / (weight * height);
let weightStatus;

if (bmi < 18.5) {
	weightStatus = "Underweight";
} else if (bmi >= 18.5 && bmi <= 24.9) {
	weightStatus = "Healthy Weight";
} else if (bmi >= 25.0 && bmi <= 29.9) {
	weightStatus = "Overweight";
} else {
	weightStatus = "Obesity";
}

console.log(weightStatus);
