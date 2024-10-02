#include "main.h"

/**
 * showStudent - function to print student information
 * @student: student information
 */

void showStudent(Student_t student)
{
	printf("STUDENT INFORMATION...\n");
	printf("NAME: %s\n", student.name);
	printf("AGE: %d\n", student.age);
	printf("GRADE: %.2f\n", student.grade);
}
/**
 * main - entry point
 * Return: 0
 */

int main(void)
{
	Student_t student3;
	strcpy(student3.name, "Selina, Kyle");
	student3.age = 21;
	student3.grade = 90;

	showStudent(student3);

	return (0);
}
