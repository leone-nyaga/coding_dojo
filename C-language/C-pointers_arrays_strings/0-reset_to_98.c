#include "main.h"

/**
 * reset_to_98 - updates the value of the integer it points to to 98
 * @n: pointer to the integer
 *
 * Return: Void
 */

void reset_to_98(int *n)
{
	*n = 98;
}

/**
 * main - check the code
 *
 * Return: 0
 */
int main(void)
{
	int n;

	n = 402;
	printf("n=%d\n", n);
	reset_to_98(&n);
	printf("n=%d\n", n);
	return (0);
}
