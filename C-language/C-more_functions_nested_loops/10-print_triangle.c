#include "main.h"

/**
 * print_triangle - Prints a triangle using #
 * @size: The size of the triangle
 */
void print_triangle(int size)
{
	int row, space, hash;
	
	if (size <= 0)
	{
		_putchar('\n');
		return;
	}
	
	for (row = 1; row <= size; row++)
	{
		
		for (space = size - row; space > 0; space--)
		{
			_putchar(' ');
		}
		
		for (hash = 0; hash < row; hash++)
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
	print_triangle(2);
	print_triangle(10);
	print_triangle(1);
	print_triangle(0);
	return (0);
}
