#!/usr/bin/node

class Person {
	constructor(name, age) {
		this.name = name;
		this.age = age;
	}

	sayHello() {
		console.log(`HI, my name is ${this.name}, and my age is ${this.age}`)
	}
}

module.exports = Person;
