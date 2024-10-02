#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * struct Student - Information about a student
 * @name: name of student
 * @age: age of student
 * @grade: grade of student
 */
struct Student
{
	char name[50];
	int age;
	float grade;
};

/**
 * Student_t - alias for the struct Student
 */
typedef struct Student Student_t;

/**
 * struct Car - Structure that holds car detail
 * @make: manufacturer of the car
 * @model: model of the car
 * @yaer: year of manufacture
 * @mileage: current mileage of the car
 * Description: holds information about a Car
 */

typedef struct
{
	char make[50];
	char model[50];
	int year;
	float mileage;
} Car;

void displayStudent(struct Student student);
void printStudent(struct Student student);
void showStudent(Student_t student);
void printCar(Car car);

#endif
