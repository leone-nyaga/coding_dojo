#include "main.h"

/**
 * print_rev - function that prints a string, in reverse
 * @s: the string to be reversed
 *
 * Return: Void
 */
void print_rev(char *s)
{
	int i = 0;

	while (s[i] != '\0')
	{
		i++;
	}

	i = i - 1;
	while (i >= 0)
	{
		_putchar(s[i]);
		i--;
	}
	_putchar('\n');
}

/**
 * main - check the code
 *
 * Return: 0
 */
int main(void)
{
	char *str = "Your so skibidi, you're so fanum tax";

	print_rev(str);

	return (0);
}
