#include "main.h"

/**
 * print_diagonal - Draws a diagonal line on the terminal
 * @n: The number of times the character '\' should be printed
 */
void print_diagonal(int n)
{
	int line, space;
	
	if (n <= 0)
	{
		_putchar('\n');
		return;
	}
	
	for (line = 0; line < n; line++)
	{
		for (space = 0; space < line; space++)
		{
			_putchar(' ');
		}
		_putchar('\\');
		_putchar('\n');
	}
}



/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
	print_diagonal(0);
	print_diagonal(2);
	print_diagonal(10);
	print_diagonal(-4);
	return (0);
}
