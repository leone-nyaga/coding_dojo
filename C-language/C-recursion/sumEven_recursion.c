#include "main.h"

/**
 * sumEven_recursion - calculates the sum of all even numbers from 1 to num
 * @num: the upper limit number
 *
 * Return: sum of all even numbers from 1 to num
 */

int sumEven_recursion(int num)
{
	if (num < 0)
	{
		return (0);
	}

	if (num % 2 == 0)
	{
		return (num + sumEven_recursion(num - 1));
	}
	else
	{
		return (sumEven_recursion(num - 1));
	}
}

/**
 * main - Entry point
 *
 * Return: 0
 */

int main(void)
{
	int num = 10;
	int result = sumEven_recursion(num);
	printf("sum of Even nums up to %d is %d\n", num, result);
	return(0);
}
