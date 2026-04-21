#include "main.h"

/**
 * main - Entry point.
 *
 * Return: 0
 */

int main(void)
{
	struct Student student_1 = {"Leone", 25, "Statistics"};

	printf("Name: %s, Age: %d, Major: %s\n",
			student_1.name,
			student_1.age,
			student_1.major);

	return (0);
}
