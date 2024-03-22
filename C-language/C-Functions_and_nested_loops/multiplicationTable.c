#include "main.h"

/**
 * multiplicationTable - prints the multiplication table
 */

void multiplicationTable(void)
{
	int i, j;

	printf("======================== Multiplication Table =====================\n");
	/* outer loop to iterate over rows */
	for (i = 0; i <= 10; i++)
	{
		/* inner loop to iterate over columns */
		for (j = 0; j <= 10; j++)
		{
			/* prints row times column */
			printf("%d\t", i * j);
		}

		/* move to the next row */
		printf("\n");
	}
}

/**
 * main -execution of the function
 *
 * Return: 0
 */

int main(void)
{
	/* calling the function */
	multiplicationTable();
	return (0);
}
