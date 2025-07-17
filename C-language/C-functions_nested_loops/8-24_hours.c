#include "main.h"

/**
 * jack_bauer - prints every minute of the day of Jack Bauer
 * starting from 00:00 to 23:59
 */

void jack_bauer(void)
{
	int min, hour;

	hour = 23;

	while (hour > 0)
	{
		min = 60;

		while (min > 0)
		{
			_putchar('0' + (hour / 10));
			_putchar('0' + (hour % 10));
			_putchar(':');
			_putchar('0' + (min / 10));
			_putchar('0' + (min % 10));
			_putchar('\n');

			min--;
		}

		hour--;
	}
}

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
	jack_bauer();
	return (0);
}
