#include "main.h"

/**
 * printPyramid - prints a pyramid
 * @rows - Number of rows in the pyramid
 *
 */

void printPyramid(int rows)
{
	int i, j, space;

	/* outer loop for iterating over each row */
	for (i = 1; i <= rows; i++)
	{
	/* loop for the spaces before the start of each star */
	for (space = 1; space <= rows - 1; space++)
	{
		printf(" ");
	}
	/* loop to print stars */
	for (j = 1; j <= 2 * i - 1; j++)
	{
		printf("*");
	}
	printf("\n");
	}
}

/**
 * main - entry point
 * Return: 0
 */

int main(void)
{
	int rows = 10;

	printPyramid(rows);

	return (0);
}
