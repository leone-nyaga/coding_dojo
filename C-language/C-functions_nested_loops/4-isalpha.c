#include "main.h"

/**
 * _isalpha - checks for alphabetic character
 * @c: character to be checked
 */

int _isalpha(int c)
{
	if ((c >= 65 && c <= 90) || (c >= 97 && c <= 122))
	{
		return (1);
	}
		return (0);
}


/**
 * main - check the code.
 *
 * Return: Always 0.
 */
int main(void)
{
	int r;
	
	r = _isalpha('H');
	_putchar(r + '0');
	r = _isalpha('o');
	_putchar(r + '0');
	r = _isalpha(108);
	_putchar(r + '0');
	r = _isalpha(';');
	_putchar(r + '0');
	_putchar('\n');
	return (0);
}
