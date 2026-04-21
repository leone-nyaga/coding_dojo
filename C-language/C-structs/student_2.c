#include "main.h"

/**
 * main - Entry point'
 *
 * Return: 0
 */

int main(void)
{
	struct Student student_2;

	strcpy(student_2.name, "Mike");
	student_2.age = 23;
	strcpy(student_2.major, "Statistics");

	printf("Name: %s, Age: %d, Major: %s\n",
			student_2.name,
			student_2.age,
			student_2.major);

	return (0);
}
