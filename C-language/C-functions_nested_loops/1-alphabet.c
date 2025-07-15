#include "main.h"

/**
 * print_alphabet -prints the alphabet, in lowercase
 *
 * Return: 0
 */

void print_alphabet(void)
{
	int alph = 97;

	while (alph <= 122)
	{
		_putchar(alph);
		alph++;
	}
	_putchar('\n');
}

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
	print_alphabet();
	return (0);
}
