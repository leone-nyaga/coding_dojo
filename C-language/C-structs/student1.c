#include "main.h"

/**
 * displayStudebt - function that displays student information
 * @student: student information
 * Description: This function takes a student structure as a parameter
 * and prints the student's name, age, and grade.
 */

void displayStudent(struct Student student)
{
	printf("Student Information:\n");
	printf("Name: %s\n", student.name);
	printf("Age: %d\n", student.age);
	printf("Grade: %.2f\n", student.grade);
}

/**
 * main - entry point
 *
 * Description: This function initializes a student structure, assigns
 * values to the structure members, and calls displayStudent to print
 * the student's details.
 * Return: 0
 */

int main(void)
{
	struct Student student1;

	strcpy(student1.name, "Alice Johnson");
	student1.age = 20;
	student1.grade = 88.5;
	
	/* Call the function to display student information */
	displayStudent(student1);
	return 0;
}
