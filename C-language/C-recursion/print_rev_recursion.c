#include "main.h"

/**
 * _print_rev_recursion - function that prints a string in reverse
 * @s: the string to be reversed
 *
 * Return: Reveresed string
 */

void _print_rev_recursion(char *s)
{
	if (*s == '\0')
	{
		return;
	}
	_print_rev_recursion(s + 1);
	_putchar(*s);
}

/**
 * main - Entry point
 *
 * Return: 0
 */

int main(void)
{
	_print_rev_recursion("\nColton Walker");
	return (0);
}
