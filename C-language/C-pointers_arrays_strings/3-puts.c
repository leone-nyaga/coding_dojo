#include "main.h"

/**
 * _puts - function that prints a string, followed by a new line, to stdout
 * @str: the string to be printed
 *
 * Return: Void
 */

void _puts(char *str)
{
	int i = 0;

	while (str[i] != '\0')
	{
		_putchar(str[i]);
		i++;
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
	char *str;

	str = "Fanum Tax!";
	_puts(str);
	

	return (0);
}
