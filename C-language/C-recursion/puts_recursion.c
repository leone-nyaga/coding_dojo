#include "main.h"

/**
 * _puts_recursion - function that prints a string, followed by a new line
 * @s: the string to bs printed
 *
 * Return: string
 */

void _puts_recursion(char *s)
{
	if (*s == '\0')
	{
		_putchar('\n');
		return;
	}

	_putchar(*s);
	_puts_recursion(s + 1);
}

/**
 * main - Entry point
 *
 * Return: 0
 */

int main(void)
{
	_puts_recursion("Puts with recursion");
	return (0);
}
