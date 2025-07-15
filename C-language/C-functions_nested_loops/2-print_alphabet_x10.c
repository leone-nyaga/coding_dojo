#include "main.h"

/**
 * print_alphabet_x10 - prints 10 times the alphabet,
 */

void print_alphabet_x10(void)
{
	int times = 0;

	while (times <= 9)
	{
		char alph = 97;

		while (alph <= 122)
		{
			_putchar(alph);
			alph++;
		}
		times++;
		_putchar('\n');
	}
}

/**
 * main - check the code.
 *
 * Return: Always 0.
 */
int main(void)
{
	print_alphabet_x10();
	return (0);
}
