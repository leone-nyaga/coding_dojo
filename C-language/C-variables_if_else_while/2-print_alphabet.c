#include <stdio.h>

/**
 * main - Entry point
 *
 * Return: 0
 */

int main(void)
{
	int alph = 97;

	while (alph <= 122)
	{
		putchar(alph);
		alph++;
	}
	putchar('\n');

	return (0);
}
