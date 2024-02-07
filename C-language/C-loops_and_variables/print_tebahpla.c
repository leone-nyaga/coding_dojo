#include <stdio.h>

/**
 * main - entry point
 * description - print alphabet in reverse
 * Return: 0
 */

int main()
{
	char i;
	
	for (i = 122; i >= 97; i--)
	{
		putchar(i);
	}
	putchar('\n');

	return (0);
}
