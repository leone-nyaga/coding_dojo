#include <stdio.h>

/**
 * main - entry point
 *
 * Return: 0
 */

int main(void)
{
	int alph = 122;

	while (alph >= 97)
	{
		putchar(alph);
		alph--;
	}
	putchar('\n');
	return (0);
}
