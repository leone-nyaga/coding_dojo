#include <stdio.h>

/**
 * main - entry point
 * Description - prints alphabet in upper and lowercase
 * Return: (0)
 */

int main()
{
	char i = 97;
	char j = 65;

	while (i <= 122)
	{
		putchar(i++);
	}
	while (j <= 90)
	{
		putchar(j++);
	}
	putchar('\n');

	return (0);
}




