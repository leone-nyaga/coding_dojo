#include "main.h"

/**
 * _islower - checks for lowercase character
 * @c: character to be checked
 * Return: 1 if lowercase, 0 if otherwise
 */

int _islower(int c)
{
	if (c >= 97 || c <= 122)
	{
		return (1);
	}
	else
	{
		return (0);
	}
}

/**
 * main - check the code.
 *
 * Return: Always 0.
 */
int main(void)
{
	int r;

	r = _islower('H');
	_putchar(r + '0');
	r = _islower('o');
	_putchar(r + '0');
	r = _islower(108);
	_putchar(r + '0');
	_putchar('\n');
	return (0);
}
