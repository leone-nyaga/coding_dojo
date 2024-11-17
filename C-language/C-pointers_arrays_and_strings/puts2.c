#include "main.h"

/**
 * puts2 - prints every other character of a string, starting with the first
 * @str: the string to be printed
 */

void puts2(char *str)
{
	int i = 0;

	while(str[i] != '\0')
	{
		if(i % 2 == 0)
		{
			_putchar(str[i]);
		}
		i++;
	}
	_putchar('\n');
}

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    char *str;

    str = "0123456789";
    puts2(str);
    return (0);
}
