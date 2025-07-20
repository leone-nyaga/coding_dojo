#include "main.h"

/**
 * more_numbers - prints 10 times the numbers, from 0 to 14,
 * followed by a new line.
 */

void more_numbers(void)
{
	int nums, times;

	for (times = 0; times < 10; times++)
	{
		for (nums = 0; nums <= 14; nums++)
		{
			if (nums >= 10)
			{
				_putchar('1');
			}
			_putchar((nums % 10) + '0');
		}
		_putchar('\n');
	}
}



/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
	more_numbers();
	return (0);
}
