#include "main.h"
/**
 * printCar - function that prints car details
 * @car: car details
 */

void printCar(Car car)
{
	printf("SHOW CAR DETAILS......\n");
	printf("Car Make: %s\n", car.make);
	printf("Car Model: %s\n", car.model);
	printf("Car Year Of Manufacture: %d\n", car.year);
	printf("Car Mileage: %.2f km\n", car.mileage);
}

/**
 * main - entry point
 * Return: 0
 */

int main(void)
{
	Car car1;

	strcpy(car1.make, "Toyota");
	strcpy(car1.model, "Camry");
	car1.year = 2019;
	car1.mileage = 1500.9;

	printCar(car1);
}
