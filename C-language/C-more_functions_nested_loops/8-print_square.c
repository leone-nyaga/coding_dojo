#include "main.h"

/**
 * print_square - Prints a square using #
 * @size: The size of the square
 */
void print_square(int size)
{
	int row, col;
	
	if (size <= 0)
	{
		_putchar('\n');
		return;
	}
	
	for (row = 0; row < size; row++)
	{
		for (col = 0; col < size; col++)
		{
			_putchar('#');
		}
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
	print_square(2);
	print_square(10);
	print_square(0);
	return (0);
}
