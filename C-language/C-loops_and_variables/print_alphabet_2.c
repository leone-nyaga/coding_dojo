#include <stdio.h>

/**
 * main - entry point
 * description - print alphabet except q and e
 * Return: (0)
 */

int main()
{
	char i = 97;
	
	while (i <= 122)
	{
		if (i != 113 && i != 101)
		{
			putchar (i);
		}
		i++;
	}
	putchar ('\n');

	return (0);
}
