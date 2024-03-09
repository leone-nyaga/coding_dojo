#include <stdio.h>

/**
 * is_vowel - Checks if character is a Vowel
 * @c - Character to be checked
 * Return: 1 if vowel else 0 
 */

int is_vowel(char c)
{
	switch (c)
	{
		case 'A':
		case 'a':
		case 'E':
		case 'e':
		case 'i':
		case 'I':
		case 'O':
		case 'o':
		case 'U':
		case 'u':
			return (1);
		default:
			return (0);
	}
}

/**
 * main - Entry point
 * Description - Identifies character input
 * Return: 0 success
 */

int main(void)
{
	char vowel;

	printf("Enter a letter: \n");
	scanf("%c\n", &vowel);

	if (is_vowel(vowel))
	{
		printf("%c is vowel\n", vowel);
	}
	else
	{
		printf("%c is a consonant\n", vowel);
	}
	return (0);
}
