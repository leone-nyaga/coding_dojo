#include "main.h"

/**
 * fibonacci - compute the nth Fibonacci number using recursion
 * @n: the index of the Fibonacci sequence to compute
 *
 * Return: the nth Fibonacci number
 */
int fibonacci(int n)
{
	if (n == 0)
	{
		return (0);
	}
	if (n == 1)
	{
		return (1);
	}

	return (fibonacci(n - 1) + fibonacci(n - 2));
}

/**
 * main - check the code
 *
 * Return: 0
 */
int main(void)
{
	int n = 10;
	int result;

	result = fibonacci(n);

	printf("Fibonacci(%d) = %d\n", n, result);
	return (0);
}
