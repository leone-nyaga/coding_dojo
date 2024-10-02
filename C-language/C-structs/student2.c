#include "main.h"

/**
 * PrintStudent - function to print student information
 * @student: student information
 * Description: This function takes a student structure as a parameter
 * and prints the student's name, age, and grade.
 */

void printStudent(struct Student student)
{
	printf("STUDENT INFORMATION.....\n");
	printf("Name: %s\n", student.name);
	printf("Age: %d\n", student.age);
	printf("Grade: %.2f\n", student.grade);
}

/**
 * main - entry point
 * DEcription: This function initializes a student structure, assigns
 * values to the structure members, and calls displayStudent to print
 * the student's details.
 * Return: 0
 */

int main(void)
{
	struct Student student2;

	strcpy(student2.name, "Bruce, Wayne");
	student2.age = 22;
	student2.grade = 89;

	printStudent(student2);
}
