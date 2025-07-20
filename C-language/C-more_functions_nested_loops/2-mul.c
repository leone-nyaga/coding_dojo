#include "main.h"

/**
 * mul - multiplies two integers
 * @a: first number
 * @b: second number
 * Return: 0
 */

int mul(int a, int b)
{
	return (a * b);
}


/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
	printf("%d\n", mul(98, 1024));
	printf("%d\n", mul(-402, 4096));
	return (0);
}
