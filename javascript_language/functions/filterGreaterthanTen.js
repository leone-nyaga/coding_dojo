function filterGreaterThanTen(arr) {
	return arr.filter(function(num) {
		return num > 10;
	});
}

console.log(filterGreaterThanTen([1, 2, 4, 6, 13, 22, 8]));
