#include <stdio.h>

/**
 * str_to_int - Funstion that converts strings to integers
 * @s: pointer to the string about to be convertedy
 *
 * Return: The converted integer
 */
int str_to_int(char *s)
{
	int i = 0, num = 0;

	while (s[i] != '\0')
	{
		num = num * 10 + (s[i] - '0');
		i++;
	}

	return (num);
}
