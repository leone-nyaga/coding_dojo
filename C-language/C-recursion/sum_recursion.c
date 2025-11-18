#include "main.h"

/**
 * sum_recursion - function the calculates the sum recursively
 * @num: number
 *
 * Return: sum
 */

int sum_recursion(int num)
{
	if (num == 0)
	{
		return (0);
	}
	return (num + sum_recursion(num - 1));
}

/**
 * main - Entry point
 *
 * Return: 0
 */

int main(void)
{
	int number, result;
	number = 11;
	result = sum_recursion(number);
	printf("%d\n", result);
	return (0);
}
