#include <stdio.h>

/**
 * main - Entry point
 *
 * Return: 0
 */

int main(void)
{
	int l_alph = 97;
	int u_alph = 65;

	while (l_alph <= 122)
	{
		putchar(l_alph);
		l_alph++;
	}


	while (u_alph <= 90)
	{
		putchar(u_alph);
		u_alph++;
	}

	putchar('\n');
	return (0);
}
