#include "main.h"

/**
 * _strlen - function that returns the length of a string
 * @s: string
 *
 * Return: Number of characters in a string
 */
int _strlen(char *s)
{
	int len = 0;

	while (s[len] != 0)
	{
		len++;
	}

	return (len);
}

/**
 * main - check the code
 *
 * Return: 0
 */
int main(void)
{
	char *str;
	int length;

	str = "Skibidi toilet!";
	length = _strlen(str);
	printf("%d\n", length);
	return (0);
}
