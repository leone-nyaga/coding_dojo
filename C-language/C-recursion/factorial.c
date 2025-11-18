#include "main.h"

/**
 * factorial - function that returns the factorial of a number
 * @n: the number
 *
 * Return: factorial
 */

int factorial(int n)
{
	if (n < 0)
	{
		return (-1);
	}
	if (n <= 0)
	{
		return (1);
	}
	return (n * factorial(n - 1));
}

/**
 * main - Entry point
 *
 * Return:0
 */

int main(void)
{
	int r;
	
	r = factorial(1);
	printf("%d\n", r);
	r = factorial(5);
	printf("%d\n", r);
	r = factorial(10);
	printf("%d\n", r);
	r = factorial(-1024);
	printf("%d\n", r);
	return (0);
}
