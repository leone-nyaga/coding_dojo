#include "main.h"

/**
 * fib - compute the nth Fibonacci number using recursion
 * @n: the index of the Fibonacci sequence to compute
 *
 * Return: the nth Fibonacci number
 */

int fib(int *n)
{
	int a, b;

	if (*n == 0)
	{
		return (0);
	}
	if (*n == 1)
	{
		return (1);
	}

	a = *n - 1;
	b = *n - 2;

	return (fib(&a) + fib(&b));
}

/**
 * main - Entry point
 *
 * Return: 0
 */

int main(void)
{
	int n, result;

	n = 10;
	result = fib(&n);
	printf("Fibonacci(%d) = %d\n", n, result);

	return (0);
}
