#include <stdio.h>

/**
 * main - entry point
 * description - print 0 - 10 but using putchar
 * Return: (0)
 */

int main()
{
	int i;

	for (i = 0; i < 10; i++)
	{
		putchar(i + '0');
	}
	putchar('\n');
	return (0);
}
