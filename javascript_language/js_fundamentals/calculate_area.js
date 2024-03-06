#!/usr/bin/node

function calculateArea(radius)
{
	let area = Math.pi * Math.pow(radius, 2);
	return area;

}

let radius_js = 5;
let area_js = calculateArea(radius_js);
console.log(area_js);
