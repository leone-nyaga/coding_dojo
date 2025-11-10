#include "main.h"

/**
 * -strcpy - function that copies the string pointed to by src
 *  to buffer pointed by dest
 *  @dest: buffer where the string will be copied
 *  @src: string to be copied
 *
 *  Return: Pointer to dest
 */
char *_strcpy(char *dest, char *src)
{
	int i = 0;

	while (src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';

	return (dest);
}

/**
 * main - check the code
 *
 * Return: 0
 */
int main(void)
{
	char str[] = "skibidi toilet";
	char str2[20];
	char *ptr;
	ptr = _strcpy(str2, str);
	printf("%s\n", ptr);

	return (0);
}

