#include <stdio.h>

/**
 * main - Entry point of the program
 *
 * Return: 0(success)
 */

int main()
{
	char grade;

	printf("Enter your Grade, (A, B, C, D, E, F): ");
	scanf("%c", &grade);

	switch (grade)
	{
		case 'A':
			printf("Excellent!\n");
			break;
		case 'B':
			printf("Good job!\n");
			break;
		case 'C':
			printf("Average!\n");
			break;
		case 'D':
			printf("Needs improvement!\n");
			break;
		case 'E':
			printf("Wake up!\n");
			break;
		case 'F':
			printf("Fail!\n");
			break;
		default:
			printf("Missing Grades!\n");
	}

	return (0);
}
